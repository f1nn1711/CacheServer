import cacheclient

client = cacheclient.CacheClient(port=1191)
client.setData('tKey22', 'tValueasdsadas', 10000, False)
print(client.getData('tKey22'))