import pandas as pd

df = pd.read_csv("datasets/train.csv")

# Кодируем строковые данные
df["Pclass"] = pd.Categorical(df["Pclass"]).codes
df["Sex"] = pd.Categorical(df["Sex"]).codes
df["Age"] = pd.cut(df["Age"], bins=[0, 18, 30, 45, 60, 80], labels=[0, 1, 2, 3, 4]).astype('float32')

df.to_csv("datasets/train.csv", index=False)
