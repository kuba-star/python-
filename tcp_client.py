import socket

target_url="127.0.0.1"
target_port=45535

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建套接字
client.connect((target_url,target_port))#建立连接
client.send(b"hello")#发送数据
response=client.recv(4096)#接受数据
client.close()#关闭连接
print(response)
