from usuario import Usuario

class UsuarioDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, nome, cpf, email, ra, senha, gremio_id=None):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO Usuario (nome, cpf, email, ra, senha, gremio_id)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id
            """,
            (nome, cpf, email, ra, senha, gremio_id)
        )

        id = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return Usuario(id, nome, cpf, email, ra, senha, gremio_id)

    def get_by_id(self, id):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT id, nome, cpf, email, ra, senha, gremio_id
            FROM Usuario
            WHERE id = %s
            """,
            (id,)
        )

        row = cursor.fetchone()
        cursor.close()

        if row is None:
            return None

        return Usuario(
            id=row[0],
            nome=row[1],
            cpf=row[2],
            email=row[3],
            ra=row[4],
            senha=row[5],
            gremio_id=row[6]
        )

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT id, nome, cpf, email, ra, senha, gremio_id
            FROM Usuario
        """)

        Usuarios = [
            Usuario(
                id=row[0],
                nome=row[1],
                cpf=row[2],
                email=row[3],
                ra=row[4],
                senha=row[5],
                gremio_id=row[6]
            )
            for row in cursor.fetchall()
        ]

        cursor.close()
        return Usuarios

    def update(self, usuario):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            UPDATE Usuario
            SET nome = %s,
                cpf = %s,
                email = %s,
                ra = %s,
                senha = %s,
                gremio_id = %s
            WHERE id = %s
            """,
            (
                usuario.nome,
                usuario.cpf,
                usuario.email,
                usuario.ra,
                usuario.senha,
                usuario.gremio_id,
                usuario.id
            )
        )

        self.connection.commit()
        cursor.close()