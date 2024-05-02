import pandas as pd

df = pd.read_csv("datasets/train.csv")

df["Age"] = df["Age"].fillna(df["Age"].mean())

df.to_csv("datasets/train.csv", index=False)
