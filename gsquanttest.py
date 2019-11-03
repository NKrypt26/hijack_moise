from gs_quant.data import Dataset

from gs_quant.session import GsSession

client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'

GsSession.use(client_id=client_id, client_secret=client_secret)

weather_ds = Dataset(Dataset.GS.WEATHER)
weather_ds.get_coverage()