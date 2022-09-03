from pydoc import cli
import socket
def server():
    host = socket.gethostname()
    port = 3000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen()
    conn, address = server_socket.accept()
    print("Connected to: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Recieved data : " + str(data))
        data = input('Enter the message for client : ')
        conn.send(data.encode())
    conn.close()

if __name__ == '__main__':
    server()