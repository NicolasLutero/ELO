

class ComunicadoDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, titulo, conteudo, data_publicacao, gremio_id, autor_idelo, cargo_adm_idelo=None):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO comunicado (titulo, conteudo, data_publicacao, gremio_id, autor_idelo, cargo_adm_idelo)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING idelo
            """,
            (titulo, conteudo, data_publicacao, gremio_id, autor_idelo, cargo_adm_idelo)
        )

        idelo = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return {
            "idelo": idelo,
            "titulo": titulo,
            "conteudo": conteudo,
            "data_publicacao": data_publicacao,
            "gremio_id": gremio_id,
            "autor_idelo": autor_idelo,
            "cargo_adm_idelo": cargo_adm_idelo}

    def get_by_id(self, idelo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT idelo, titulo, conteudo, data_publicacao, gremio_id, autor_idelo, cargo_adm_idelo
            FROM comunicado
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
            "conteudo": row[2],
            "data_publicacao": row[3],
            "gremio_id": row[4],
            "autor_idelo": row[5],
            "cargo_adm_idelo": row[6]
        }

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT idelo, titulo, conteudo, data_publicacao, gremio_id, autor_idelo, cargo_adm_idelo
            FROM comunicado
        """)

        comunicados = [
            {
                "idelo": row[0],
                "titulo": row[1],
                "conteudo": row[2],
                "data_publicacao": row[3],
                "gremio_id": row[4],
                "autor_idelo": row[5],
                "cargo_adm_idelo": row[6]
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
                gremio_id = %s,
                autor_idelo = %s,
                cargo_adm_idelo = %s
            WHERE idelo = %s
            """,
            (
                comunicado.titulo,
                comunicado.conteudo,
                comunicado.data_publicacao,
                comunicado.gremio_id,
                comunicado.autor_idelo,
                comunicado.cargo_adm_idelo,
                comunicado.idelo
            )
        )

        self.connection.commit()
        cursor.close()

    def create_permissoes(self, comunicado_idelo, att_per):
        cursor = self.connection.cursor()

        columns = ["comunicado_idelo"] + list(att_per.keys())
        values = [comunicado_idelo] + list(att_per.values())

        placeholders = ", ".join(["%s"] * len(values))
        columns_sql = ", ".join(columns)

        cursor.execute(
            f"""
            INSERT INTO comunicado_permissoes ({columns_sql})
            VALUES ({placeholders})
            """,
            values
        )

        self.connection.commit()
        cursor.close()