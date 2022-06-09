from pydoc import cli
import socket

HEADER = 64
PORT = 555
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER ="192.168.1.16"# "172.17.64.1"#"192.168.1.16"
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
userpass=False
adked=False


print(client.recv(2048).decode(FORMAT))
while True:
    if not userpass:
        print(client.recv(2048).decode(FORMAT))
        send(input())
        print(client.recv(2048).decode(FORMAT))
        send(input())
        y=client.recv(2048).decode(FORMAT)
        print(y)
        if y == "You are OK for asking me.":
            userpass=True
            print(client.recv(2048).decode(FORMAT))
    elif not adked:
        x = input()
        send(x)
        print(client.recv(2048).decode(FORMAT))
        if x == "quit":
            adked=True
            break

input()















