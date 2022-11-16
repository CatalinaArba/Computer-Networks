# 2.   The client sends the complete path to a file. The server returns back the length of the file and its content in the case the file exists. When the file does not exist the server returns a length of -1 and no content. The client will store the content in a file with the same name as the input file with the suffix –copy appended (ex: for f.txt => f.txt-copy).
import socket
import threading
import os.path
def sendable_data(data):
    return str(data).encode("utf-8")
#1.   A client sends to the server an array of numbers. Server returns the sum of the numbers.
#Create a socket (connesct two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host="127.0.0.1"
        port=9999
        s=socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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
        bind_socket((host,port))

#Establish connection with client (socket must be listening)
def socket_accept():
    conn,address=s.accept()
    print("Connection has been establish | "+"IP "+address[0]+ "| Port "+str(address[1]))

    thread = threading.Thread(target=handler, args=(conn, address))
    thread.start()


#Send commands to client/victim or a friend
def handler(conn,address):
    path = str(conn.recv(1024).decode())
    print("Server received path: ", path)

    if os.path.isfile(path):
        f = open(path, "r")
        data = f.read()
        number_of_characters = len(data)
        conn.send(str(number_of_characters).rjust(1024, " ").encode("utf-8"))
        for i in data:
            conn.send(str(i).rjust(1024, " ").encode("utf-8"))
        f.close()
    else:
        msg=-1
        conn.send(str(msg).rjust(1024, " ").encode("utf-8").strip())

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
