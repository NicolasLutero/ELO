

class CargoDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, nome, descricao, vagas, gremio_id):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO cargo (nome, descricao, vagas, gremio_id)
            VALUES (%s, %s, %s, %s)
            RETURNING id_elo
            """,
            (nome, descricao, vagas, gremio_id)
        )

        id_elo = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return {"id_elo": id_elo,
                "nome": nome,
                "descricao": descricao,
                "vagas": vagas,
                "gremio_id": gremio_id}

    def get_by_id(self, id_elo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT id_elo, nome, descricao, vagas, gremio_id
            FROM cargo
            WHERE id_elo = %s
            """,
            (id_elo,)
        )

        row = cursor.fetchone()
        cursor.close()

        if row is None:
            return None

        return {"id_elo": row[0],
                "nome": row[1],
                "descricao": row[2],
                "vagas": row[3],
                "gremio_id": row[4]
                }

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT id_elo, nome, descricao, vagas, gremio_id
            FROM cargo
        """)

        cargos = [
            {
                "id_elo": row[0],
                "nome": row[1],
                "descricao": row[2],
                "vagas": row[3],
                "gremio_id": row[4]
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
                vagas = %s,
                gremio_id = %s
            WHERE id_elo = %s
            """,
            (
                cargo.nome,
                cargo.descricao,
                cargo.vagas,
                cargo.gremio_id,
                cargo.id_elo
            )
        )

        self.connection.commit()
        cursor.close()

    def add_permissao(self, cargo_id_elo, permissao_id_elo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO cargo_concede_permissao
                (cargo_id_elo, permissao_id_elo)
            VALUES (%s, %s)
            """,
            (cargo_id_elo, permissao_id_elo)
        )

        self.connection.commit()
        cursor.close()


    def remove_permissao(self, cargo_id_elo, permissao_id_elo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            DELETE FROM cargo_concede_permissao
            WHERE cargo_id_elo = %s
              AND permissao_id_elo = %s
            """,
            (cargo_id_elo, permissao_id_elo)
        )

        self.connection.commit()
        cursor.close()

    def add_cargo(self, usuario_id_elo, cargo_id_elo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO ocupa (usuario_id_elo, cargo_id_elo)
            VALUES (%s, %s)
            """,
            (usuario_id_elo, cargo_id_elo)
        )

        self.connection.commit()
        cursor.close()

    def remove_cargo(self, usuario_id_elo, cargo_id_elo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            DELETE FROM ocupa
            WHERE usuario_id_elo = %s
              AND cargo_id_elo = %s
            """,
            (usuario_id_elo, cargo_id_elo)
        )

        self.connection.commit()
        cursor.close()
