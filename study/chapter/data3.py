import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

picher_file_path = '../data/picher_stats_2017.csv'
batter_file_path = '../data/batter_stats_2017.csv'
picher = pd.read_csv(picher_file_path)
batter = pd.read_csv(batter_file_path)

print(picher.columns)

print(picher.head())

print(picher.shape)


print(picher['연봉(2018)'].describe())

picher['연봉(2018)'].hist(bins = 100)