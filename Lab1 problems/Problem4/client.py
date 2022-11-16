import socket
def sendable_data(data):
    return str(data).rjust(1024, " ").encode("utf-8")


if __name__=="__main__":
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host='192.168.0.111'
    port=9999
    s.connect((host, port))
    l1=[]
    nr1=int(input("Enter the number of elements for the first list: "))
    for i in range(0,nr1):
        e=input('e=')
        l1.append(e)

    s.sendall(sendable_data(nr1))
    for i in l1:
        s.sendall(sendable_data(i))
    print("First array sent: "+repr(l1))

    l2 = []
    nr2 = int(input("Enter the number of elements for the second list: "))
    for i in range(0, nr2):
        e = input('e=')
        l2.append(e)

    s.sendall(sendable_data(nr2))
    for i in l2:
        s.sendall(sendable_data(i))
    print("Second array sent: "+repr(l2))

    resulted_list=[]
    for i in range(0,nr1+nr2):
        data=s.recv(1024)
        letter = data.decode("utf-8").strip()
        resulted_list.append(letter)

    print(repr(resulted_list))
    s.close()
