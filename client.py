import socket
import concurrent.futures as pool
import sys

def receive_message(conn):
    while True:
        try:
            msg = conn.recv(2048).decode('utf-8')
            print(msg)
        except:
            print("Server Down")
            sys.exit()

HOST_IP = "127.0.0.1"
PORT = 80
executor = pool.ThreadPoolExecutor()
name = input("Enter Username: ")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST_IP, PORT))

server.send(name.encode('utf-8'))

executor.submit(receive_message, server)

while True:
    msg = input('Type Message: ')
    server.send(msg.encode('utf-8'))
