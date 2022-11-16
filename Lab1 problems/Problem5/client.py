import socket
import struct
import pickle
def sendable_data(data):
    return str(data).rjust(1024, " ").encode("utf-8")


if __name__=="__main__":
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host='192.168.0.111'
    port=9999
    s.connect((host, port))

    nr=int(input("Nr="))
    s.send(sendable_data(nr))

    data = s.recv(1024)
    div_nr= int(data.decode("utf-8").strip())
    resulted_list=[]
    for i in range(0,div_nr):
        data=s.recv(1024)
        div=int( data.decode("utf-8").strip())
        resulted_list.append(div)

    print(repr(resulted_list))
    s.close()