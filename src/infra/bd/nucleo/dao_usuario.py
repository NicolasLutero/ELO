

class UsuarioDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, nome, cpf, email, ra, senha, gremio_id=None):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO Usuario (nome, cpf, email, ra, senha, gremio_id)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id_elo
            """,
            (nome, cpf, email, ra, senha, gremio_id)
        )

        id_elo = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return {"id_elo": id_elo,
                "nome": nome,
                "cpf": cpf,
                "email": email,
                "ra": ra,
                "senha": senha,
                "gremio_id": gremio_id}

    def get_by_id(self, id_elo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT id_elo, nome, cpf, email, ra, senha, gremio_id
            FROM Usuario
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
            "cpf": row[2],
            "email": row[3],
            "ra": row[4],
            "senha": row[5],
            "gremio_id": row[6]
        }

    def check_availability_cpf(self, cpf):
        return self._check_availability("cpf = %s", cpf)

    def check_availability_email(self, email):
        return self._check_availability("email = %s", email)

    def check_availability_ra(self, ra):
        return self._check_availability("ra = %s", ra)

    def _check_availability(self, sql, valor):
        cursor = self.connection.cursor()

        cursor.execute(
            f"""
                SELECT count(id_elo)
                FROM usuario
                WHERE {sql}
            """,
            (valor,)
        )

        row = cursor.fetchone()
        cursor.close()

        return row[0] == 0

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT id_elo, nome, cpf, email, ra, senha, gremio_id
            FROM Usuario
        """)

        usuarios = [
            {
                "id_elo": row[0],
                "nome": row[1],
                "cpf": row[2],
                "email": row[3],
                "ra": row[4],
                "senha": row[5],
                "gremio_id": row[6]
            }
            for row in cursor.fetchall()
        ]

        cursor.close()
        return usuarios

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
            WHERE id_elo = %s
            """,
            (
                usuario.nome,
                usuario.cpf,
                usuario.email,
                usuario.ra,
                usuario.senha,
                usuario.gremio_id,
                usuario.id_elo
            )
        )

        self.connection.commit()
        cursor.close()
