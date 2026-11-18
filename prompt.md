# SafeSlope — Registro de uso de IA
## Computational Thinking with Python | Global Solution 2026.2

---

## 1. Ferramenta de IA utilizada

- **Ferramenta:** assistente de IA conversacional.
- **Finalidade:** apoiar a compreensão dos requisitos, discutir decisões de implementação, revisar regras de negócio e sugerir cenários de teste.
- **Responsabilidade do grupo:** avaliar as sugestões, conferir sua compatibilidade com o código e com o enunciado da atividade, executar o programa e decidir quais alterações serão incorporadas.

## 2. Contexto do projeto fornecido à IA

O SafeSlope é uma aplicação de terminal em Python voltada ao monitoramento simulado de áreas sujeitas a deslizamentos e alagamentos. O sistema possui dois perfis principais:

- **Morador:** consulta o nível de risco de uma área, registra pontos de risco e acompanha relatos por protocolo.
- **Defesa Civil:** cadastra áreas, registra leituras simuladas de sensores, consulta uma fila de prioridades, atualiza o andamento dos relatos e visualiza indicadores.
- **Simulação de tempestade:** calcula a intensidade da chuva e o nível acumulado de água durante seis horas, utilizando o modelo matemático definido no projeto.

A aplicação está dividida em módulos: `main.py`, `config.py`, `dados.py`, `entradas.py`, `regras.py`, `simulacao.py`, `telas.py`, `morador.py` e `defesa_civil.py`. Os dados são armazenados localmente em JSON, sem bibliotecas externas.

---

## 3. Perguntas técnicas e respostas

### Interação 1 — Como transformar leituras em uma classificação de risco?

**Prompt:**

> Analise a regra de classificação de risco do SafeSlope. O sistema recebe nível de água, limite da área, intensidade da chuva e, no caso de encostas, umidade do solo. Como esses dados são combinados? Explique o motivo de utilizar uma pontuação e quais são os limites da abordagem.

**Resposta da IA:**

Na implementação atual, a função `classificar_risco()` do módulo `regras.py` começa calculando a relação entre o nível de água medido e o limite cadastrado para a área:

`pontuacao = nivel_mm / limite_mm * 100`

Depois, são adicionados pontos quando existem condições que aumentam a preocupação:

- **+10 pontos:** intensidade da chuva maior ou igual a 30 mm/h.
- **+15 pontos:** umidade do solo maior ou igual a 80%, somente para áreas do tipo `encosta`.
- **+10 pontos:** existe pelo menos um relato grave ainda não resolvido na área.

A pontuação final é convertida em uma categoria:

| Pontuação | Classificação |
|---|---|
| Menor que 50 | NORMAL |
| De 50 até menos de 75 | ATENCAO |
| De 75 até menos de 100 | ALERTA |
| Igual ou maior que 100 | CRITICO |

A vantagem dessa estratégia é reunir diferentes sinais em uma regra simples, compreensível e fácil de testar. Por exemplo, uma área pode apresentar nível de água abaixo do limite, mas a chuva intensa e os relatos da comunidade podem elevar a classificação.

Entretanto, essa pontuação é uma **regra simplificada de simulação**, não um modelo oficial de previsão de desastres. Os pesos e limites precisam ser calibrados com dados técnicos e validação de especialistas antes de qualquer uso real. O próprio README informa que os limites utilizados são valores de exemplo.

**Ponto de atenção para o grupo:** explicar que a pontuação organiza os sinais disponíveis, mas não garante que um evento ocorrerá nem substitui os alertas oficiais.

---

### Interação 2 — Por que separar o programa em módulos?

**Prompt:**

> Avalie a divisão dos arquivos do SafeSlope. Seria melhor manter todas as funcionalidades em um único arquivo ou separar menus, regras, persistência e validação? Explique como essa organização ajuda na manutenção e no desenvolvimento em equipe.

**Resposta da IA:**

A separação atual é adequada porque cada módulo possui uma responsabilidade predominante:

| Módulo | Responsabilidade |
|---|---|
| `main.py` | Iniciar a aplicação e direcionar os menus |
| `config.py` | Centralizar constantes e configurações |
| `dados.py` | Carregar, salvar e consultar os dados |
| `entradas.py` | Ler e validar informações digitadas |
| `regras.py` | Calcular risco, prioridade e indicadores |
| `simulacao.py` | Executar o modelo matemático da tempestade |
| `telas.py` | Exibir e selecionar áreas monitoradas |
| `morador.py` | Implementar as operações do perfil morador |
| `defesa_civil.py` | Implementar as operações da Defesa Civil |

Se todas essas funções estivessem em um único arquivo, alterações em uma funcionalidade poderiam tornar mais difícil localizar problemas em outra. Com os módulos, por exemplo, uma mudança na fórmula de risco fica concentrada em `regras.py`, enquanto a validação de números pode ser ajustada em `entradas.py`.

Essa divisão também facilita a leitura do código e permite que integrantes trabalhem em partes diferentes, desde que respeitem as interfaces entre os módulos.

**Ponto de atenção para o grupo:** modularização não significa que os arquivos não dependem uns dos outros. É importante observar os `import` e os parâmetros recebidos pelas funções para evitar dependências desnecessárias.

---

### Interação 3 — Como garantir que os dados não desapareçam ao fechar o programa?

**Prompt:**

> No SafeSlope, áreas, leituras e relatos precisam continuar disponíveis depois que o usuário fecha o terminal. Explique como a persistência em JSON foi implementada, quais são suas vantagens e quais cuidados ainda seriam necessários.

**Resposta da IA:**

O módulo `dados.py` concentra a persistência. A função `carregar_dados()` tenta abrir o arquivo definido por `ARQUIVO_DADOS`, atualmente `safeslope_dados.json`, e utiliza `json.load()` para reconstruir os dados em estruturas Python.

O programa organiza as informações em três listas:

- `areas`: áreas monitoradas e seus limites.
- `leituras`: medições registradas para cada área.
- `relatos`: ocorrências informadas pelos moradores e seus históricos.

Quando o arquivo ainda não existe, `dados_vazios()` fornece uma estrutura inicial com as três listas vazias. Quando o JSON está sintaticamente corrompido, o programa apresenta um aviso e começa com dados vazios. A função `salvar_dados()` utiliza `json.dump()` para gravar as informações com indentação e suporte a caracteres acentuados.

O JSON é uma escolha simples para um projeto acadêmico executado localmente: não exige instalar um banco de dados e permite visualizar os registros em um editor de texto.

Há limitações importantes. O tratamento atual identifica arquivo inexistente e erro de sintaxe JSON, mas não valida profundamente todos os campos de um arquivo que seja JSON válido. Também não oferece controle de acesso, histórico de versões, transações ou proteção adequada para múltiplos usuários gravando simultaneamente.

**Ponto de atenção para o grupo:** o JSON atende ao escopo didático atual, mas não deve ser apresentado como solução de armazenamento pronta para uma operação real da Defesa Civil.

---

### Interação 4 — Como evitar entradas inválidas nos menus e cadastros?

**Prompt:**

> Revise o módulo `entradas.py`. Por que utilizar laços `while`, `try/except` e limites mínimo e máximo nas funções de leitura? Dê exemplos de situações que o programa precisa tratar.

**Resposta da IA:**

As funções de entrada evitam que valores incompatíveis cheguem às regras de negócio.

- `ler_texto()` remove espaços nas extremidades e exige uma quantidade mínima de caracteres.
- `ler_numero()` tenta converter a entrada para `float`, aceita vírgula como separador decimal e verifica se o valor está dentro do intervalo permitido.
- `ler_inteiro()` converte para `int` e verifica os limites.
- `ler_tipo_area()` aceita somente os tipos definidos em `TIPOS_AREA`: `encosta` ou `alagamento`.

O `while True` permite solicitar novamente a informação quando ela é inválida. O `try/except ValueError` impede que uma entrada como `abc` encerre inesperadamente a execução durante uma conversão numérica.

Exemplos de testes úteis:

1. Digitar letras quando o sistema espera um número.
2. Informar um valor abaixo do mínimo ou acima do máximo.
3. Digitar um tipo de área não cadastrado.
4. Informar um texto vazio ou muito curto.
5. Digitar um número decimal em um campo que exige inteiro.

A validação melhora a experiência do usuário e reduz a chance de dados fora do formato esperado. Ela não substitui, porém, a validação das relações entre os dados, como garantir que uma leitura esteja associada a uma área existente.

**Ponto de atenção para o grupo:** os limites de entrada são regras definidas pelo projeto. O grupo deve saber justificar por que cada campo aceita determinado intervalo.

---

### Interação 5 — Como organizar e priorizar os relatos dos moradores?

**Prompt:**

> O SafeSlope permite que moradores registrem rachaduras, muros inclinados e outros pontos de risco. Explique como o protocolo, o histórico de status e a fila de prioridades funcionam. Existe alguma diferença entre gravidade do relato e risco calculado da área?

**Resposta da IA:**

O perfil morador registra informações como área, tipo de ocorrência, localização, descrição e gravidade. A função `gerar_protocolo()` cria um identificador no formato `SS-ANO-NÚMERO`, e o relato é salvo junto com um histórico inicial contendo a data, o status e a observação de recebimento.

O fluxo de status definido em `config.py` é:

`RECEBIDO → EM_ANALISE → VISTORIADO → RESOLVIDO`

A função `atualizar_status()` avança somente para a próxima etapa, evitando que o fluxo volte para um status anterior. O morador pode consultar o andamento informando o protocolo.

A prioridade utiliza duas informações diferentes:

- **Gravidade do relato:** nota informada pelo morador, de 1 a 5.
- **Pontuação da área:** resultado das regras de risco calculadas com base na leitura mais recente e nos fatores adicionais.

A função `calcular_prioridade()` combina essas informações:

`prioridade = gravidade * 10 + pontuacao_area * 0.5`

A fila é ordenada em ordem decrescente, de modo que os relatos com maior pontuação apareçam primeiro.

Essa combinação é uma regra de priorização definida para a aplicação. Ela ajuda a organizar o atendimento, mas não representa uma avaliação profissional da ocorrência. Além disso, o relato é uma informação fornecida pela comunidade e precisa ser verificado pela equipe responsável.

---

### Interação 6 — Como verificar se a simulação matemática está coerente?

**Prompt:**

> Analise o módulo `simulacao.py`. Explique a relação entre as funções de intensidade da chuva e nível acumulado, o papel do escoamento e como testar o instante em que o limite de água é atingido.

**Resposta da IA:**

O módulo utiliza o modelo matemático definido para a atividade, considerando uma tempestade de seis horas.

A intensidade da chuva é dada por:

`r(t) = -2t² + 12t`

O nível acumulado é calculado por:

`h(t) = -(2/3)t³ + 6t² - E·t`

Em que `t` representa o tempo em horas e `E` é a capacidade de escoamento informada pelo usuário, em mm/h.

A função `intensidade_chuva(t)` calcula a intensidade em determinado instante. Já `nivel_acumulado(t, escoamento)` calcula o nível acumulado segundo a expressão fornecida.

A função `simular_tempestade()` percorre o intervalo da simulação em passos de 0,01 hora para encontrar o primeiro instante em que o nível calculado alcança o limite informado. Depois, monta uma tabela com intervalos de meia hora para exibição.

Na tabela, o nível é limitado a zero com `max(0.0, ...)`, pois o projeto não apresenta acúmulo negativo de água. Essa proteção é aplicada à exibição da tabela; a busca do instante crítico utiliza diretamente a expressão matemática.

Um cenário de conferência é utilizar `E = 8 mm/h` e limite de `10 mm`. Pela expressão, o limite é atingido aproximadamente em `2,80 h`. Como a busca avança em passos de 0,01 hora, o resultado é uma aproximação, não uma solução algébrica exata.

**Ponto de atenção para o grupo:** a simulação é um modelo didático simplificado. Ela não incorpora características reais de uma bacia, topografia, infiltração variável ou calibração meteorológica.

---

## 5. Análise crítica do uso da IA e do projeto

### Benefícios

- A IA pode ajudar a decompor um problema grande em partes menores.
- A discussão das regras de risco ajuda a conferir se os fatores utilizados estão claros.
- A revisão dos módulos facilita identificar responsabilidades e dependências.
- A criação de cenários de teste ajuda o grupo a verificar entradas válidas, inválidas e situações de limite.

### Limitações

- Uma resposta da IA pode parecer convincente mesmo quando não corresponde ao código. Por isso, cada sugestão precisa ser comparada com a implementação.
- A classificação de risco utiliza pesos e limites simplificados, sem validação com dados oficiais.
- As leituras são digitadas manualmente para representar os dados que poderiam ser enviados por sensores; não existe integração direta com ESP32 nesta aplicação Python.
- O armazenamento em JSON é adequado ao escopo acadêmico, mas não oferece os recursos de segurança e concorrência esperados em um sistema de produção.
- A simulação matemática representa o modelo da disciplina, não uma previsão meteorológica ou hidrológica real.

### Responsabilidade do grupo

O uso da IA deve servir como apoio à aprendizagem e à revisão técnica. O grupo precisa compreender as funções, explicar as decisões de implementação, executar os testes e registrar somente os resultados que verificou. As respostas deste documento devem ser ajustadas quando a implementação ou os requisitos da atividade forem diferentes.

---

## 6. Conclusão

A análise do SafeSlope mostra como conceitos de Python podem ser aplicados a um problema social: modularização, funções, estruturas de dados, validação de entradas, tratamento de exceções, persistência em JSON, ordenação e regras condicionais.

A IA pode apoiar a investigação e a revisão dessas decisões, mas não substitui a compreensão do código nem a validação do funcionamento do sistema. O principal critério para considerar uma sugestão adequada é verificar se ela atende aos requisitos do projeto e se o grupo consegue explicar e demonstrar seu funcionamento.
