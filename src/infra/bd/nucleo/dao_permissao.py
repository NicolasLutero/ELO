

class PermissaoDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, nome, descricao):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO permissao (nome, descricao)
            VALUES (%s, %s) RETURNING id_elo
            """,
            (nome, descricao)
        )

        id_elo = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return {"id_elo": id_elo,
                "nome": nome,
                "descricao": descricao}

    def get_by_id(self, id_elo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT id_elo, nome, descricao
            FROM permissao
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
            "descricao": row[2]
        }

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT id_elo, nome, descricao
            FROM permissao
         """)

        permissoes = [
            {
                "id_elo": row[0],
                "nome": row[1],
                "descricao": row[2]
            }
            for row in cursor.fetchall()
        ]

        cursor.close()
        return permissoes

    def update(self, permissao):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            UPDATE permissao
            SET nome     = %s,
                descricao = %s
            WHERE id_elo = %s
            """,
            (
                permissao.nome,
                permissao.descricao,
                permissao.id_elo
            )
        )

        self.connection.commit()
        cursor.close()
