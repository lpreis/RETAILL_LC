# Open Specs - Simulador de Frutas

## Objetivo
Esta aplicação Streamlit simula a evolução pós-colheita de diferentes frutas ao longo do tempo, considerando condições ambientais, atmosfera de armazenamento e valores iniciais do utilizador.

O simulador deve evoluir para um Digital Twin pós-colheita capaz de estimar firmeza, teor de °Brix, qualidade, risco de bolor e vida útil restante com base nos parâmetros ativos do modelo.

## Funcionalidades principais
- Seleção de idioma: Português, Inglês, Espanhol e Turco.
- O idioma inicial por defeito é Português.
- A interface, os nomes das frutas, as métricas, os gráficos e as mensagens devem refletir o idioma selecionado.
- Seleção de fruta a partir de um conjunto de presets pré-definidos.
- Ajuste de parâmetros de simulação:
  - temperatura (°C)
  - humidade relativa (%)
  - etileno (ppm)
  - CO2 (%)
  - número de dias
  - dureza inicial (N)
  - °Brix inicial
- Seleção explícita dos parâmetros ambientais usados no modelo:
  - usar temperatura: sim/não
  - usar humidade relativa: sim/não
  - usar etileno: sim/não
  - usar CO2: sim/não
  - usar bolor/carga microbiológica no índice de qualidade: sim/não
- Visualização dos resultados em gráficos de:
  - dureza e °Brix ao longo do tempo
  - índice de qualidade ao longo do tempo
  - bolor/carga microbiológica ao longo do tempo, quando este módulo estiver ativo
- Apresentação dos valores iniciais por defeito associados a cada fruta.

## Unidade de dureza
A dureza/firmeza deve ser expressa explicitamente em Newton (N).

Cada preset deve incluir:

```text
firmness_unit = "N"
```

Campos calibrados em Newton:
- `dureza_0_default`
- `dureza_min`
- `qual_firm_threshold`

Nota exibida na app:

```text
Dureza expressa em Newton (N). Para frutos pequenos, representa força de compressão/penetração aproximada e deve ser calibrada com o protocolo experimental usado.
```

Conversões úteis:

```text
1 kgf = 9.80665 N
1 lbf = 4.44822 N
```

Valores recomendados para os presets:

| Fruta | dureza_0_default | dureza_min | qual_firm_threshold |
| --- | ---: | ---: | ---: |
| Kiwi Hayward | 75 N | 5 N | 12 N |
| Kiwi Baby | 35 N | 2 N | 8 N |
| Maçã Golden | 72 N | 12 N | 35 N |
| Maçã Reineta | 65 N | 10 N | 30 N |
| Maçã Gala | 60 N | 9 N | 28 N |
| Maçã Fuji | 80 N | 15 N | 40 N |
| Laranja | 55 N | 30 N | 38 N |
| Banana | 25 N | 2 N | 8 N |
| Mirtilo | 3 N | 0.5 N | 1.5 N |
| Framboesa | 1.5 N | 0.2 N | 0.7 N |
| Pera | 60 N | 4 N | 12 N |
| Ameixa | 35 N | 3 N | 8 N |
| Pêssego | 35 N | 2 N | 8 N |
| Cereja | 6 N | 1 N | 3 N |
| Morango | 3 N | 0.5 N | 1.5 N |
| Uva | 5 N | 1 N | 2.5 N |
| Figo | 2 N | 0.2 N | 0.8 N |
| Melão | 40 N | 3 N | 12 N |

## Parâmetros selecionáveis do modelo
Cada fator ambiental deve poder ser ativado ou desativado sem remover o respetivo controlo da interface.

Quando um parâmetro está ativo, o seu fator multiplicativo é usado na taxa de deterioração. Quando está inativo, o fator correspondente deve ser neutro, isto é, igual a 1.

Exemplo:

```text
k = k_base * k_T * k_RH * k_E * k_CO2
```

Com seleção de parâmetros:

```text
k_T   = f_T(T)             se temperatura ativa; caso contrário 1
k_RH  = f_RH(RH)           se humidade ativa; caso contrário 1
k_E   = f_E(etileno)       se etileno ativo; caso contrário 1
k_CO2 = f_CO2(CO2)         se CO2 ativo; caso contrário 1
```

Isto permite comparar cenários como:
- modelo apenas com temperatura e humidade
- modelo com temperatura, humidade e etileno
- modelo com temperatura, humidade e CO2
- modelo completo com temperatura, humidade, etileno, CO2 e bolor

## Perfis temporais dos parâmetros ambientais
Os parâmetros ambientais não devem estar limitados a valores constantes. O simulador deve suportar perfis temporais para transformar os inputs em funções do tempo:

```text
T(t), RH(t), E_ext(t), CO2(t)
```

Por defeito, a app deve manter o modo simples com valores constantes. Quando o modo avançado estiver ativo, o utilizador deve poder selecionar um modelo temporal para cada parâmetro.

Modelos temporais recomendados:
- constante
- aumento linear
- diminuição linear
- aproximação exponencial a um valor alvo
- oscilação diária
- degrau
- pulso

Cada parâmetro deve ter:
- valor base
- modelo temporal
- parâmetros específicos do modelo selecionado

Exemplo de temperatura com oscilação diária:

```text
T(t) = T0 + A sin(2*pi*t/P + phase)
```

Exemplo de aproximação exponencial:

```text
x(t) = x_inf + (x0 - x_inf) * exp(-rate * t)
```

Exemplo de pulso de etileno:

```text
E(t) = E_pulse entre t_start e t_end; caso contrário E0
```

O motor de simulação deve usar o valor de cada perfil em cada passo temporal, e não apenas o valor inicial.

Na prática:

```text
k(t) = k_base * k_T(T(t)) * k_RH(RH(t)) * k_E(E_ext(t)) * k_CO2(CO2(t))
```

As variáveis devem ser limitadas aos intervalos físicos aceitáveis:
- temperatura: intervalo operacional definido pela app
- RH: 0-100%
- etileno: >= 0 ppm
- CO2: 0-20%

O gráfico dos perfis ambientais deve ser mostrado quando o modo avançado estiver ativo.

## CO2
O CO2 deve ser adicionado como novo input do simulador, expresso em percentagem.

Valor inicial recomendado:

```text
CO2 = 0.04 %
```

Intervalo recomendado para o controlo:

```text
0 % a 20 %
```

Exemplo de slider:

```python
co2_pct = st.slider("CO2 (%)", min_value=0.0, max_value=20.0, value=0.04, step=0.1)
```

O fator de CO2 deve reduzir a taxa de respiração e deterioração quando o CO2 aumenta, dentro de limites biologicamente aceitáveis para cada fruta.

Modelo inicial recomendado:

```text
k_CO2 = 1 / (1 + beta_CO2 * CO2_pct)
```

Interpretação:
- CO2 mais alto reduz respiração
- menor respiração reduz amadurecimento
- menor amadurecimento preserva dureza
- preservação da dureza aumenta shelf-life

O valor `beta_CO2` deve poder ser definido por fruta no preset ou, numa primeira versão, ser usado como constante global.

## Bolor / carga microbiológica
O bolor não deve ser tratado como input principal do utilizador. Deve ser uma variável de estado interna do modelo.

Variável:

```text
M(t)
```

Onde:
- `M = 0` representa ausência de bolor/carga microbiológica relevante
- `M = 1` representa contaminação máxima ou produto não comercializável

Modelo inicial:

```text
dM/dt = r_M(T, RH) * (1 - M)
```

Modelo melhorado com dano físico:

```text
dM/dt = r_M(T, RH) * (1 - M) * (1 + gamma_D * D)
```

Onde:
- `D` é o índice de dano físico
- `gamma_D` controla quanto o dano acelera o crescimento microbiológico

Fatores principais do bolor:
- humidade relativa
- temperatura
- tempo
- dano físico, opcional numa versão posterior

O bolor deve poder afetar o índice de qualidade quando o módulo estiver ativo. Quando estiver inativo, a qualidade deve ser calculada sem penalização microbiológica.

## O2
O O2 deve ser considerado como extensão futura do simulador.

Motivação:
- atmosferas controladas e modificadas usam simultaneamente O2 e CO2
- frutas como maçã, kiwi e pera podem ser armazenadas durante longos períodos com O2 baixo e CO2 moderado

Exemplo industrial:
- ar normal: O2 aproximadamente 21%, CO2 aproximadamente 0.04%
- atmosfera controlada: O2 aproximadamente 1-3%, CO2 aproximadamente 1-5%

Numa segunda versão, deve ser adicionado:
- input O2 (%)
- seletor usar O2: sim/não
- fator `k_O2`
- eventual cálculo explícito de respiração

## Outputs esperados
### Nível 1
Inputs:
- temperatura
- humidade relativa
- etileno
- CO2

Outputs:
- dureza
- °Brix
- bolor/carga microbiológica
- qualidade

### Nível 2
Inputs:
- temperatura
- humidade relativa
- etileno
- CO2
- O2

Outputs:
- dureza
- °Brix
- bolor/carga microbiológica
- respiração
- etileno endógeno
- qualidade
- shelf-life

### Nível 3 - RETAIL LC Agent
Outputs:
- Freshness Index
- Remaining Shelf Life
- Waste Risk
- Carbon Impact
- Recommended Route
- Recommended Storage

Este nível deve alimentar agentes de routing, stock e decisão dentro da arquitetura RETAILL/RETAIL LC.

## Requisitos de execução
- Python 3.11 ou superior
- Dependências definidas em requirements.txt
- Comando de execução:

```bash
python -m streamlit run app.py
```

## Estrutura do projeto
- app.py - aplicação principal Streamlit
- requirements.txt - dependências da app
- logos/ - imagens dos logos usados na interface

## Comportamento esperado
- Ao abrir a app, o seletor de idioma deve estar em Português.
- Ao alterar o idioma, os textos visíveis da interface devem mudar sem alterar os valores da simulação.
- Ao alterar a fruta, os valores por defeito associados à fruta devem ser carregados automaticamente no menu lateral.
- O utilizador pode depois ajustar manualmente esses valores antes de correr a simulação.
- Os valores de dureza inicial e °Brix inicial usados na simulação devem corresponder aos valores visíveis no menu no momento da execução.
- O modelo deve usar o valor de °Brix inicial informado pelo utilizador na simulação e nos gráficos.
- O modelo deve respeitar os seletores de ativação dos parâmetros ambientais.
- Parâmetros desativados devem ser tratados como fatores neutros no modelo.
- O CO2 deve reduzir a taxa de deterioração quando ativo.
- O bolor deve evoluir internamente ao longo do tempo e não deve ser exigido como input principal do utilizador.

## Publicação
A app pode ser publicada em Streamlit Cloud a partir deste repositório GitHub.
