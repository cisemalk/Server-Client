from asyncore import socket_map
import socket
import threading
import datetime

HEADER = 64
PORT = 555
SERVER = "192.168.1.16" # socket.gethostbyname(socket.gethostname()) #"192.168.1.16"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def getMessage(conn):
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length = int(msg_length)
        return conn.recv(msg_length).decode(FORMAT)
        

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    conn.send("Welcome".encode(FORMAT))
    usercheck=True
    okeyforadking=False
    connected = True
    while connected:
        if usercheck:
            conn.send("Enter user name: ".encode(FORMAT))
            usernam = getMessage(conn)
            
            conn.send("Enter password: ".encode(FORMAT))
            password = getMessage(conn)
            
            if usernam=="CMPE322" and password == "bilgiuni":
                conn.send("You are OK for asking me.".encode(FORMAT))
                okeyforadking=True
                usercheck=False
            else:
                conn.send("You are NOT OK for asking me. Try again.".encode(FORMAT))

        elif okeyforadking:
            conn.send("1.date\n2.time\n3.capTurkey\n4.quit".encode(FORMAT))
            while okeyforadking:
                msg = getMessage(conn)
                if msg == "date":
                    x= datetime.datetime.now()
                    conn.send(x.strftime("%x").encode(FORMAT))
                elif msg == "time":
                    x= datetime.datetime.now()
                    conn.send(x.strftime("%X").encode(FORMAT))
                elif msg == "capTurkey":
                    conn.send("Ankara".encode(FORMAT))
                elif msg == "quit":
                    conn.send("Bye bye".encode(FORMAT))
                    okeyforadking=False
                    print(f"[DISCONNECTION] {addr} disconnected")   
                    conn.close()
                    connected=False
                else:
                    conn.send("Enter a valid response".encode(FORMAT))              
    

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()