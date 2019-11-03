from datetime import datetime
from iexfinance.stocks import get_historical_data

IEX_TOKEN = 'pk_59ecee438d9947bdb0d4434ea5d66114'

start = datetime(2014, 1, 1)
end = datetime(2018, 1, 1)

df = get_historical_data("AMZN", start, end, output_format='pandas', token=IEX_TOKEN)

plot = df['close']


import matplotlib.pyplot as plt
plot.plot()
plt.show()




# from iexfinance.stocks import Stock
#
# a = Stock("AAPL", token="pk_59ecee438d9947bdb0d4434ea5d66114")
# quote = a.get_quote()
