import pandas as pd
import csv
import plotly.express as pe

df = pd.read_csv("info.csv")

print(df.groupby("level")["attempt"].mean())

figure = pe.scatter(
            x=df.groupby("level")["attempt"].mean(),
            y=['Level 1', 'Level 2', 'Level 3', 'Level 4'],
            )

figure.show()
