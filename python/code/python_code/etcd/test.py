import etcd

# etcd_client = etcd.Client()
etcd_client = etcd.Client(host="10.153.205.30",allow_reconnect="True",port=8379,protocol='http')
etcd_client.write('/a', 1)
a = etcd_client.read('/a').value

print(a)










# print(etcd_client.read('/').value)