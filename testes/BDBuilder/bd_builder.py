from pathlib import Path

from infra.bd.connection_factory import ConnectionFactory


BASE_PATH = Path(
    r"C:\Users\Nicol\OneDrive\Desktop\Projetos Python\IFSP\ELO\testes\BDBuilder"
)

ARQUIVOS_SQL = [
    BASE_PATH / "BDELO_CLEAR.sql",
    BASE_PATH / "BDELO_CREATE_NUCLEO.sql",
    BASE_PATH / "BDELO_CREATE.sql",
    BASE_PATH / "BDELO_INSERT_NUCLEO.sql",
    BASE_PATH / "BDELO_INSERT.sql",
    BASE_PATH / "BDELO_RESTRICT_NUCLEO.sql",
    BASE_PATH / "BDELO_RESTRICT.sql"
]


def executar_script(caminho: Path):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        script = arquivo.read()

    connection = ConnectionFactory.get_connection()

    try:
        cursor = connection.cursor()

        comandos = script.split(";")

        for comando in comandos:
            comando = comando.strip()

            if not comando:
                continue

            cursor.execute(comando)

        connection.commit()

    finally:
        cursor.close()
        connection.close()


def main():
    try:
        for arquivo in ARQUIVOS_SQL:
            print(f"Executando: {arquivo}")
            executar_script(arquivo)
            print(f"Concluído: {arquivo}")

        print("\nBanco de dados criado com sucesso!")

    except Exception as e:
        print("\nErro ao construir o banco de dados:")
        print(e)


if __name__ == "__main__":
    main()
