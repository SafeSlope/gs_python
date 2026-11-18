"""
Simulação de tempestade (modelo da disciplina de Matemática).

chuva r(t) = -2t² + 12t (mm/h); escoamento constante E (mm/h);
acúmulo h(t) = integral de (r(t) - E) dt = -(2/3)t³ + 6t² - E·t
"""

from config import DURACAO_TEMPESTADE_H
from entradas import ler_numero


def intensidade_chuva(t):
    """r(t) = -2t² + 12t, em mm/h."""
    return -2 * t**2 + 12 * t


def nivel_acumulado(t, escoamento):
    """h(t) = -(2/3)t³ + 6t² - E·t, em mm."""
    return -(2 / 3) * t**3 + 6 * t**2 - escoamento * t


def simular_tempestade(escoamento, limite):
    """Retorna (tabela, t_critico). t_critico é None se o limite nunca é atingido."""
    t_critico = None
    t = 0.0
    while t <= DURACAO_TEMPESTADE_H:
        if nivel_acumulado(t, escoamento) >= limite:
            t_critico = round(t, 2)
            break
        t += 0.01

    tabela = []
    for meia_hora in range(DURACAO_TEMPESTADE_H * 2 + 1):
        hora = meia_hora / 2
        # nível negativo não existe na prática: a água já escoou
        nivel = max(0.0, nivel_acumulado(hora, escoamento))
        tabela.append((hora, intensidade_chuva(hora), nivel))
    return tabela, t_critico


def simular():
    print("\n--- Simulação de tempestade (modelo de Matemática) ---")
    print("Chuva: r(t) = -2t² + 12t mm/h, durante 6 horas.")
    escoamento = ler_numero("Capacidade de escoamento em mm/h (ex.: 8): ", 0, 50)
    limite = ler_numero("Limite de transbordamento em mm (ex.: 10): ", 1, 500)

    tabela, t_critico = simular_tempestade(escoamento, limite)
    print(f"\n{'Hora':>5} | {'Chuva (mm/h)':>12} | {'Nível (mm)':>10}")
    for hora, chuva, nivel in tabela:
        print(f"{hora:>5.1f} | {chuva:>12.1f} | {nivel:>10.1f}")

    if t_critico is not None:
        print(f"\nALERTA CRÍTICO: o limite de {limite:.1f} mm será atingido em {t_critico:.2f} h.")
    else:
        print(f"\nSITUAÇÃO SEGURA: o limite de {limite:.1f} mm não é atingido.")