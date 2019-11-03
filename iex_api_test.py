from datetime import datetime
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

# from iexfinance.stocks import Stock
#
# def getInfo(ticker, date):
#     #date format 'yyyy-mm-dd'
#     import json
#     tickerS = Stock(ticker, token=IEX_TOKEN)
#     stockInfo = tickerS.get_quote()
#     sheet = tickerS.get_historical_data(ticker, date, date, output_formate='pandas', token=IEX_TOKEN)
#     info = [stockInfo['symbol'], stockInfo['companyName'], sheet]
#     print(sheet)
#
# array = getInfo('AAPL', '2016-03-13')
# print(array)






# from iexfinance.stocks import Stock
#
# a = Stock("AAPL", token="pk_59ecee438d9947bdb0d4434ea5d66114")
# quote = a.get_quote()
