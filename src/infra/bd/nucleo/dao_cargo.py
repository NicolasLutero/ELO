

class CargoDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, nome, descricao, vagas, gremio_id):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO cargo (nome, descricao, vagas)
            VALUES (%s, %s, %s)
            RETURNING idelo
            """,
            (nome, descricao, vagas)
        )

        idelo = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return {"idelo": idelo,
                "nome": nome,
                "descricao": descricao,
                "vagas": vagas}

    def get_by_id(self, idelo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT idelo, nome, descricao, vagas
            FROM cargo
            WHERE idelo = %s
            """,
            (idelo,)
        )

        row = cursor.fetchone()
        cursor.close()

        if row is None:
            return None

        return {"idelo": row[0],
                "nome": row[1],
                "descricao": row[2],
                "vagas": row[3]
                }

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT idelo, nome, descricao, vagas
            FROM cargo
        """)

        cargos = [
            {
                "idelo": row[0],
                "nome": row[1],
                "descricao": row[2],
                "vagas": row[3]
            }
            for row in cursor.fetchall()
        ]

        cursor.close()
        return cargos

    def update(self, cargo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            UPDATE cargo
            SET nome = %s,
                descricao = %s,
                vagas = %s
            WHERE idelo = %s
            """,
            (
                cargo.nome,
                cargo.descricao,
                cargo.vagas,
                cargo.idelo
            )
        )

        self.connection.commit()
        cursor.close()

    def add_permissao(self, cargo_idelo, permissao_idelo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO cargo_concede_permissao
                (cargo_idelo, permissao_idelo)
            VALUES (%s, %s)
            """,
            (cargo_idelo, permissao_idelo)
        )

        self.connection.commit()
        cursor.close()


    def remove_permissao(self, cargo_idelo, permissao_idelo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            DELETE FROM cargo_concede_permissao
            WHERE cargo_idelo = %s
              AND permissao_idelo = %s
            """,
            (cargo_idelo, permissao_idelo)
        )

        self.connection.commit()
        cursor.close()

    def add_cargo(self, usuario_idelo, cargo_idelo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO ocupa (usuario_idelo, cargo_idelo)
            VALUES (%s, %s)
            """,
            (usuario_idelo, cargo_idelo)
        )

        self.connection.commit()
        cursor.close()

    def remove_cargo(self, usuario_idelo, cargo_idelo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            DELETE FROM ocupa
            WHERE usuario_idelo = %s
              AND cargo_idelo = %s
            """,
            (usuario_idelo, cargo_idelo)
        )

        self.connection.commit()
        cursor.close()
