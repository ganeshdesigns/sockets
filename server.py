import socket
import time
import concurrent.futures as pool

def clientThread(client, host):
    name = client.recv(1024).decode('utf-8')
    print(f"{name} Connected to IP: {HOST_IP}")
    broadcast_all(f"{name} Connected".encode('utf-8'))

    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            msg = f"<{name}> {msg}"
            
            print(msg)
            broadcast(msg, client)
            
        except:
            remove(client)
            break

def broadcast(msg, conn):
    for client in list_of_clients:
        if client != conn:
            try:
                client.send(msg.encode('utf-8'))
            except:
                client.close()
                remove(client)
                
def broadcast_all(msg):
    for i in list_of_clients:
        i.send(msg)

def remove(conn):
    if conn in list_of_clients:
        list_of_clients.remove(conn)

list_of_clients = []
executor = pool.ThreadPoolExecutor()
HOST_IP = "127.0.0.1"
PORT = 80
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST_IP, PORT))

print(f"Server Initialized - IP: {HOST_IP} | PORT: {PORT}")
server.listen(100)

while True:
    conn, ip = server.accept()
    list_of_clients.append(conn)
    
    executor.submit(clientThread, conn, server)
