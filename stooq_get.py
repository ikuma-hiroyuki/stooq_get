import os
import pandas as pd


def get_price(code):
    df = pd.read_csv(f'https://stooq.com/q/d/l/?s={code}&i=d', index_col=0)
    return df


symbole = input('Please enter a symbol.\n')
df = get_price(symbole)
download = os.environ["USERPROFILE"] + r'\Downloads'
file = download + '\\' + symbole + '.CSV'
print(file)
df.to_csv(file)

input('Completed')
