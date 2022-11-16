import socket
import struct

def sendable_data(data):
    return str(data).rjust(1024, " ").encode("utf-8")


if __name__=="__main__":
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host='192.168.0.111'
    port=9999
    a=int(input('a='))
    b=int(input('b='))

    s.connect((host,port))

    s.sendall(str(a).rjust(1024, " ").encode("utf-8"))
    s.sendall(str(b).rjust(1024, " ").encode("utf-8"))
    print("a and b were sent")
    c=s.recv(1024)
    sum= int(c.decode("utf-8").strip())

    print('a+b='+str(sum))
    s.close()