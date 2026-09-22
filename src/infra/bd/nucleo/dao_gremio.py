

class GremioDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, nome, instituicao, etapa_ensino, legitimado=False):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO gremio (nome, instituicao, etapa_ensino, legitimado)
            VALUES (%s, %s, %s, %s)
            RETURNING id
            """,
            (nome, instituicao, etapa_ensino, legitimado)
        )

        id = cursor.fetchone()[0]

        self.connection.commit()
        cursor.close()

        return {"id": id,
                "nome": nome,
                "isntituicao": instituicao,
                "etapa_ensino": etapa_ensino,
                "legitimidade": legitimado}

    def get_by_id(self, id):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT id, nome, instituicao, etapa_ensino, legitimado
            FROM gremio
            WHERE id = %s
            """,
            (id,)
        )

        row = cursor.fetchone()
        cursor.close()

        if row is None:
            return None

        return {
            "id": row[0],
            "nome": row[1],
            "instituicao": row[2],
            "etapa_ensino": row[3],
            "legitimado": row[4],
        }

    def get_all(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT id, nome, instituicao, etapa_ensino, legitimado
            FROM gremio
        """)

        gremios = [
            {
                "id": row[0],
                "nome": row[1],
                "instituicao": row[2],
                "etapa_ensino": row[3],
                "legitimado": row[4],
            }
            for row in cursor.fetchall()
        ]

        cursor.close()
        return gremios

    def update(self, gremio):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            UPDATE gremio
            SET nome = %s,
                instituicao = %s,
                etapa_ensino = %s,
                legitimado = %s
            WHERE id = %s
            """,
            (
                gremio.nome,
                gremio.instituicao,
                gremio.etapa_ensino,
                gremio.legitimado,
                gremio.id
            )
        )

        self.connection.commit()
        cursor.close()
