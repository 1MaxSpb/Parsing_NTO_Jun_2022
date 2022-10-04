import pandas as pd

data = pd.read_csv('movies_emotions.csv')
name = input()
data[data['Жанр'] == name]