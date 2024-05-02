from catboost.datasets import titanic

# Загружаем данные 
train, test = titanic()

train.to_csv("datasets/train.csv", index=False)
test.to_csv("datasets/test.csv", index=False)
