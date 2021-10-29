import cacheclient
import time

client = cacheclient.CacheClient(port=1191)
client.setData('tKey1', 'tValueasdsadas', 1, False)
time.sleep(2)
print(client.getData('tKey1'))
print(client.getServerData())
