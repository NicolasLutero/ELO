

class UsuarioDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, nome, cpf, email, ra, senha, gremio_idelo=None):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO Usuario (nome, cpf, email, ra, senha, gremio_idelo)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING idelo
            """,
            (nome, cpf, email, ra, senha, gremio_idelo)
        )

        idelo = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return {"idelo": idelo,
                "nome": nome,
                "cpf": cpf,
                "email": email,
                "ra": ra,
                "senha": senha,
                "gremio_idelo": gremio_idelo}

    def get_by_idelo(self, idelo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT idelo, nome, cpf, email, ra, senha, gremio_idelo
            FROM Usuario
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
            "cpf": row[2],
            "email": row[3],
            "ra": row[4],
            "senha": row[5],
            "gremio_idelo": row[6]
        }

    def get_by_email_senha(self, email, senha):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT id_elo, nome, cpf, email, ra, senha, gremio_idelo
            FROM Usuario
            WHERE email = %s
                AND senha = %s
            """,
            (email, senha,)
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
            "gremio_idelo": row[6]
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
                SELECT count(idelo)
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
            SELECT idelo, nome, cpf, email, ra, senha, gremio_idelo
            FROM Usuario
        """)

        usuarios = [
            {
                "idelo": row[0],
                "nome": row[1],
                "cpf": row[2],
                "email": row[3],
                "ra": row[4],
                "senha": row[5],
                "gremio_idelo": row[6]
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
                gremio_idelo = %s
            WHERE idelo = %s
            """,
            (
                usuario.nome,
                usuario.cpf,
                usuario.email,
                usuario.ra,
                usuario.senha,
                usuario.gremio_idelo,
                usuario.idelo
            )
        )

        self.connection.commit()
        cursor.close()
