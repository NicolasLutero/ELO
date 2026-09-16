import psycopg2, json


class ConnectionFactory:
    @staticmethod
    def get_connection():
        config = ConnectionFactory.carregar_configuracao()
        return psycopg2.connect(**config)

    @staticmethod
    def carregar_configuracao():
        with open("connection_config.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
