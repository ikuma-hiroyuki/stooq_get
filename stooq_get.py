import os
import pandas as pd


def get_price(code):
    df = pd.read_csv(f'https://stooq.com/q/d/l/?s={code}&i=d', index_col=0)
    return df


print('Start acquiring stooq data.')
symbols = ['ES.F', 'NQ.F', 'ZB.F', 'UL.F']

for symbol in symbols:
    print('Request ' + symbol + ' data.')
    df = get_price(symbol)
    print('Get ' + symbol + ' data.\n')
    download = os.environ["USERPROFILE"] + r'\Downloads'
    file = download + '\\' + symbol + '.CSV'
    df.to_csv(file)

input('Completed.')
