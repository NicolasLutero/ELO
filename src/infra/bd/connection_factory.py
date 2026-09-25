from pathlib import Path
import psycopg2, json


class ConnectionFactory:
    @staticmethod
    def get_connection():
        config = ConnectionFactory.carregar_configuracao()
        return psycopg2.connect(**config)

    @staticmethod
    def carregar_configuracao():
        caminho = Path(__file__).parent / "connection_config.json"
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
