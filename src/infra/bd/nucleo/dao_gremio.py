

class GremioDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, nome, instituicao, etapa_ensino, legitimado=False, fundador_idelo=None, cargo_adm_idelo=None):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO gremio (nome, instituicao_id, etapa_ensino, legitimado, fundador_idelo, cargo_adm_idelo)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING idelo
            """,
            (nome, instituicao, etapa_ensino, legitimado, fundador_idelo, cargo_adm_idelo)
        )

        idelo = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return {"idelo": idelo,
                "nome": nome,
                "instituicao": instituicao,
                "etapa_ensino": etapa_ensino,
                "legitimado": legitimado,
                "fundador_idelo": fundador_idelo,
                "cargo_adm_idelo": cargo_adm_idelo}

    def get_by_id(self, idelo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT idelo, nome, instituicao_id, etapa_ensino, legitimado, fundador_idelo, cargo_adm_idelo
            FROM gremio
            WHERE idelo = %s
            """,
            (idelo,)
        )

        row = cursor.fetchone()
        cursor.close()

        if row is None:
            return None

        return {
            "idelo": row[0],
            "nome": row[1],
            "instituicao": row[2],
            "etapa_ensino": row[3],
            "legitimado": row[4],
            "fundador_idelo": row[5],
            "cargo_adm_idelo": row[6]
        }

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT idelo, nome, instituicao_id, etapa_ensino, legitimado, fundador_idelo, cargo_adm_idelo
            FROM gremio
        """)

        gremios = [
            {
                "idelo": row[0],
                "nome": row[1],
                "instituicao": row[2],
                "etapa_ensino": row[3],
                "legitimado": row[4],
                "fundador_idelo": row[5],
                "cargo_adm_idelo": row[6]
            }
            for row in cursor.fetchall()
        ]

        cursor.close()
        return gremios

    def get_by_inst_etapa(self, instituicao_idelo, etapa):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT idelo, nome, instituicao_id, etapa_ensino, legitimado, fundador_idelo, cargo_adm_idelo
            FROM gremio
            WHERE instituicao_id = %s
                AND etapa_ensino = %s
            """,
            (instituicao_idelo, etapa)
        )

        row = cursor.fetchone()
        cursor.close()

        if row is None:
            return None

        return {
            "idelo": row[0],
            "nome": row[1],
            "instituicao": row[2],
            "etapa_ensino": row[3],
            "legitimado": row[4],
            "fundador_idelo": row[5],
            "cargo_adm_idelo": row[6]
        }

    def check_availability_inst_etapa(self, inst, etapa):
        cursor = self.connection.cursor()

        cursor.execute(
            f"""
                SELECT count(idelo)
                FROM gremio
                WHERE instituicao_id = %s 
                    AND etapa_ensino = %s
            """,
            (inst, etapa)
        )

        row = cursor.fetchone()
        cursor.close()

        return row[0] == 0

    def update(self, gremio):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            UPDATE gremio
            SET nome = %s,
                instituicao_id = %s,
                etapa_ensino = %s,
                legitimado = %s,
                fundador_idelo = %s,
                cargo_adm_idelo = %s
            WHERE idelo = %s
            """,
            (
                gremio.nome,
                gremio.instituicao,
                gremio.etapa_ensino,
                gremio.legitimado,
                gremio.fundador_idelo,
                gremio.cargo_adm_idelo,
                gremio.idelo
            )
        )

        self.connection.commit()
        cursor.close()

    def create_permissoes(self, gremio_idelo, att_per):
        cursor = self.connection.cursor()

        columns = ["gremio_idelo"] + list(att_per.keys())
        values = [gremio_idelo] + list(att_per.values())

        placeholders = ", ".join(["%s"] * len(values))
        columns_sql = ", ".join(columns)

        cursor.execute(
            f"""
            INSERT INTO gremio_permissoes ({columns_sql})
            VALUES ({placeholders})
            """,
            values
        )

        self.connection.commit()
        cursor.close()
