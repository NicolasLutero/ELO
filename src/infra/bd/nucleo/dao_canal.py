

class CanalDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, nome, descricao, gremio_id):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO canal (nome, descricao, gremio_id)
            VALUES (%s, %s, %s)
            RETURNING id_elo
            """,
            (nome, descricao, gremio_id)
        )

        id_elo = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return {
            "id_elo": id_elo,
            "nome": nome,
            "descricao": descricao,
            "gremio_id": gremio_id}

    def get_by_id(self, id_elo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT id_elo, nome, descricao, gremio_id
            FROM canal
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
            "gremio_id": row[3]
        }

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT id_elo, nome, descricao, gremio_id
            FROM canal
        """)

        canais = [
            {
                "id_elo": row[0],
                "nome": row[1],
                "descricao": row[2],
                "gremio_id": row[3]
            }
            for row in cursor.fetchall()
        ]

        cursor.close()
        return canais

    def update(self, canal):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            UPDATE canal
            SET nome = %s,
                descricao = %s,
                gremio_id = %s
            WHERE id_elo = %s
            """,
            (
                canal.nome,
                canal.descricao,
                canal.gremio_id,
                canal.id_elo
            )
        )

        self.connection.commit()
        cursor.close()