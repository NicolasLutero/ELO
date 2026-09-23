

class InstituicaoDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, nome, endereco):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO instituicao (nome, endereco)
            VALUES (%s, %s) RETURNING id_elo
            """,
            (nome, endereco)
        )

        id_elo = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return {"id_elo": id_elo,
                "nome": nome,
                "endereco": endereco}

    def get_by_id(self, id_elo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT id_elo, nome, endereco
            FROM instituicao
            WHERE id_elo = %s
            """,
            (id_elo,)
        )

        row = cursor.fetchone()
        cursor.close()

        if row is None:
            return None

        return {
            "id_elo": row[0],
            "nome": row[1],
            "endereco": row[2]
        }

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT id_elo, nome, endereco
            FROM instituicao
            """)

        instituicoes = [
            {
                "id_elo": row[0],
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
            WHERE id_elo = %s
            """,
            (
                instituicao.nome,
                instituicao.endereco,
                instituicao.id_elo
            )
        )

        self.connection.commit()
        cursor.close()
