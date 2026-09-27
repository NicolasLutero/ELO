

class ValidadeDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, data_inicio, data_fim, cargo_idelo):
        cursor = self.connection.cursor()

        cursor.execute(
             """
            INSERT INTO validade (data_inicio, data_fim, cargo_idelo)
            VALUES (%s, %s, %s) RETURNING idelo
            """,
            (data_inicio, data_fim, cargo_idelo)
        )

        idelo = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return {"idelo": idelo,
                "data_inicio": data_inicio,
                "data_fim": data_fim,
                "cargo_idelo": cargo_idelo}

    def get_by_idelo(self, idelo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT idelo, data_inicio, data_fim, cargo_idelo
            FROM validade
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
            "data_inicio": row[1],
            "data_fim": row[2],
            "cargo_idelo": row[3]
        }

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT idelo, data_inicio, data_fim, cargo_idelo
            FROM validade
         """)

        validades = [
            {
                "idelo": row[0],
                "data_inicio": row[1],
                "data_fim": row[2],
                "cargo_idelo": row[3]
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
                cargo_idelo = %s
            WHERE idelo = %s
            """,
            (
                validade.data_inicio,
                validade.data_fim,
                validade.cargo_idelo,
                validade.idelo
            )
        )

        self.connection.commit()
        cursor.close()
