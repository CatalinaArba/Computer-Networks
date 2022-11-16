import socket
import struct

def sendable_data(data):
    return str(data).encode("utf-8")


if __name__=="__main__":
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host='192.168.0.111'
    port=9999
    s.connect((host, port))

    message=input("Enter the string: ")
    s.sendall(sendable_data(message))
    print("Client sent the string="+message)
    c=s.recv(1024)
    count= int(c.decode("utf-8").strip())

    print('Count='+str(count))
    s.close()
