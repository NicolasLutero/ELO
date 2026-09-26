

class CanalDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, nome, descricao, gremio_id, criador_idelo, cargo_adm_idelo=None):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO canal (nome, descricao, gremio_id, criador_idelo, cargo_adm_idelo)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING idelo
            """,
            (nome, descricao, gremio_id, criador_idelo, cargo_adm_idelo)
        )

        idelo = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return {
            "idelo": idelo,
            "nome": nome,
            "descricao": descricao,
            "gremio_id": gremio_id,
            "criador_idelo": criador_idelo,
            "cargo_adm_idelo": cargo_adm_idelo}

    def get_by_id(self, idelo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT idelo, nome, descricao, gremio_id, criador_idelo, cargo_adm_idelo
            FROM canal
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
            "gremio_id": row[3],
            "criador_idelo": row[4],
            "cargo_adm_idelo": row[5]
        }

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT idelo, nome, descricao, gremio_id, criador_idelo, cargo_adm_idelo
            FROM canal
        """)

        canais = [
            {
                "idelo": row[0],
                "nome": row[1],
                "descricao": row[2],
                "gremio_id": row[3],
                "criador_idelo": row[4],
                "cargo_adm_idelo": row[5]
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
                gremio_id = %s,
                criador_idelo = %s,
                cargo_adm_idelo = %s
            WHERE idelo = %s
            """,
            (
                canal.nome,
                canal.descricao,
                canal.gremio_id,
                canal.criador_idelo,
                canal.cargo_adm_idelo,
                canal.idelo
            )
        )

        self.connection.commit()
        cursor.close()

    def create_permissoes(self, canal_idelo, att_per):
        cursor = self.connection.cursor()

        columns = ["canal_idelo"] + list(att_per.keys())
        values = [canal_idelo] + list(att_per.values())

        placeholders = ", ".join(["%s"] * len(values))
        columns_sql = ", ".join(columns)

        cursor.execute(
            f"""
            INSERT INTO canal_permissoes ({columns_sql})
            VALUES ({placeholders})
            """,
            values
        )

        self.connection.commit()
        cursor.close()