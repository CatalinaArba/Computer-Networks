import socket
def sendable_data(data):
    return str(data).rjust(1024, " ").encode("utf-8")


if __name__=="__main__":
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host='192.168.0.111'
    port=9999
    s.connect((host, port))

    string_s=input("Enter the string: ")

    s.sendall(sendable_data(len(string_s)))
    for i in string_s:
        s.sendall(sendable_data(i))
    print("First array sent: "+string_s)

    c = input("Enter the char: ")
    s.sendall(sendable_data(c))

    data = s.recv(1024)
    len_r = int(data.decode("utf-8").strip())
    resulted_list = []
    for i in range(0, len_r):
        data = s.recv(1024)
        e= int(data.decode("utf-8").strip())
        resulted_list.append(e)

    print(repr(resulted_list))