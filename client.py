from pydoc import cli
import socket
def client():
    host = socket.gethostname()
    port = 3000
    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = input("Enter your message : ")
    while message.lower().strip() != 'over&out':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print('Messge received from server: ' + data)
        message = input("Enter your next message : ")
    client_socket.close()
if __name__ == '__main__':
    client()