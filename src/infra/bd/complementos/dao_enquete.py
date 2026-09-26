

class EnqueteDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, titulo, descricao, data_criacao, data_encerramento, gremio_id, autor_idelo, cargo_adm_idelo=None):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO enquete (titulo, descricao, data_criacao, data_encerramento, gremio_id, autor_idelo, cargo_adm_idelo)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING idelo
            """,
            (titulo, descricao, data_criacao, data_encerramento, gremio_id, autor_idelo, cargo_adm_idelo)
        )

        idelo = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return {
            "idelo": idelo,
            "titulo": titulo,
            "descricao": descricao,
            "data_criacao": data_criacao,
            "data_encerramento": data_encerramento,
            "gremio_id": gremio_id,
            "autor_idelo": autor_idelo,
            "cargo_adm_idelo": cargo_adm_idelo}

    def get_by_id(self, idelo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT idelo, titulo, descricao, data_criacao, data_encerramento, gremio_id, autor_idelo, cargo_adm_idelo
            FROM enquete
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
            "titulo": row[1],
            "descricao": row[2],
            "data_criacao": row[3],
            "data_encerramento": row[4],
            "gremio_id": row[5],
            "autor_idelo": row[6],
            "cargo_adm_idelo": row[7]
        }

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT idelo, titulo, descricao, data_criacao, data_encerramento, gremio_id, autor_idelo, cargo_adm_idelo
            FROM enquete
        """)

        enquetes = [
            {
                "idelo": row[0],
                "titulo": row[1],
                "descricao": row[2],
                "data_criacao": row[3],
                "data_encerramento": row[4],
                "gremio_id": row[5],
                "autor_idelo": row[6],
                "cargo_adm_idelo": row[7]
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
                gremio_id = %s,
                autor_idelo = %s,
                cargo_adm_idelo = %s
            WHERE idelo = %s
            """,
            (
                enquete.titulo,
                enquete.descricao,
                enquete.data_criacao,
                enquete.data_encerramento,
                enquete.gremio_id,
                enquete.autor_idelo,
                enquete.cargo_adm_idelo,
                enquete.idelo
            )
        )
        self.connection.commit()
        cursor.close()

    def create_permissoes(self, enquete_idelo, att_per):
        cursor = self.connection.cursor()

        columns = ["enquete_idelo"] + list(att_per.keys())
        values = [enquete_idelo] + list(att_per.values())

        placeholders = ", ".join(["%s"] * len(values))
        columns_sql = ", ".join(columns)

        cursor.execute(
            f"""
            INSERT INTO enquete_permissoes ({columns_sql})
            VALUES ({placeholders})
            """,
            values
        )

        self.connection.commit()
        cursor.close()