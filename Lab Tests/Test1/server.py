import socket
import threading
import random
import struct
import time
threads = []
my_lock = threading.Lock()


def is_the_point_inside_the_circle(x,y,radius):
    center_x=0
    center_y=0
    L=(x-center_x)*(x-center_x)+(y-center_y)*(y-center_y)
    R=radius*radius
    if (L<R):
        return True
    return False

def handler(client,addr,radius):
    # print("Client connected ", addr)
    # data = client.recv(4)
    # client_UDP = struct.unpack('!I', data)[0]
    #print("Server received udp="+str(client_UDP))
    count_inside=0
    count_outside=0
    for i in range(0,100):
        data = client.recv(1024)
        x = int(data.decode("utf-8").rjust(1024, " ").strip())
        data = client.recv(1024)
        y = int(data.decode("utf-8").rjust(1024, " ").strip())
        print("ROUND "+str(i))
        print("Server received "+str(x)+" "+str(y))
        message=""
        if(is_the_point_inside_the_circle(x,y,radius)):
            message="Inside"
            count_inside+=1
        else:
            message="Outside"
            count_outside+=1
        client.send(message.encode())

        print("Count inside="+str(count_inside)+"  Count outside"+str(count_outside))
        time.sleep(1)

    client.close()


if __name__ == '__main__':
    radius=random.randint(0,100)
    print("Radius="+str(radius))
    try:
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind(("127.0.0.1",1234))
        server.listen(5)
    except Exception:
        print("Error on creating the socket")
        exit(-1)
    print("Server waiting for connection")
    while True:
        client, addr = server.accept()
        thread = threading.Thread(target=handler,args=(client,addr,radius))
        threads.append(thread)
        thread.start()