from cargo import Cargo

class CargoDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, nome, descricao, vagas, gremio_id):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO cargo (nome, descricao, vagas, gremio_id)
            VALUES (%s, %s, %s, %s)
            RETURNING id
            """,
            (nome, descricao, vagas, gremio_id)
        )

        id = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return Cargo(id, nome, descricao, vagas, gremio_id)

    def get_by_id(self, id):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT id, nome, descricao, vagas, gremio_id
            FROM cargo
            WHERE id = %s
            """,
            (id,)
        )

        row = cursor.fetchone()
        cursor.close()

        if row is None:
            return None

        return Cargo(
            id=row[0],
            nome=row[1],
            descricao=row[2],
            vagas=row[3],
            gremio_id=row[4]
        )

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT id, nome, descricao, vagas, gremio_id
            FROM cargo
        """)

        cargos = [
            Cargo(
                id=row[0],
                nome=row[1],
                descricao=row[2],
                vagas=row[3],
                gremio_id=row[4]
            )
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
            WHERE id = %s
            """,
            (
                cargo.nome,
                cargo.descricao,
                cargo.vagas,
                cargo.gremio_id,
                cargo.id
            )
        )

        self.connection.commit()
        cursor.close()