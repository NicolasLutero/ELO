

class ComunicadoDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, titulo, conteudo, data_publicacao, gremio_id):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO comunicado (titulo, conteudo, data_publicacao, gremio_id)
            VALUES (%s, %s, %s, %s)
            RETURNING id_elo
            """,
            (titulo, conteudo, data_publicacao, gremio_id)
        )

        id_elo = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return {
            "id_elo": id_elo,
            "titulo": titulo,
            "conteudo": conteudo,
            "data_publicacao": data_publicacao,
            "gremio_id": gremio_id}

    def get_by_id(self, id_elo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT id_elo, titulo, conteudo, data_publicacao, gremio_id
            FROM comunicado
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
            "conteudo": row[2],
            "data_publicacao": row[3],
            "gremio_id": row[4]
        }

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT id_elo, titulo, conteudo, data_publicacao, gremio_id
            FROM comunicado
        """)

        comunicados = [
            {
                "id_elo": row[0],
                "titulo": row[1],
                "conteudo": row[2],
                "data_publicacao": row[3],
                "gremio_id": row[4]
            }
            for row in cursor.fetchall()
        ]

        cursor.close()
        return comunicados

    def update(self, comunicado):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            UPDATE comunicado
            SET titulo = %s,
                conteudo = %s,
                data_publicacao = %s,
                gremio_id = %s
            WHERE id_elo = %s
            """,
            (
                comunicado.titulo,
                comunicado.conteudo,
                comunicado.data_publicacao,
                comunicado.gremio_id,
                comunicado.id_elo
            )
        )

        self.connection.commit()
        cursor.close()