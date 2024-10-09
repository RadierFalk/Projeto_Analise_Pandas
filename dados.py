# type: ignore

import pandas as pd 
import numpy as np

#Carregando o conjunto de dados em um quadro de dados usando Pandas
#@title
df = pd.read_csv('agricultural_raw_material.csv')

#Explorando o conjunto de dados
df.info
#checking Null Values of each column
df.isnull().sum()