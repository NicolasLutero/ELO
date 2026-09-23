

class EnqueteDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, titulo, descricao, data_criacao, data_encerramento, gremio_id):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO enquete (titulo, descricao, data_criacao, data_encerramento, gremio_id)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id_elo
            """,
            (titulo, descricao, data_criacao, data_encerramento, gremio_id)
        )

        id_elo = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return {
            "id_elo": id_elo,
            "titulo": titulo,
            "descricao": descricao,
            "data_criacao": data_criacao,
            "data_encerramento": data_encerramento,
            "gremio_id": gremio_id}

    def get_by_id(self, id_elo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT id_elo, titulo, descricao, data_criacao, data_encerramento, gremio_id
            FROM enquete
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
            "titulo": row[1],
            "descricao": row[2],
            "data_criacao": row[3],
            "data_encerramento": row[4],
            "gremio_id": row[5]
        }

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT id_elo, titulo, descricao, data_criacao, data_encerramento, gremio_id
            FROM enquete
        """)

        enquetes = [
            {
                "id_elo": row[0],
                "titulo": row[1],
                "descricao": row[2],
                "data_criacao": row[3],
                "data_encerramento": row[4],
                "gremio_id": row[5]
            }
            for row in cursor.fetchall()
        ]

        cursor.close()
        return enquetes

    def update(self, enquete):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            UPDATE enquete
            SET titulo = %s,
                descricao = %s,
                data_criacao = %s,
                data_encerramento = %s,
                gremio_id = %s
            WHERE id_elo = %s
            """,
            (
                enquete.titulo,
                enquete.descricao,
                enquete.data_criacao,
                enquete.data_encerramento,
                enquete.gremio_id,
                enquete.id_elo
            )
        )
        self.connection.commit()
        cursor.close()