import random
import socket
import struct

def sendable_data(data):
    return str(data).encode("utf-8")


if __name__=="__main__":
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host='localhost'
    port=5555
    s.connect((host, port))

    #Read inputs
    nr= random.randint(0,10)


    #Send imputs
    s.sendall(sendable_data(nr))
    print("Command was sent"+str(nr))

    #Receive outputs
    data=s.recv(1024)
    output=data.decode("utf-8").rjust(1024, " ").strip()

    print(output)
    s.close()

