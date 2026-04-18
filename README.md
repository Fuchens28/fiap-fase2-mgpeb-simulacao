# 🚀 MGPEB — Modelo de Gerenciamento de Pousos em Estruturas Básicas

![Python](https://img.shields.io/badge/PYTHON-3.6+-3776AB?labelColor=0a0f1e&logo=python&logoColor=c5d8f0) ![Status](https://img.shields.io/badge/STATUS-SIMULAÇÃO_ATIVA-52be80?logo=startrek&labelColor=0a0f1e&logoColor=c5d8f0)

*Atividade Integradora · Fase 2 · Ciência da Computação, 2026 — FIAP*

🧑‍🚀 [Matheus Fuchelberguer | RM571321](https://www.linkedin.com/in/matheus-fuchelberguer-neves/) · [Julia Ramos | RM568988](https://www.linkedin.com/in/juliaramosguedes) · [Julio Joaquim | RM569113](https://github.com/jojigoats)

---

## 🛰 Resumo do Sistema

O **MGPEB — Modelo de Gerenciamento de Pousos em Estruturas Básicas** é um simulador em Python que avalia condições críticas para pouso de módulos em Marte.  
O sistema considera variáveis como **massa, energia, combustível, sensores, área livre e clima**, aplicando regras de decisão para autorizar, negar ou forçar o pouso conforme a prioridade do módulo.  

Cada tentativa gera um **histórico com data e hora**, exportado automaticamente para `.csv`, permitindo análise posterior.  
Ao final das simulações, o sistema apresenta **estatísticas consolidadas** e **gráficos visuais** (barras e pizza) que mostram a distribuição dos resultados.

---

## 🛰 Pipeline


1. **Módulo sorteado** — seleciona aleatoriamente um dos módulos disponíveis com seus atributos fixos.  
2. **Verificação de variáveis críticas** — sensores, área livre e clima são avaliados junto ao nível de combustível.  
3. **Regras de decisão** — aplicam a lógica: pouso autorizado, negado ou forçado pela prioridade.  
4. **Resultado** — cada tentativa gera uma saída imediata no console.  
5. **Registro no histórico** — salva data/hora, atributos do módulo e resultado.  
6. **Exportação CSV** — adiciona os registros ao arquivo `historico_pousos.csv`.  
7. **Estatísticas e Gráficos** — consolida os resultados e apresenta visualizações (barras e pizza).

---

## 🛰 Arquitetura

**Funções puras** — cada verificação é implementada como função independente, sem efeitos colaterais.  
**Imutabilidade** — os atributos dos módulos (massa, energia, combustível, prioridade) são fixos e não se alteram durante a simulação.  
**Estratégia fail-fast** — se qualquer condição crítica não é atendida, o pouso é negado imediatamente.  
**Registro contínuo** — cada tentativa é armazenada com data/hora, permitindo auditoria e análise posterior.  
**Análise estatística** — ao final, o sistema consolida os resultados e gera gráficos para interpretação visual.  

---

## 📡 Resultados

**Exemplo de saída no console:**

**Pouso autorizado:**
```
Situação sorteada:
Módulo: Habitação 1
Massa: 28 t | Energia: 20 kW | Combustível: 65%
Sensores OK: True | Área livre: True | Clima: Estável | Prioridade: Alta
Habitação 1 → Pouso autorizado ✅
```

**Pouso negado:**
```
Situação sorteada:
Módulo: Módulo de Mineração
Massa: 40 t | Energia: 25 kW | Combustível: 30%
Sensores OK: False | Área livre: True | Clima: Tempestade de poeira | Prioridade: Baixa
Módulo de Mineração → Pouso negado ❌
```

**Pouso forçado pela prioridade:**
```
Situação sorteada:
Módulo: Suporte Médico
Massa: 26 t | Energia: 22 kW | Combustível: 55%
Sensores OK: False | Área livre: False | Clima: Vento forte | Prioridade: Alta
Suporte Médico → Pouso autorizado ⚠️ (forçado pela prioridade)
```

**Exemplo de histórico em CSV (`historico_pousos.csv`):**

| Momento              | Modulo       | Massa | Energia | Combustivel | Prioridade | Resultado                          |
|----------------------|--------------|-------|---------|-------------|------------|------------------------------------|
| 18/04/2026 14:30:00 | Habitação 1 | 28    | 20      | 65          | Alta       | Habitação 1 → Pouso autorizado ✅ |
| 18/04/2026 14:30:05 | Energia Solar| 22    | 25      | 40          | Alta       | Energia Solar → Pouso negado ❌   |

**Exemplo de gráficos gerados:**

- 📊 **Gráfico de barras** (exemplo conceitual):
  ```
  Estatísticas de Pousos
  |
  |       ████
  | ████  ████
  | ████  ████  ████
  +------------------
    Autorizados Negados Forçados
  ```

- 🥧 **Gráfico de pizza** (exemplo conceitual):
  ```
  Distribuição de Pousos
  Autorizados: 50% ██████████
  Negados:     30% ███████
  Forçados:    20% ████
  ```

*(Os gráficos são exibidos automaticamente ao final da execução do programa usando matplotlib. Para capturas reais, execute o simulador e salve as imagens.)*

---

## 🚀 Como executar

**Pré-requisitos:**  
- Python 3.9 ou superior instalado  
- Biblioteca `matplotlib` instalada (`pip install matplotlib`)  

**Passo a passo:**

```bash
# Clonar o repositório
git clone https://github.com/Fuchens28/fiap-fase2-mgpeb-simulacao.git
cd fiap-fase2-mgpeb-simulacao

# Instalar dependências
pip install -r requirements.txt

# Executar o simulador
python mgpeb_simulacao.py

1. Informe o número de simulações desejadas.  
2. Acompanhe os resultados no console.  
3. Verifique o arquivo `historico_pousos.csv` gerado automaticamente.  
4. Analise os gráficos exibidos ao final da execução.  

> 💡 Dica: você pode abrir o CSV no Excel ou Google Sheets para explorar os dados em mais detalhes.

```
fiap-fase2-mgpeb-simulacao/
├── mgpeb_simulacao.py      ← código principal em Python
├── historico_pousos.csv    ← arquivo gerado automaticamente com os resultados
├── requirements.txt        ← dependências (ex.: matplotlib)
├── LICENSE                 ← licença do projeto (MIT)
└── README.md               ← documentação do projeto
```

## 🔭 Reflexão Crítica

O desenvolvimento do **MGPEB** vai além da prática técnica: ele traz reflexões sobre **ética, sustentabilidade e impacto social**.  

- **Ética**: o sistema simula decisões críticas em cenários de pouso, reforçando a importância de algoritmos transparentes e auditáveis. Em missões reais, decisões automatizadas devem sempre ser acompanhadas de supervisão humana para evitar riscos.
- **Sustentabilidade**:  ao trabalhar com simulações, reduzimos custos e impactos ambientais de testes físicos, mostrando como a tecnologia pode apoiar práticas mais sustentáveis.
- **Impacto social**: projetos como este incentivam o aprendizado colaborativo e a aplicação prática da ciência da computação em problemas complexos, preparando profissionais para lidar com desafios reais em exploração espacial e em outras áreas críticas.
- **Responsabilidade**: ao registrar cada tentativa e resultado, o sistema promove rastreabilidade e responsabilidade, valores essenciais em qualquer aplicação que envolva segurança e vidas humanas.

> O MGPEB não é apenas um exercício acadêmico, mas um exemplo de como a tecnologia pode ser usada de forma responsável, crítica e consciente.

## 🏁 Conclusão e Próximos Passos

O **MGPEB** demonstra como conceitos de programação funcional, análise estatística e simulação podem ser aplicados em cenários de alta complexidade, como pousos em Marte.  
Ele cumpre seu papel acadêmico ao integrar teoria e prática, mas também abre espaço para evoluções futuras:

- 🔧 **Expansão de variáveis**: incluir novos fatores como topografia, temperatura e falhas mecânicas.  
- 📈 **Aprimoramento dos gráficos**: adicionar dashboards interativos para análise em tempo real.  
- 🌍 **Aplicações terrestres**: adaptar o modelo para simulações em logística, transporte e gerenciamento de riscos.  
- 🤝 **Colaboração interdisciplinar**: integrar áreas como engenharia aeroespacial, ciência de dados e ética em tecnologia.  

> O projeto mostra que a exploração espacial não é apenas sobre tecnologia avançada, mas também sobre responsabilidade, aprendizado contínuo e visão de futuro.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.



