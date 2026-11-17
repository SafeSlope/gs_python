"""
Perfil MORADOR: ver alerta, reportar ponto de risco e acompanhar protocolo.
"""

from config import STATUS_RELATO, TIPOS_RELATO
from dados import agora, gerar_protocolo, salvar_dados
from entradas import ler_inteiro, ler_texto
from regras import acao_recomendada, avaliar_area
from telas import escolher_area


def ver_alerta(dados):
    print("\n--- Alerta da minha área ---")
    area = escolher_area(dados)
    if area is None:
        return
    nivel, pontuacao, leitura = avaliar_area(dados, area)
    if nivel is None:
        print("Ainda não há leituras do sensor para esta área.")
        return
    print(f"\nÁrea: {area['nome']} ({area['bairro']})")
    print(f"Última leitura: {leitura['data']} | chuva {leitura['chuva_mm_h']:.1f} mm/h | "
          f"nível {leitura['nivel_mm']:.1f} mm")
    print(f"RISCO: {nivel} (pontuação {pontuacao})")
    print(f"O que fazer: {acao_recomendada(nivel, area['tipo'])}")


def reportar_risco(dados):
    print("\n--- Reportar ponto de risco ---")
    area = escolher_area(dados)
    if area is None:
        return

    print("\nO que você viu?")
    for numero, tipo in enumerate(TIPOS_RELATO, start=1):
        print(f"{numero} - {tipo}")
    opcao = ler_inteiro("Escolha: ", 1, len(TIPOS_RELATO))

    relato = {
        "protocolo": gerar_protocolo(dados),
        "area_id": area["id"],
        "tipo": TIPOS_RELATO[opcao - 1],
        "local": ler_texto("Onde fica? (rua, número ou referência): ", 3),
        "descricao": ler_texto("Descreva o que está acontecendo: ", 5),
        "gravidade": ler_inteiro("Gravidade de 1 (leve) a 5 (muito grave): ", 1, 5),
        "status": STATUS_RELATO[0],
        "criado_em": agora(),
        "historico": [],
    }
    relato["historico"].append(
        {"data": relato["criado_em"], "status": relato["status"], "obs": "Relato recebido."})
    dados["relatos"].append(relato)
    salvar_dados(dados)

    print(f"\nRelato registrado! Guarde seu protocolo: {relato['protocolo']}")
    if relato["gravidade"] >= 4:
        print("Como a gravidade é alta, o relato entra no topo da fila da Defesa Civil.")
        print("Se houver perigo agora, ligue 199.")


def acompanhar_protocolo(dados):
    print("\n--- Acompanhar protocolo ---")
    codigo = ler_texto("Digite o protocolo (ex.: SS-2026-0001): ", 4).upper()
    for relato in dados["relatos"]:
        if relato["protocolo"] == codigo:
            print(f"\nProtocolo {codigo} | {relato['tipo']}")
            print(f"Local: {relato['local']} | gravidade {relato['gravidade']}")
            print(f"Status atual: {relato['status']}")
            print("Andamento:")
            for passo in relato["historico"]:
                print(f"  {passo['data']} | {passo['status']} | {passo['obs']}")
            return
    print("Protocolo não encontrado. Confira o código e tente de novo.")


def menu_morador(dados):
    while True:
        print("\n=== MORADOR ===")
        print("1 - Ver alerta da minha área")
        print("2 - Reportar ponto de risco")
        print("3 - Acompanhar um protocolo")
        print("0 - Voltar")
        match input("Escolha: ").strip():
            case "1":
                ver_alerta(dados)
            case "2":
                reportar_risco(dados)
            case "3":
                acompanhar_protocolo(dados)
            case "0":
                return
            case _:
                print("Opção inválida.")