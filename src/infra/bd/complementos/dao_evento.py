

class EventoDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, nome, descricao, data_evento, local, gremio_id):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO evento (nome, descricao, data_evento, local, gremio_id)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id_elo
            """,
            (nome, descricao, data_evento, local, gremio_id)
        )

        id_elo = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return {
            "id_elo": id_elo,
            "nome": nome,
            "descricao": descricao,
            "data_evento": data_evento,
            "local": local,
            "gremio_id": gremio_id}

    def get_by_id(self, id_elo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT id_elo, nome, descricao, data_evento, local, gremio_id
            FROM evento
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
            "descricao": row[2],
            "data_evento": row[3],
            "local": row[4],
            "gremio_id": row[5]
        }

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT id_elo, nome, descricao, data_evento, local, gremio_id
            FROM evento
        """)

        eventos = [
            {
                "id_elo": row[0],
                "nome": row[1],
                "descricao": row[2],
                "data_evento": row[3],
                "local": row[4],
                "gremio_id": row[5]
            }
            for row in cursor.fetchall()
        ]

        cursor.close()
        return eventos

    def update(self, evento):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            UPDATE evento
            SET nome = %s,
                descricao = %s,
                data_evento = %s,
                local = %s,
                gremio_id = %s
            WHERE id_elo = %s
            """,
            (
                evento.nome,
                evento.descricao,
                evento.data_evento,
                evento.local,
                evento.gremio_id,
                evento.id_elo
            )
        )
        self.connection.commit()
        cursor.close()