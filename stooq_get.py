import os
import sys

import pandas as pd
from pandas.errors import EmptyDataError


def get_csv(code: str):
    print(f'Request {symbol} data.')
    df = pd.read_csv(f'https://stooq.com/q/d/l/?s={code}&i=d', index_col=0)
    print(f'Get {symbol} data.\n')
    fileName = symbol.replace('.F', '') + '.csv'
    if os.name == 'nt':
        download = f'{os.environ["USERPROFILE"]}\\Downloads'
        filePath = f'{download}\\{fileName}'
    else:
        download = f"{os.getenv('HOME')}/Downloads"
        filePath = f'{download}/{fileName}'

    df.to_csv(filePath)


processingMethod = input('Select a processing number.\n'
                         '1: ES, NQ, ZB, UB(UD).\n'
                         '2: Manual input.\n')


if processingMethod == '1':
    symbols = ['ES.F', 'NQ.F', 'ZB.F', 'UD.F']

    for symbol in symbols:
        get_csv(symbol)

elif processingMethod == '2':
    symbol = input('Please input a symbol.\n')
    try:
        get_csv(symbol)
    except EmptyDataError:
        input('\n!!ERROR!!\n'
              'The symbol you entered does not exist.')
        sys.exit()

else:
    input('Processing number input error.')
    sys.exit()

input('Done. Check your downloads folder.')
