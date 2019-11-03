from datetime import datetime
from datetime import timedelta

from iexfinance.stocks import get_historical_data

IEX_TOKEN = 'pk_59ecee438d9947bdb0d4434ea5d66114'

def makeGraph(ticker):
    start = datetime(2014, 1, 1)
    end = datetime(2018, 1, 1)

    df = get_historical_data(ticker, start, end, output_format='pandas', token=IEX_TOKEN)

    plot = df['close']

    import matplotlib.pyplot as plt
    plot.plot()
    return plt

from iexfinance.stocks import Stock

def getInfo(ticker, datetime):
    tickerS = Stock(ticker, token=IEX_TOKEN)
    stockInfo = tickerS.get_quote()
    sheet = get_historical_data(ticker, datetime, datetime.now() + timedelta(days=1), output_format='pandas', token=IEX_TOKEN)
    info = [stockInfo['symbol'], stockInfo['companyName']]
    print(sheet)
    return info

array = getInfo('AAPL', datetime(2016, 3, 13))
print(array)