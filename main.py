# Predictive analysis of earthquakes in/around Japan

import pandas as pd
from googletrans import Translator

df = pd.read_csv('dataset/earthquakes_japan.csv')  # reads dataset
print(df)
