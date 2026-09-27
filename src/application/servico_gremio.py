from datetime import date
from dateutil.relativedelta import relativedelta

from src.application.erros.gremio_erro import GremioJaExisteInstEtapaErro, GremioNaoExisteErro
from src.application.erros.usuario_erro import UsuarioNaoTemRAErro, UsuarioNaoExisteErro
from src.domain.nucleo.cargo import Cargo
from src.domain.nucleo.gremio import Gremio
from src.domain.nucleo.permissao import Permissao
from src.domain.nucleo.usuario import Usuario
from src.infra.api_externa.instituicao_etapa_por_ra import InstituicaoEEtapaPorRa
from src.infra.bd.nucleo.dao_cargo import CargoDAO
from src.infra.bd.nucleo.dao_gremio import GremioDAO
from src.infra.bd.nucleo.dao_permissao import PermissaoDAO
from src.infra.bd.nucleo.dao_usuario import UsuarioDAO
from src.infra.bd.nucleo.dao_validade import ValidadeDAO


class ServicoGremio:
    def __init__(self, dao_gremio: GremioDAO, dao_usuario: UsuarioDAO, dao_cargo: CargoDAO, dao_permissao: PermissaoDAO, dao_validade: ValidadeDAO):
        self.dao_gremio = dao_gremio
        self.dao_usuario = dao_usuario
        self.dao_cargo = dao_cargo
        self.dao_permissao = dao_permissao
        self.dao_validade = dao_validade

    def criar_gremio(self, criador_idelo, nome_gremio):
        criador = self.dao_usuario.get_by_idelo(criador_idelo)
        if criador is None:
            raise UsuarioNaoExisteErro()
        criador = Usuario(**criador)

        ra = criador.ra
        if ra is None:
            raise UsuarioNaoTemRAErro()

        instituicao_idelo, etapa = InstituicaoEEtapaPorRa.get(ra)
        if not self.dao_gremio.check_availability_inst_etapa(instituicao_idelo, etapa):
            raise GremioJaExisteInstEtapaErro()

        dados_novo_gremio = self.dao_gremio.create(nome_gremio, instituicao_idelo, etapa)
        gremio = Gremio(**dados_novo_gremio)

        criador.gremio_idelo = gremio.idelo
        self.dao_usuario.update(criador)

        dados_cargo_adm = self.dao_cargo.create(
            f"Adm do Grêmio {gremio.idelo}",
            f"Cargo de ADM absoluto para o Grêmio {gremio.idelo}",
            5,
            gremio.idelo)
        cargo_adm = Cargo(**dados_cargo_adm)

        gremio.cargo_adm_idelo = cargo_adm.idelo
        self.dao_gremio.update(gremio)

        per_edit_name = Permissao(**self.dao_permissao.create(
            f"Editar Nome do Grêmio {gremio.idelo}",
            f"Permite editar o nome deste Grêmio."))
        per_add_cargo = Permissao(**self.dao_permissao.create(
            f"Add Cargo ao Grêmio {gremio.idelo}",
            f"Permite adicionar cargos a este Grêmio."))
        att_per = {
            "per_edit_name": per_edit_name.idelo,
            "per_add_cargo": per_add_cargo.idelo,
        }
        self.dao_gremio.create_permissoes(gremio.idelo, att_per)

        self.dao_cargo.add_permissao(cargo_adm.idelo, per_edit_name.idelo)
        self.dao_cargo.add_permissao(cargo_adm.idelo, per_add_cargo.idelo)

        data_inicio = date.today()
        data_fim = data_inicio + relativedelta(months=1)
        self.dao_validade.create(data_inicio, data_fim, cargo_adm.idelo)
        self.dao_cargo.add_cargo(criador.idelo, cargo_adm.idelo)
        return gremio

    def legitimar_gremio(self, gremio_idelo):
        gremio = self.dao_gremio.get_by_idelo(gremio_idelo)
        if gremio is None:
            raise GremioNaoExisteErro()

        gremio.legitimidade = True
        self.dao_gremio.update(gremio)
