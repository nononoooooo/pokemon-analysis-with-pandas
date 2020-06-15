import numpy as np
import pandas as pd

TOTAL_COLUMNS_NAME = "合計"

dataset = pd.read_csv("./dataset/pokemon_status.csv", encoding="utf-8")

print(dataset.head())

print("max:\n{0}".format(dataset.sort_values(TOTAL_COLUMNS_NAME, ascending=False)[:5]))

print("min\n{}".format(dataset.sort_values(TOTAL_COLUMNS_NAME)[:5]))

print("na:{}".format(dataset[TOTAL_COLUMNS_NAME].isna().sum()))

print(dataset.describe())
print(dataset.describe(exclude="number"))
