import random
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt  # Biblioteca para gráficos

# ================================
# Lista de módulos com atributos fixos
# ================================
modulos = [
    {"nome": "Habitação 1", "massa": 28, "energia": 20, "combustivel": 65, "prioridade": "Alta"},
    {"nome": "Energia Solar", "massa": 22, "energia": 25, "combustivel": 40, "prioridade": "Alta"},
    {"nome": "Laboratório Científico", "massa": 30, "energia": 18, "combustivel": 25, "prioridade": "Média"},
    {"nome": "Logística 1", "massa": 35, "energia": 15, "combustivel": 70, "prioridade": "Média"},
    {"nome": "Suporte Médico", "massa": 26, "energia": 22, "combustivel": 55, "prioridade": "Alta"},
    {"nome": "Habitação 2", "massa": 32, "energia": 20, "combustivel": 18, "prioridade": "Alta"},
    {"nome": "Rover de Exploração", "massa": 12, "energia": 10, "combustivel": 80, "prioridade": "Média"},
    {"nome": "Módulo de Mineração", "massa": 40, "energia": 25, "combustivel": 30, "prioridade": "Baixa"},
    {"nome": "Logística 2", "massa": 34, "energia": 15, "combustivel": 65, "prioridade": "Média"},
    {"nome": "Habitação 3", "massa": 29, "energia": 20, "combustivel": 50, "prioridade": "Alta"},
    {"nome": "Estação de Comunicações", "massa": 20, "energia": 12, "combustivel": 22, "prioridade": "Alta"},
    {"nome": "Armazém de Suprimentos", "massa": 33, "energia": 18, "combustivel": 75, "prioridade": "Média"},
    {"nome": "Módulo de Produção Local", "massa": 38, "energia": 25, "combustivel": 28, "prioridade": "Baixa"},
    {"nome": "Habitação 4", "massa": 31, "energia": 20, "combustivel": 62, "prioridade": "Alta"},
    {"nome": "Laboratório Biológico", "massa": 27, "energia": 18, "combustivel": 19, "prioridade": "Média"},
]

# Lista para armazenar o histórico
historico_pousos = []

# ================================
# Função: verificar_pouso
# ================================
def verificar_pouso(modulo):
# Ajuste de probabilidades para aumentar taxa de sucesso (~50%)
    sensores_ok = random.choices([True, False], weights=[0.7, 0.3])[0]
    area_livre = random.choices([True, False], weights=[0.7, 0.3])[0]
    clima = random.choices(["Estável", "Tempestade de poeira", "Vento forte"], weights=[0.6, 0.2, 0.2])[0]


    print(f"Sensores OK: {sensores_ok} | Área livre: {area_livre} | Clima: {clima} | Prioridade: {modulo['prioridade']}")

    if modulo["combustivel"] >= 30 and sensores_ok and area_livre and clima == "Estável":
        resultado = f"{modulo['nome']} → Pouso autorizado ✅"
    else:
        if modulo["prioridade"] == "Alta" and modulo["combustivel"] >= 20:
            resultado = f"{modulo['nome']} → Pouso autorizado ⚠️ (forçado pela prioridade)"
        else:
            resultado = f"{modulo['nome']} → Pouso negado ❌"

    momento = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    historico_pousos.append({
        "momento": momento,
        "modulo": modulo["nome"],
        "massa": modulo["massa"],
        "energia": modulo["energia"],
        "combustivel": modulo["combustivel"],
        "prioridade": modulo["prioridade"],
        "resultado": resultado
    })
    return resultado

# ================================
# Função: simular_pouso
# ================================
def simular_pouso():
    escolhido = random.choice(modulos)
    print("Situação sorteada:")
    print(f"Módulo: {escolhido['nome']}")
    print(f"Massa: {escolhido['massa']} t | Energia: {escolhido['energia']} kW | Combustível: {escolhido['combustivel']}%")
    print(verificar_pouso(escolhido))

# ================================
# Função: mostrar_historico
# ================================
def mostrar_historico():
    print("\n📜 Histórico de Pousos:")
    for registro in historico_pousos:
        print(f"{registro['momento']} | {registro['modulo']} → {registro['resultado']}")

# ================================
# Função: mostrar_estatisticas
# ================================
def mostrar_estatisticas():
    autorizados = sum(1 for r in historico_pousos if "✅" in r["resultado"])
    negados = sum(1 for r in historico_pousos if "❌" in r["resultado"])
    forçados = sum(1 for r in historico_pousos if "⚠️" in r["resultado"])

    print("\n📊 Estatísticas finais:")
    print(f"Pousos autorizados: {autorizados}")
    print(f"Pousos negados: {negados}")
    print(f"Pousos forçados pela prioridade: {forçados}")

    # Gráfico de barras
    plt.bar(["Autorizados", "Negados", "Forçados"], [autorizados, negados, forçados], color=["green", "red", "orange"])
    plt.title("Estatísticas de Pousos")
    plt.xlabel("Categoria")
    plt.ylabel("Quantidade")
    plt.show()

    # Gráfico de pizza
    plt.pie([autorizados, negados, forçados], labels=["Autorizados", "Negados", "Forçados"], autopct="%1.1f%%", colors=["green", "red", "orange"])
    plt.title("Distribuição de Pousos")
    plt.show()

# ================================
# Função: exportar_csv
# ================================
def exportar_csv(nome_arquivo="historico_pousos.csv"):
    arquivo_existe = os.path.isfile(nome_arquivo)
    with open(nome_arquivo, mode="a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        if not arquivo_existe:
            escritor.writerow(["Momento", "Modulo", "Massa", "Energia", "Combustivel", "Prioridade", "Resultado"])
        for registro in historico_pousos:
            escritor.writerow([
                registro["momento"],
                registro["modulo"],
                registro["massa"],
                registro["energia"],
                registro["combustivel"],
                registro["prioridade"],
                registro["resultado"]
            ])
    print(f"\n📂 Histórico adicionado em {nome_arquivo}")

# ================================
# Entrada do usuário
# ================================
while True:
    try:
        qtd = int(input("Digite o número de simulações (1 a 15): "))
        if 1 <= qtd <= 15:
            break
        else:
            print("Valor inválido! Escolha um número entre 1 e 15.")
    except ValueError:
        print("Entrada inválida! Digite apenas números.")

# Executa simulações
for _ in range(qtd):
    simular_pouso()

# Mostra histórico e estatísticas (com gráficos)
mostrar_historico()
mostrar_estatisticas()

# Exporta para CSV
exportar_csv()
