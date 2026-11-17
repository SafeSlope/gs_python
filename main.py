from dados import carregar_dados
from defesa_civil import menu_defesa_civil
from morador import menu_morador
from simulacao import simular


def main():
    dados = carregar_dados()
    while True:
        print("\n=== SAFESLOPE - Safe slopes, peaceful lives ===")
        print("1 - Sou morador")
        print("2 - Sou da Defesa Civil")
        print("3 - Simular tempestade")
        print("0 - Sair")
        match input("Escolha: ").strip():
            case "1":
                menu_morador(dados)
            case "2":
                menu_defesa_civil(dados)
            case "3":
                simular()
            case "0":
                print("Encerrando. Dados salvos. Fique em segurança!")
                break
            case _:
                print("Opção inválida.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C ou fim da entrada: os dados já foram salvos a cada operação
        print("\nPrograma encerrado. Dados já salvos.")