import pandas as pd
import matplotlib.pyplot as plt

# 1. 데이터 특징 파악
midwest = pd.read_csv("midwest.csv")
print(midwest.head())
print(midwest.info())
print(midwest.describe())