

class MensagemDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, texto, data_envio, canal_id, usuario_id):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO mensagem (texto, data_envio, canal_id, usuario_id)
            VALUES (%s, %s, %s, %s)
            RETURNING id_elo
            """,
            (texto, data_envio, canal_id, usuario_id)
        )
        id_elo = cursor.fetchone()[0]
        self.connection.commit()
        cursor.close()

        return {
            "id_elo": id_elo,
            "texto": texto,
            "data_envio": data_envio,
            "canal_id": canal_id,
            "usuario_id": usuario_id}

    def get_by_id(self, id_elo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT id_elo, texto, data_envio, canal_id, usuario_id
            FROM mensagem
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
            "texto": row[1],
            "data_envio": row[2],
            "canal_id": row[3],
            "usuario_id": row[4]
        }

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT id_elo, texto, data_envio, canal_id, usuario_id
            FROM mensagem
        """)

        mensagens = [
            {
                "id_elo": row[0],
                "texto": row[1],
                "data_envio": row[2],
                "canal_id": row[3],
                "usuario_id": row[4]
            }
            for row in cursor.fetchall()
        ]

        cursor.close()
        return mensagens

    def update(self, mensagem):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            UPDATE mensagem
            SET texto = %s,
                data_envio = %s,
                canal_id = %s,
                usuario_id = %s
            WHERE id_elo = %s
            """,
            (
                mensagem.texto,
                mensagem.data_envio,
                mensagem.canal_id,
                mensagem.usuario_id,
                mensagem.id_elo
            )
        )

        self.connection.commit()
        cursor.close()