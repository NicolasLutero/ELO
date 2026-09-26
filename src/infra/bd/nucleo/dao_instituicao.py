

class InstituicaoDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, nome, endereco):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO instituicao (nome, endereco)
            VALUES (%s, %s) RETURNING idelo
            """,
            (nome, endereco)
        )

        idelo = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return {"idelo": idelo,
                "nome": nome,
                "endereco": endereco}

    def get_by_id(self, idelo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT idelo, nome, endereco
            FROM instituicao
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
            "endereco": row[2]
        }

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT idelo, nome, endereco
            FROM instituicao
            """)

        instituicoes = [
            {
                "idelo": row[0],
                "nome": row[1],
                "endereco": row[2]
            }
            for row in cursor.fetchall()
        ]

        cursor.close()
        return instituicoes

    def update(self, instituicao):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            UPDATE instituicao
            SET nome = %s,
                endereco = %s
            WHERE idelo = %s
            """,
            (
                instituicao.nome,
                instituicao.endereco,
                instituicao.idelo
            )
        )

        self.connection.commit()
        cursor.close()
