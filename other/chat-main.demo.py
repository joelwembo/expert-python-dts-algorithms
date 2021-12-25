import socket

def Welcomemsg():
    print('Server Program Running...')

def Server_program():

    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn,address = server_socket.accept()
    print("Connection from: " + str(address))

    #Start the chat functionalities
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("From Connected User client: " + str(data))
        data = input(" -> ")   
        conn.send(data.encode()) 
    conn.close()

if __name__ == '__main__':
       Welcomemsg()
       Server_program()