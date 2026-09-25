

class GremioDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, nome, instituicao, etapa_ensino, legitimado=False):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO gremio (nome, instituicao, etapa_ensino, legitimado)
            VALUES (%s, %s, %s, %s)
            RETURNING id_elo
            """,
            (nome, instituicao, etapa_ensino, legitimado)
        )

        id_elo = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return {"id_elo": id_elo,
                "nome": nome,
                "instituicao": instituicao,
                "etapa_ensino": etapa_ensino,
                "legitimado": legitimado}

    def get_by_id(self, id_elo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT id_elo, nome, instituicao, etapa_ensino, legitimado
            FROM gremio
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
            "instituicao": row[2],
            "etapa_ensino": row[3],
            "legitimado": row[4],
        }

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT id_elo, nome, instituicao, etapa_ensino, legitimado
            FROM gremio
        """)

        gremios = [
            {
                "id_elo": row[0],
                "nome": row[1],
                "instituicao": row[2],
                "etapa_ensino": row[3],
                "legitimado": row[4],
            }
            for row in cursor.fetchall()
        ]

        cursor.close()
        return gremios

    def get_by_inst_etapa(self, instituicao_id_elo, etapa):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT id_elo, nome, instituicao, etapa_ensino, legitimado
            FROM gremio
            WHERE instituicao = %s
                AND etapa_ensino = %s
            """,
            (instituicao_id_elo, etapa)
        )

        row = cursor.fetchone()
        cursor.close()

        if row is None:
            return None

        return {
            "id_elo": row[0],
            "nome": row[1],
            "instituicao": row[2],
            "etapa_ensino": row[3],
            "legitimado": row[4],
        }

    def check_availability_inst_etapa(self, inst, etapa):
        cursor = self.connection.cursor()

        cursor.execute(
            f"""
                SELECT count(id_elo)
                FROM gremio
                WHERE instituicao_id = %s 
                    AND etapa_ensino = %s
            """,
            (inst, etapa)
        )

        row = cursor.fetchone()
        cursor.close()

        return row[0] == 0

    def update(self, gremio):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            UPDATE gremio
            SET nome = %s,
                instituicao = %s,
                etapa_ensino = %s,
                legitimado = %s
            WHERE id_elo = %s
            """,
            (
                gremio.nome,
                gremio.instituicao,
                gremio.etapa_ensino,
                gremio.legitimado,
                gremio.id_elo
            )
        )

        self.connection.commit()
        cursor.close()

    def create_permissoes(self, gremio_id_elo, att_per):
        cursor = self.connection.cursor()

        columns = ["gremio_id_elo"] + list(att_per.keys())
        values = [gremio_id_elo] + list(att_per.values())

        placeholders = ", ".join(["%s"] * len(values))
        columns_sql = ", ".join(columns)

        cursor.execute(
            f"""
            INSERT INTO gremio_permissoes ({columns_sql})
            VALUES ({placeholders})
            """,
            values
        )

        self.connection.commit()
        cursor.close()
