"""
Perfil DEFESA CIVIL: áreas, leituras, prioridades, status e impacto.
"""

from config import STATUS_RELATO
from dados import agora, buscar_por_id, salvar_dados
from entradas import ler_numero, ler_texto, ler_tipo_area
from regras import (acao_recomendada, avaliar_area, calcular_prioridade,
                    chave_prioridade, contar_leituras_criticas, horas_entre)
from telas import escolher_area


def cadastrar_area(dados):
    print("\n--- Cadastrar área monitorada ---")
    novo_id = max([a["id"] for a in dados["areas"]], default=0) + 1
    area = {
        "id": novo_id,
        "nome": ler_texto("Nome da área (ex.: Morro do Alto): ", 3),
        "bairro": ler_texto("Bairro: ", 3),
        "tipo": ler_tipo_area(),
        "limite_mm": ler_numero("Limite de transbordamento em mm (1 a 500): ", 1, 500),
    }
    dados["areas"].append(area)
    salvar_dados(dados)
    print(f"Área #{novo_id} cadastrada.")


def registrar_leitura(dados):
    print("\n--- Registrar leitura do sensor ---")
    area = escolher_area(dados)
    if area is None:
        return
    leitura = {
        "area_id": area["id"],
        "data": agora(),
        "chuva_mm_h": ler_numero("Intensidade da chuva em mm/h (0 a 200): ", 0, 200),
        "nivel_mm": ler_numero("Nível de água em mm (0 a 1000): ", 0, 1000),
        "umidade_pct": 0.0,
    }
    if area["tipo"] == "encosta":
        leitura["umidade_pct"] = ler_numero("Umidade do solo em % (0 a 100): ", 0, 100)

    dados["leituras"].append(leitura)
    salvar_dados(dados)

    nivel, pontuacao, _ = avaliar_area(dados, area)
    print(f"\nLeitura salva. RISCO: {nivel} (pontuação {pontuacao})")
    print(f"Alerta para os moradores: {acao_recomendada(nivel, area['tipo'])}")


def painel_prioridades(dados):
    print("\n--- Painel de prioridades (relatos abertos) ---")
    fila = []  # lista de tuplas (prioridade, relato, area)
    for relato in dados["relatos"]:
        if relato["status"] == "RESOLVIDO":
            continue
        area = buscar_por_id(dados["areas"], relato["area_id"])
        _, pontuacao, _ = avaliar_area(dados, area)
        fila.append((calcular_prioridade(relato, pontuacao), relato, area))

    if not fila:
        print("Nenhum relato aberto. Tudo em dia!")
        return

    fila.sort(key=chave_prioridade, reverse=True)
    for posicao, (prioridade, relato, area) in enumerate(fila, start=1):
        print(f"{posicao}º | {relato['protocolo']} | prioridade {prioridade:.0f} | "
              f"grav. {relato['gravidade']} | {relato['status']}")
        print(f"     {relato['tipo']} - {relato['local']} ({area['bairro']})")


def atualizar_status(dados):
    print("\n--- Atualizar status de um relato ---")
    codigo = ler_texto("Protocolo: ", 4).upper()
    for relato in dados["relatos"]:
        if relato["protocolo"] != codigo:
            continue
        atual = STATUS_RELATO.index(relato["status"])
        if atual == len(STATUS_RELATO) - 1:
            print("Este relato já foi resolvido.")
            return
        proximo = STATUS_RELATO[atual + 1]
        print(f"Status atual: {relato['status']} -> próximo: {proximo}")
        obs = ler_texto("Observação para o morador (ficará visível no protocolo): ", 3)
        relato["status"] = proximo
        relato["historico"].append({"data": agora(), "status": proximo, "obs": obs})
        salvar_dados(dados)
        print("Status atualizado. O morador já pode ver a mudança.")
        return
    print("Protocolo não encontrado.")


def relatorio_impacto(dados):
    print("\n--- Relatório de impacto ---")
    total = len(dados["relatos"])
    if total == 0:
        print("Ainda não há relatos para calcular indicadores.")
        return

    resolvidos = 0
    horas_resolucao = []
    for relato in dados["relatos"]:
        if relato["status"] == "RESOLVIDO":
            resolvidos += 1
            horas = horas_entre(relato["criado_em"], relato["historico"][-1]["data"])
            if horas is not None:
                horas_resolucao.append(horas)

    alertas_criticos = contar_leituras_criticas(dados)

    print(f"Áreas monitoradas: {len(dados['areas'])}")
    print(f"Leituras registradas: {len(dados['leituras'])} (críticas: {alertas_criticos})")
    print(f"Relatos de moradores: {total}")
    print(f"Relatos resolvidos: {resolvidos} ({resolvidos / total * 100:.0f}%)")
    if horas_resolucao:
        media = sum(horas_resolucao) / len(horas_resolucao)
        print(f"Tempo médio de resolução: {media:.1f} h")
    else:
        print("Tempo médio de resolução: ainda sem relatos resolvidos.")


def menu_defesa_civil(dados):
    while True:
        print("\n=== DEFESA CIVIL ===")
        print("1 - Cadastrar área monitorada")
        print("2 - Registrar leitura do sensor")
        print("3 - Painel de prioridades")
        print("4 - Atualizar status de um relato")
        print("5 - Relatório de impacto")
        print("0 - Voltar")
        match input("Escolha: ").strip():
            case "1":
                cadastrar_area(dados)
            case "2":
                registrar_leitura(dados)
            case "3":
                painel_prioridades(dados)
            case "4":
                atualizar_status(dados)
            case "5":
                relatorio_impacto(dados)
            case "0":
                return
            case _:
                print("Opção inválida.")