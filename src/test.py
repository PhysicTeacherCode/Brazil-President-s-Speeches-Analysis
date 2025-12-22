import pandas as pd
import numpy as np

dados = {
    'A': [1,2,3,4,6,1,2,0]
}
df = pd.DataFrame(dados)

df['A'] = df['A'].rolling(window = 5, step = 2, min_periods = 1, center = True, closed = 'both').mean()

print(df['A'])