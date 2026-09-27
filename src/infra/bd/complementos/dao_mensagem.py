

class MensagemDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, texto, data_envio, canal_idelo, usuario_idelo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO mensagem (texto, data_envio, canal_idelo, usuario_idelo)
            VALUES (%s, %s, %s, %s)
            RETURNING idelo
            """,
            (texto, data_envio, canal_idelo, usuario_idelo)
        )
        idelo = cursor.fetchone()[0]
        self.connection.commit()
        cursor.close()

        return {
            "idelo": idelo,
            "texto": texto,
            "data_envio": data_envio,
            "canal_idelo": canal_idelo,
            "usuario_idelo": usuario_idelo}

    def get_by_idelo(self, idelo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT idelo, texto, data_envio, canal_idelo, usuario_idelo
            FROM mensagem
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
            "texto": row[1],
            "data_envio": row[2],
            "canal_idelo": row[3],
            "usuario_idelo": row[4]
        }

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT idelo, texto, data_envio, canal_idelo, usuario_idelo
            FROM mensagem
        """)

        mensagens = [
            {
                "idelo": row[0],
                "texto": row[1],
                "data_envio": row[2],
                "canal_idelo": row[3],
                "usuario_idelo": row[4]
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
                canal_idelo = %s,
                usuario_idelo = %s
            WHERE idelo = %s
            """,
            (
                mensagem.texto,
                mensagem.data_envio,
                mensagem.canal_idelo,
                mensagem.usuario_idelo,
                mensagem.idelo
            )
        )

        self.connection.commit()
        cursor.close()