# Essa classe deve implementar interações com APIs externas que
# determinem a que Instituição e Etapa de Ensino pertence este aluno.

class InstituicaoEEtapaPorRa:
    @staticmethod
    def get(ra):
        if ra is None:
            return None
        else:
            return 1, "3"
