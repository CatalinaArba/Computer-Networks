import socket
import sys

#1.   A client sends to the server an array of numbers. Server returns the sum of the numbers.
#Create a socket (connesct two computers)
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
        s.listen(5)#the number the bad connection that it will tollerate until it will call th error

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
    dataa=conn.recv(1024)
    datab=conn.recv(1024)
    a=int(dataa.decode("utf-8").strip())
    b=int(datab.decode("utf-8").strip())
    s=int(a+b)
    print(a,b,s)
    print("a and b were received")
    conn.sendall(str(s).rjust(1024, " ").encode("utf-8"))

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()