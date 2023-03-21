import socket
import threading

IP='0.0.0.0'
port=45535

def main():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建套接字
    server.bind((IP,port))#绑定IP和端口
    server.listen(5)#开始监听,设置连接数5
    print(f'[*] Listening on {IP}:{port}')

    while True:
        client,address=server.accept()#将客户端socket对象保存在client中，远程连接详细地址保存在address中
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler=threading.Thread(target=handle_client,args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request=sock.recv(1024)
        print(f'[*] Received:{request.decode("utf-8")}')
        sock.send(b'ACK')

if __name__=='__main__':
    main()
        




