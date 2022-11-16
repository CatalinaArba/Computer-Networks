#8.   The client sends to the server two arrays of integers. The server returns an arrays containing the common numbers found in both arrays
import socket
import sys

#3.   A client sends to the server a string. The server returns the reversed string to the client (characters from the end to begging)
def create_socket():
    try:
        global host
        global port
        global s
        host="192.168.0.111"
        port=9999
        s=socket.socket()
    except socket.error as msg:
        print ("Socket creation error: "+str(msg))

#Binding the socket and listening for connection
def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port "+str(port))

        s.bind((host,port))
        s.listen(100)#the number the bad connection that it will tollerate until it will call th error

    except socket.error as msg:
        print("Socket binding error: "+str(msg)+"\n"+"Retrying..")
        bind_socket()

#Establish connection with client (socket must be listening)
def socket_accept():
    conn,address=s.accept()
    print("Connection has been establish | "+"IP "+address[0]+ "| Port "+str(address[1]))
    send_commands(conn)
    conn.close()



#Send commands to client/victim or a friend
def send_commands(conn):
    data=conn.recv(1024)
    #Reading data
    nr1= int(data.decode("utf-8").rjust(1024, " ").strip())
    l1=[]
    for i in range(0,nr1):
        data = conn.recv(1024)
        e= int(data.decode("utf-8").rjust(1024, " ").strip())
        l1.append(e)
    print("Server received l1")

    data = conn.recv(1024)
    nr2 = int(data.decode("utf-8").rjust(1024, " ").strip())
    l2 = []
    for i in range(0, nr2):
        data = conn.recv(1024)
        e = int(data.decode("utf-8").rjust(1024, " ").strip())
        l2.append(e)
    print("Server received l2")

    #Computing data
    common_list = set(l1).intersection(l2)

    #Sending data
    conn.sendall(str(len(common_list)).rjust(1024, " ").encode("utf-8"))
    for i in common_list:
       conn.sendall(str(i).rjust(1024, " ").encode("utf-8"))


def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
