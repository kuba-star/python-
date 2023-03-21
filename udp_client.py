import socket

target_url="127.0.0.1"
target_port=80

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#创建套接字
client.sendto(b'AAABBBCCC',(target_url,target_port))#发送数据
data,addr=client.recv(4096) #接受返回的数据
print(data.decode())
client.close()