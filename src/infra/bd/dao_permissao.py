from permissao import Permissao

class PermissaoDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, nome, descricao):
        cursor = self.connection.cursor()

        cursor.execute(
             """
            INSERT INTO permissao (nome, descricao)
            VALUES (%s, %s) RETURNING id
            """,
            (nome, descricao)
        )

        id = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return Permissao(id, nome, descricao)

    def get_by_id(self, id):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT id, nome, descricao
            FROM permissao
            WHERE id = %s
            """,
            (id,)
        )

        row = cursor.fetchone()
        cursor.close()

        if row is None:
            return None

        return Permissao(
            id=row[0],
            nome=row[1],
            descricao=row[2]
        )

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT id, nome, descricao
            FROM permissao
         """)

        permissoes = [
            Permissao(
                id=row[0],
                nome=row[1],
                descricao=row[2]
            )
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
            WHERE id = %s
            """,
            (
                permissao.nome,
                permissao.descricao,
                permissao.id
            )
        )

        self.connection.commit()
        cursor.close()