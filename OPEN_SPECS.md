# Open Specs - Simulador de Frutas

## Objetivo
Esta aplicação Streamlit simula a evolução da firmeza e do teor de °Brix de diferentes frutas ao longo do tempo, considerando temperatura, etileno, humidade relativa e valores iniciais do utilizador.

## Funcionalidades principais
- Seleção de idioma: Português, Inglês, Espanhol e Turco.
- O idioma inicial por defeito é Português.
- A interface, os nomes das frutas, as métricas, os gráficos e as mensagens devem refletir o idioma selecionado.
- Seleção de fruta a partir de um conjunto de presets pré-definidos.
- Ajuste de parâmetros de simulação:
  - temperatura (°C)
  - etileno (ppm)
  - humidade relativa (%)
  - número de dias
  - dureza inicial
  - °Brix inicial
- Visualização dos resultados em gráficos de:
  - dureza e °Brix ao longo do tempo
  - índice de qualidade ao longo do tempo
- Apresentação dos valores iniciais por defeito associados a cada fruta.

## Requisitos de execução
- Python 3.11 ou superior
- Dependências definidas em requirements.txt
- Comando de execução:
  python -m streamlit run app.py

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

## Publicação
A app pode ser publicada em Streamlit Cloud a partir deste repositório GitHub.
