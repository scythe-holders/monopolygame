from GUI import guiImage
import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((HOST, PORT))
    print("Connection successful!")
except ConnectionRefusedError:
    print("Connection failed: server is not available.")
except Exception as e:
    print("Connection failed:", e)


def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            break

thread = threading.Thread(target=receive_messages)
thread.start()


def send_to_backend(socket_conn, data):
    """
    Sends data to the backend via an existing socket connection.

    Args:
        socket_conn: a connected socket object.
        data: str or bytes to send.
    """
    try:
        if isinstance(data, str):
            data = data.encode()  
        socket_conn.sendall(data)
    except Exception as e:
        print(f"Error sending data: {e}")
        
        
        
        