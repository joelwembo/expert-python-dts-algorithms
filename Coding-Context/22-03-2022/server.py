# server
import socket 
import threading

HEADER = 64
PORT = 5053
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
SERVER = "192.168.254.101"
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect( "192.168.254.101")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))
    
    
send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello Tim!")


print("[STARTING] server is starting...")
start()