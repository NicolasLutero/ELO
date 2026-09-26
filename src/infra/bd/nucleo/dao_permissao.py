

class PermissaoDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, nome, descricao):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO permissao (nome, descricao)
            VALUES (%s, %s) RETURNING idelo
            """,
            (nome, descricao)
        )

        idelo = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return {"idelo": idelo,
                "nome": nome,
                "descricao": descricao}

    def get_by_id(self, idelo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT idelo, nome, descricao
            FROM permissao
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
            "descricao": row[2]
        }

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT idelo, nome, descricao
            FROM permissao
         """)

        permissoes = [
            {
                "idelo": row[0],
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
            WHERE idelo = %s
            """,
            (
                permissao.nome,
                permissao.descricao,
                permissao.idelo
            )
        )

        self.connection.commit()
        cursor.close()
