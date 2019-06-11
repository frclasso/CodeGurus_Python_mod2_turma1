import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data, wb
import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime, timedelta

# stock of interest
stock = [
    'ABEV3.SA',
    'B3SA3.SA',
    'BBAS3.SA',
    'BBDC3.SA',
    'BBDC4.SA',
    'BBSE3.SA',
    'BRAP4.SA',
    'BRFS3.SA',
    'BRKM5.SA',
    'BRML3.SA',
    'BTOW3.SA',
    'CCRO3.SA',
    'CIEL3.SA',
    'CMIG4.SA',
    'CPLE6.SA',
    'CSAN3.SA',
    'CSNA3.SA',
    'CVCB3.SA',
    'CYRE3.SA',
    'ECOR3.SA',
    'EGIE3.SA',
    'ELET3.SA',
    'ELET6.SA',
    'EMBR3.SA',
    'ENBR3.SA',
    'EQTL3.SA',
    'ESTC3.SA',
    'FIBR3.SA',
    'FLRY3.SA',
    'GGBR4.SA',
    'GOAU4.SA',
    'GOLL4.SA',
    'HYPE3.SA',
    'IGTA3.SA',
    'ITSA4.SA',
    'ITUB4.SA',
    'JBSS3.SA',
    'KLBN11.SA',
    'KROT3.SA',
    'LAME4.SA',
    'LREN3.SA',
    'MGLU3.SA',
    'MRFG3.SA',
    'MRVE3.SA',
    'MULT3.SA',
    'NATU3.SA',
    'PCAR4.SA',
    'PETR3.SA',
    'PETR4.SA',
    'QUAL3.SA',
    'RADL3.SA',
    'RAIL3.SA',
    'RENT3.SA',
    'SANB11.SA',
    'SBSP3.SA',
    'SMLS3.SA',
    'SUZB3.SA',
    'TAEE11.SA',
    'TIMP3.SA',
    'UGPA3.SA',
    'USIM5.SA',
    'VALE3.SA',
    'VIVT4.SA',
    'VVAR11.SA',
    'WEGE3.SA']

# period of analysis
end = datetime.now()
start = end - timedelta(days=20)

values = {}

for i in range(len(stock)):
    try :
        f = wb.DataReader(stock[i], 'yahoo', start, end)

        f = f.reset_index()

        if i == 0:
            values['Date'] = f.Date.values
        # a.append(f.Close.values);
        print(len(f.Close.values))
        if len(f.Close.values) == 1361:
            values[stock[i]] = f.Close.values
            print(len(f.Close.values))
    except:
        print(stock[i] + ' failed')

# values['date'] =  f.Date.values[0:-6]

# f = pd.Series(a[0],f.Date)
bb = pd.DataFrame.from_dict(values)

bb.to_excel('micrsoft.xls')
print(bb)
# plt.show();