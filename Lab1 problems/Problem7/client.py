import socket
def sendable_data(data):
    return str(data).rjust(1024, " ").encode("utf-8")


if __name__=="__main__":
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host='192.168.0.111'
    port=9999
    s.connect((host, port))
    #Read input
    string_s=input("Enter the string: ")
    index=int(input("Enter the index: "))
    l = int(input("Enter the length: "))

    #Send to server
    s.sendall(sendable_data(len(string_s)))
    for i in string_s:
        s.sendall(sendable_data(i))
    print("First array sent: "+string_s)
    s.sendall(sendable_data(index))
    s.sendall(sendable_data(l))


    #Receive from server
    resulted_list = ""
    for i in range(0, l+1):
        data = s.recv(1024)
        e=data.decode("utf-8").strip()
        resulted_list+=e


    #Print data
    print("Result:" +resulted_list)