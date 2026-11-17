# 🌊 SafeSlope
### *Safe slopes, peaceful lives.*

**Uma solução CitizenTech para prevenção de desastres urbanos, com foco em deslizamentos de terra e alagamentos.**

<p align="center">
  <strong>Global Solution 2026.2</strong> · Engenharia de Software · FIAP
</p>

---

## 📌 Sobre o projeto

O **SafeSlope** é uma solução tecnológica desenvolvida no contexto da Global Solution 2026.2, com o objetivo de contribuir para a prevenção de desastres naturais em regiões urbanas vulneráveis, especialmente áreas sujeitas a deslizamentos de terra e alagamentos.

A proposta busca aproximar moradores e equipes da Defesa Civil por meio de uma plataforma que permite registrar situações de risco, acompanhar ocorrências e analisar condições ambientais que podem indicar perigo.

O projeto tem como referência o contexto da Região Metropolitana de São Paulo, onde chuvas intensas podem causar alagamentos, instabilidade do solo e deslizamentos, colocando vidas e patrimônios em risco.

A aplicação desenvolvida em Python representa a camada de processamento e tomada de decisão da solução, organizando informações e classificando situações de risco para apoiar a prevenção e o acompanhamento de ocorrências.

## 🎯 Problema identificado

Moradores de regiões vulneráveis frequentemente enfrentam dificuldades para comunicar problemas relacionados à segurança de suas comunidades. Rachaduras no solo, acúmulo de água, encostas instáveis e pontos de alagamento podem passar despercebidos ou demorar para chegar ao conhecimento dos órgãos responsáveis.

Entre os principais desafios estão:

- Dificuldade para registrar e comunicar situações de risco.
- Falta de organização no acompanhamento de ocorrências.
- Necessidade de identificar áreas que exigem maior atenção.
- Demora na comunicação entre moradores e equipes responsáveis.
- Vulnerabilidade de comunidades expostas a chuvas intensas e eventos climáticos extremos.

## 💡 Nossa solução

O SafeSlope propõe uma plataforma de apoio à prevenção de desastres, permitindo que moradores registrem problemas identificados em suas regiões e que equipes da Defesa Civil acompanhem essas informações de maneira organizada.

A aplicação Python funciona como uma ferramenta de gerenciamento e análise dos dados cadastrados. Por meio de regras de negócio, o sistema processa informações ambientais e ocorrências registradas, atribuindo níveis de risco às áreas monitoradas.

Dessa forma, o projeto busca transformar informações isoladas em dados organizados que possam auxiliar na identificação de prioridades e na tomada de decisões.

## 👥 Público-alvo

- **Moradores de áreas de encosta:** pessoas que vivem em regiões sujeitas a deslizamentos.
- **Populações próximas a rios e córregos:** comunidades expostas a alagamentos.
- **Trabalhadores e comerciantes:** pessoas que exercem atividades em regiões vulneráveis.
- **Defesa Civil:** equipes responsáveis pelo acompanhamento e gerenciamento de ocorrências.

## ⚙️ Funcionalidades

A aplicação foi planejada para atender a dois perfis principais: Morador e Defesa Civil.

### 🏠 Perfil Morador

- Cadastro e consulta de informações relacionadas às áreas monitoradas.
- Registro de relatos sobre problemas identificados na região.
- Comunicação de situações como rachaduras, acúmulo de água e outros sinais de perigo.
- Acompanhamento das informações e do andamento dos relatos registrados.

### 🚨 Perfil Defesa Civil

- Consulta das áreas cadastradas.
- Visualização das informações ambientais registradas.
- Consulta e gerenciamento dos relatos enviados pelos moradores.
- Atualização do status das ocorrências.
- Identificação de situações que exigem maior atenção.

### 📊 Análise e classificação de risco

O sistema utiliza regras de negócio para analisar informações relacionadas às condições das áreas monitoradas.

Entre os fatores considerados estão:

- Nível de água registrado em relação ao limite definido para a área.
- Intensidade da chuva.
- Umidade do solo em áreas de encosta.
- Existência de relatos graves ainda não resolvidos.

A partir dessas informações, o sistema classifica as condições em quatro níveis:

| Nível | Significado |
|---|---|
| 🟢 NORMAL | Condições dentro dos parâmetros definidos. |
| 🟡 ATENÇÃO | Situação que exige acompanhamento. |
| 🟠 ALERTA | Condições que indicam risco elevado. |
| 🔴 CRÍTICO | Situação de maior gravidade, que exige atenção prioritária. |

> **Importante:** a classificação é baseada nas regras implementadas no protótipo acadêmico. Ela não representa um sistema oficial de previsão de desastres nem substitui avaliações técnicas da Defesa Civil.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Aplicação no projeto |
|---|---|
| Python 3 | Desenvolvimento da aplicação e implementação das regras de negócio. |
| JSON | Armazenamento e recuperação dos dados. |
| Git e GitHub | Versionamento e organização do projeto. |

## 🧠 Conceitos de Python aplicados

O desenvolvimento da aplicação utiliza conceitos fundamentais da disciplina **Computational Thinking with Python**:

- **Variáveis e tipos de dados:** armazenamento e manipulação das informações.
- **Estruturas condicionais:** tomada de decisões com `if`, `elif` e `else`.
- **Estruturas de repetição:** utilização de `while` e `for` para controlar fluxos e percorrer dados.
- **Funções:** organização da lógica em blocos reutilizáveis, com parâmetros e retornos.
- **Listas, tuplas e dicionários:** organização e manipulação dos registros.
- **Validação de entradas:** verificação dos dados informados pelos usuários.
- **Tratamento de exceções:** utilização de `try` e `except` para lidar com entradas inválidas e possíveis erros.
- **Manipulação de arquivos JSON:** leitura e gravação dos dados para persistência das informações.

## 🗂️ Organização do projeto

A aplicação foi organizada em módulos para separar as responsabilidades e facilitar a manutenção do código.

```text
SafeSlope/
│
├── main.py
├── config.py
├── dados.py
├── entradas.py
├── regras.py
├── telas.py
├── morador.py
├── defesa_civil.py
│
├── dados/
│   └── dados.json
│
├── prompts.md
└── README.md
```

### Responsabilidade dos módulos

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Inicialização da aplicação e controle do fluxo principal. |
| `config.py` | Definições e configurações utilizadas pelo sistema. |
| `dados.py` | Leitura, gravação e gerenciamento dos dados em JSON. |
| `entradas.py` | Validação e tratamento das informações digitadas pelo usuário. |
| `regras.py` | Implementação das regras de negócio e classificação de risco. |
| `telas.py` | Exibição de menus, mensagens e elementos da interface no terminal. |
| `morador.py` | Funcionalidades relacionadas ao perfil Morador. |
| `defesa_civil.py` | Funcionalidades relacionadas ao perfil Defesa Civil. |

*Observação: a estrutura acima representa a organização dos módulos da aplicação. O arquivo JSON é utilizado para persistir as informações cadastradas.*

## ▶️ Como executar o projeto

### 1. Pré-requisitos

Para executar a aplicação, é necessário ter:

- Python 3 instalado.
- Git instalado (opcional, caso queira clonar o repositório).

### 2. Clonar o repositório

```bash
git clone https://github.com/SafeSlope/gs_python
```

Entre na pasta do projeto:

```bash
cd SafeSlope
```

### 3. Executar a aplicação

```bash
python main.py
```

Caso esteja utilizando Windows e o comando `python` não funcione, tente:

```bash
py main.py
```

Após a execução, o menu principal será apresentado no terminal, permitindo navegar pelas funcionalidades disponíveis.

## 💾 Persistência de dados

O SafeSlope utiliza arquivos JSON para armazenar as informações da aplicação.

Esse formato permite salvar e recuperar os dados mesmo após o encerramento do programa, evitando que os registros sejam perdidos a cada nova execução.

As informações são organizadas em estruturas de dados que representam, entre outros elementos:

- Áreas monitoradas.
- Leituras e informações ambientais.
- Relatos registrados pelos moradores.

## 🌱 Objetivos de Desenvolvimento Sustentável (ODS)

O projeto está conectado a dois Objetivos de Desenvolvimento Sustentável da Organização das Nações Unidas:

### ODS 11 — Cidades e Comunidades Sustentáveis

<sub>Objetivo: tornar as cidades e os assentamentos humanos inclusivos, seguros, resilientes e sustentáveis.</sub>

O SafeSlope contribui com essa proposta ao buscar melhorar a organização de informações sobre áreas vulneráveis e apoiar ações de prevenção de desastres urbanos.

### ODS 13 — Ação contra a Mudança Global do Clima

<sub>Objetivo: tomar medidas urgentes para combater a mudança climática e seus impactos.</sub>

A solução está relacionada à necessidade de preparação e prevenção diante de eventos climáticos extremos, como chuvas intensas e suas consequências nas cidades.

## 🚀 Próximos passos

O SafeSlope é um projeto acadêmico com possibilidade de evolução. Entre as melhorias planejadas estão:

- Integração com sensores físicos para coleta de dados ambientais.
- Monitoramento de chuva, umidade do solo e nível da água em tempo real.
- Integração com serviços meteorológicos e fontes de dados externas.
- Desenvolvimento de uma interface web para moradores e equipes da Defesa Civil.
- Implementação de notificações e alertas direcionados por região.
- Utilização de dados históricos para aprimorar a análise de risco.
- Integração com serviços e órgãos responsáveis pela prevenção de desastres.

## 👨‍💻 Integrantes

Projeto desenvolvido por estudantes do curso de Engenharia de Software da FIAP.

| Integrante | RM |
|---|---|
| Gustavo Braga | 569211 |
| Henry Gabriel | 570063 |
| Nicholas Belo | 571063 |
| Renan Bonanno | 573043 |
| Murillo Dourado | 571912 |

## 📚 Contexto acadêmico

**Instituição:** FIAP — Faculdade de Informática e Administração Paulista  
**Curso:** Engenharia de Software  
**Projeto:** Global Solution 2026.2 — CitizenTech  
**Disciplina:** Computational Thinking with Python  
**Tema:** Prevenção de desastres urbanos — encostas e alagamentos.

---

<p align="center">
  <strong>🌊 SafeSlope — Safe slopes, peaceful lives.</strong>
  <br>
  <sub>Tecnologia, prevenção e informação para comunidades mais seguras.</sub>
</p>
