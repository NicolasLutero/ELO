

class ValidadeDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, data_inicio, data_fim, cargo_id):
        cursor = self.connection.cursor()

        cursor.execute(
             """
            INSERT INTO validade (data_inicio, data_fim, cargo_id)
            VALUES (%s, %s, %s) RETURNING id
            """,
            (data_inicio, data_fim, cargo_id)
        )

        id = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return {"id": id,
                "data_inicio": data_inicio,
                "data_fim": data_fim,
                "cargo_id": cargo_id}

    def get_by_id(self, id):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT id, data_inicio, data_fim, cargo_id
            FROM validade
            WHERE id = %s
            """,
            (id,)
        )

        row = cursor.fetchone()
        cursor.close()

        if row is None:
            return None

        return {
            "id": row[0],
            "data_inicio": row[1],
            "data_fim": row[2],
            "cargo_id": row[3]
        }

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT id, data_inicio, data_fim, cargo_id
            FROM validade
         """)

        validades = [
            {
                "id": row[0],
                "data_inicio": row[1],
                "data_fim": row[2],
                "cargo_id": row[3]
            }
            for row in cursor.fetchall()
        ]

        cursor.close()
        return validades

    def update(self, validade):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            UPDATE validade
            SET data_inicio = %s,
                data_fim = %s,
                cargo_id = %s
            WHERE id = %s
            """,
            (
                validade.data_inicio,
                validade.data_fim,
                validade.cargo_id,
                validade.id
            )
        )

        self.connection.commit()
        cursor.close()
