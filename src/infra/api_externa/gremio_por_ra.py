# Essa classe deve implementar interações com APIs externas que
# determinem a que Instituição e Etapa de Ensino pertence este aluno.

class GremioPorRa:
    @staticmethod
    def get(ra):
        if ra is None:
            return None
        try:
            return int(ra[0])
        except ValueError:
            return 0
