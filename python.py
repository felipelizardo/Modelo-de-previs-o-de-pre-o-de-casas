import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
import numpy as np

df = pd.read_csv("Housing.csv")


print(f"Linhas: {df.shape[0]} | Colunas: {df.shape[1]}")
df.info()

print(f"VALORES NULOS:\n{df.isnull().sum()}")
print(f"VALORES DUPLICADOS: {df.duplicated().sum()}")
print(f"ESTATISTICAS:\n{df.describe().T}")

# valores que não fazem sentido
checagem = {
    "price <= 0": (df["price"] <= 0).sum(),
    "area <= 0": (df["area"] <= 0).sum(),
    "bedrooms < 1": (df["bedrooms"] < 1).sum(),
    "bathrooms < 1": (df["bathrooms"] < 1).sum(),
    "stories < 1": (df["stories"] < 1).sum(),
    "parking < 0": (df["parking"] < 0).sum(),
}
print(checagem)

colunas_texto = ["mainroad", "guestroom", "basement", "hotwaterheating",
                 "airconditioning", "prefarea", "furnishingstatus"]
for c in colunas_texto:
    df[c] = df[c].str.strip().str.lower()
    print(f"{c:18s} ->", sorted(df[c].unique()))


df_limpo = df.copy()

# Variáveis sim/não -> 1/0
colunas_binarias = ["mainroad", "guestroom", "basement",
                    "hotwaterheating", "airconditioning", "prefarea"]
for c in colunas_binarias:
    df
    df_limpo[c] = df_limpo[c].map({"yes": 1, "no": 0})

# Mobília (3 categorias) -> variáveis dummy (one-hot), descartando uma categoria de referência
df_limpo = pd.get_dummies(df_limpo, columns=["furnishingstatus"], drop_first=True, dtype=int)

print("Valores nulos após o tratamento:", df_limpo.isna().sum())
df_limpo.head()

#criando o modelo 
X = df_limpo.drop(columns=["price"])
y = df_limpo["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Criar o modelo
modelo = LinearRegression()

# Treinar o modelo
modelo.fit(X_train, y_train)

# Fazer previsões
previsoes = modelo.predict(X_test)

#pontuação do modelo

# Prever o preço
nova_casa = pd.DataFrame([{
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
    "furnishingstatus_unfurnished": 0
}])


preco_previsto = modelo.predict(nova_casa)[0]

print(f"Preço previsto para a nova casa: {preco_previsto:,.2f}")

mae = mean_absolute_error(y_test, previsoes)
rmse = np.sqrt(mean_squared_error(y_test, previsoes))
r2 = r2_score(y_test, previsoes)

# Exibir resultados
print(f"R²: {r2:.3f}")
print(f"MAE: {mae:,.2f}")
print(f"RMSE: {rmse:,.2f}")