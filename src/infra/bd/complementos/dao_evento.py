

class EventoDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, nome, descricao, data_evento, local, gremio_id, organizador_idelo, cargo_adm_idelo=None):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO evento (nome, descricao, data_evento, local, gremio_id, organizador_idelo, cargo_adm_idelo)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING idelo
            """,
            (nome, descricao, data_evento, local, gremio_id, organizador_idelo, cargo_adm_idelo)
        )

        idelo = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return {
            "idelo": idelo,
            "nome": nome,
            "descricao": descricao,
            "data_evento": data_evento,
            "local": local,
            "gremio_id": gremio_id,
            "organizador_idelo": organizador_idelo,
            "cargo_adm_idelo": cargo_adm_idelo}

    def get_by_id(self, idelo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT idelo, nome, descricao, data_evento, local, gremio_id, organizador_idelo, cargo_adm_idelo
            FROM evento
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
            "nome": row[1],
            "descricao": row[2],
            "data_evento": row[3],
            "local": row[4],
            "gremio_id": row[5],
            "organizador_idelo": row[6],
            "cargo_adm_idelo": row[7]
        }

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT idelo, nome, descricao, data_evento, local, gremio_id, organizador_idelo, cargo_adm_idelo
            FROM evento
        """)

        eventos = [
            {
                "idelo": row[0],
                "nome": row[1],
                "descricao": row[2],
                "data_evento": row[3],
                "local": row[4],
                "gremio_id": row[5],
                "organizador_idelo": row[6],
                "cargo_adm_idelo": row[7]
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
                gremio_id = %s,
                organizador_idelo = %s,
                cargo_adm_idelo = %s
            WHERE idelo = %s
            """,
            (
                evento.nome,
                evento.descricao,
                evento.data_evento,
                evento.local,
                evento.gremio_id,
                evento.organizador_idelo,
                evento.cargo_adm_idelo,
                evento.idelo
            )
        )
        self.connection.commit()
        cursor.close()

    def create_permissoes(self, evento_idelo, att_per):
        cursor = self.connection.cursor()

        columns = ["evento_idelo"] + list(att_per.keys())
        values = [evento_idelo] + list(att_per.values())

        placeholders = ", ".join(["%s"] * len(values))
        columns_sql = ", ".join(columns)

        cursor.execute(
            f"""
            INSERT INTO evento_permissoes ({columns_sql})
            VALUES ({placeholders})
            """,
            values
        )

        self.connection.commit()
        cursor.close()