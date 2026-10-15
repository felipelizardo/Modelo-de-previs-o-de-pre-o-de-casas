# Previsão de Preços de Imóveis
Projeto de estudo em Python que treina um modelo de regressão linear para estimar preços de imóveis a partir de características como área, número de quartos e banheiros, localização e itens de infraestrutura.

O programa utiliza o arquivo `Housing.csv` como fonte de dados, separa uma parte dos registros para avaliação e também calcula uma previsão para um imóvel de exemplo definido no próprio script.

## Tecnologias utilizadas

- **Python 3**: linguagem do projeto.
- **Pandas**: leitura, inspeção e preparação dos dados tabulares.
- **NumPy**: cálculo da raiz do erro quadrático médio (RMSE).
- **scikit-learn**: divisão entre treino e teste, treinamento do modelo e cálculo das métricas.
- **Matplotlib**: importado no script, mas ainda não utilizado.
- **CSV**: formato do conjunto de dados de entrada.

## Funcionamento do projeto

1. **Leitura dos dados:** carrega `Housing.csv` com o Pandas.
2. **Inspeção:** exibe dimensões, tipos de dados, valores ausentes, duplicados, estatísticas descritivas e contagens de algumas condições consideradas inválidas (por exemplo, área menor ou igual a zero). Essas condições são contabilizadas, mas não removem registros.
3. **Normalização de texto:** remove espaços nas extremidades e converte para minúsculas as colunas categóricas.
4. **Codificação das categorias:** converte os atributos `yes`/`no` para `1`/`0` e aplica one-hot encoding a `furnishingstatus`, descartando uma categoria como referência.
5. **Preparação para o aprendizado:** define `price` como variável-alvo e usa as demais colunas como atributos de entrada. Separa 20% dos registros para teste e usa `random_state=42` para tornar essa divisão reproduzível.
6. **Treinamento e previsão:** ajusta um modelo `LinearRegression` aos dados de treino, faz previsões para o conjunto de teste e calcula uma estimativa para o imóvel de exemplo declarado no script.
7. **Avaliação:** apresenta R², MAE e RMSE para as previsões do conjunto de teste.

## Conceitos aplicados

- **Aprendizado supervisionado:** o modelo aprende a relacionar atributos dos imóveis aos preços conhecidos.
- **Regressão linear:** estima uma variável numérica contínua, neste caso o preço, como combinação linear dos atributos.
- **Separação treino/teste:** mantém parte dos exemplos fora do treinamento para avaliar o modelo em dados não usados no ajuste.
- **Pré-processamento categórico:** transforma categorias textuais em valores numéricos que o modelo pode utilizar. As variáveis binárias usam 0/1; as categorias de mobília são representadas por colunas indicadoras.
- **Métricas de regressão:** R² resume a proporção da variação explicada pelo modelo; MAE mede o erro absoluto médio; RMSE penaliza mais erros maiores por elevar os erros ao quadrado antes da média.
- **Estruturas de dados:** DataFrames do Pandas organizam os registros e colunas; um dicionário Python reúne as contagens das verificações de consistência.

## Instalação e configuração

É necessário ter Python 3 e `pip` instalados. O repositório não define uma versão mínima nem fixa as versões das bibliotecas.

1. Clone o repositório e acesse a pasta do projeto:

	```bash
	git clone <URL_DO_REPOSITORIO>
	cd <PASTA_DO_REPOSITORIO>
	```

2. (Opcional, recomendado) Crie e ative um ambiente virtual.

	No Windows:

	```powershell
	py -m venv .venv
	.\.venv\Scripts\Activate.ps1
	```

	No macOS ou Linux:

	```bash
	python3 -m venv .venv
	source .venv/bin/activate
	```

3. Instale as bibliotecas usadas pelo script:

	```bash
	python -m pip install pandas numpy scikit-learn matplotlib
	```

O arquivo `Housing.csv` deve permanecer na mesma pasta de onde o comando de execução será iniciado, pois o script o procura pelo caminho relativo `Housing.csv`.

## Como executar

Na pasta que contém `python.py` e `Housing.csv`, execute:

```bash
python python.py
```

No Windows, também é possível usar o inicializador:

```powershell
py python.py
```

O script imprime informações da base, a previsão para o imóvel definido no código e as métricas calculadas para o conjunto de teste.

## Exemplo de utilização

O imóvel de exemplo está definido em `python.py` com estes atributos já codificados:

```python
nova_casa = {
	 "area": 6500,
	 "bedrooms": 3,
	 "bathrooms": 2,
	 "stories": 2,
	 "mainroad": 1,
	 "guestroom": 0,
	 "basement": 1,
	 "hotwaterheating": 0,
	 "airconditioning": 1,
	 "parking": 2,
	 "prefarea": 1,
	 "furnishingstatus_semi-furnished": 1,
	 "furnishingstatus_unfurnished": 0,
}
```

Ao executar, o programa exibe a estimativa e, em seguida, as métricas. Os valores numéricos dependem da versão dos dados e das bibliotecas instaladas; não são fixados neste README.

```text
Preço previsto para a nova casa: <valor calculado>
R²: <valor calculado>
MAE: <valor calculado>
RMSE: <valor calculado>
```

Para testar outro imóvel, altere os valores de `nova_casa` em `python.py`, mantendo os mesmos nomes e a mesma codificação das colunas usadas no treinamento.

## Limitações conhecidas

- O exemplo de imóvel está fixo no código; não há entrada interativa nem interface de usuário.
- O script não salva o modelo treinado para uso posterior.
- As verificações de dados inconsistentes apenas contam ocorrências; não filtram nem corrigem esses registros.
- Não há validação cruzada, comparação com outros algoritmos ou ajuste de hiperparâmetros.
- A qualidade das previsões depende da representatividade e da qualidade do conjunto `Housing.csv`.
- `matplotlib` está importado, mas não há gráficos implementados. A chamada `df_limpo.head()` também não é impressa quando o arquivo é executado como script.

## Aprendizados

O projeto reúne práticas fundamentais de um fluxo de Machine Learning: leitura e exploração de dados, tratamento de categorias, separação entre treino e teste, treinamento de um estimador de regressão e análise de métricas. Também exercita o uso integrado de Pandas, NumPy e scikit-learn em um problema de previsão numérica.

## Próximas melhorias

- Criar um pipeline de pré-processamento e treinamento para manter as transformações consistentes entre treino e novas previsões.
- Validar os dados e tratar ou rejeitar registros inválidos antes do treinamento.
- Adicionar validação cruzada e comparar a regressão linear com modelos de referência.
- Registrar as versões das dependências em `requirements.txt`.
- Permitir informar as características do imóvel por argumentos, formulário ou interface simples.
- Adicionar testes automatizados para o pré-processamento e para as previsões.
- Implementar visualizações de exploração e avaliação usando Matplotlib, que já está importado.

## Autor

Desenvolvedor: **não informado**. Nome, perfil do GitHub e links profissionais podem ser adicionados aqui quando disponíveis.
>>>>>>> 4d9dcdc (Adicionando o README)
