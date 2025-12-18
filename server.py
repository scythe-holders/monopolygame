import socket
import threading
from xmlrpc.client import Server

class server:

    def __init__(self, host='127.0.0.1', port=5555):
        self.PlayerNUM = {}
        self.HOST = host
        self.PORT = port
        self.clients = []

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.HOST, self.PORT))
        self.server.listen()
        self.start()
        # self.server.settimeout(120)

    def handle_client(self, conn):
        try:
            while len(self.clients) < 4:
                data = conn.recv(1024)
                if not data:
                    break
            self.broadcast(data)
        except:
            pass

    def start(self):
        self.server.settimeout(1)
        try:
            while True:
                try:
                    conn, addr = self.server.accept()
                    if conn:
                        print("1 person connected")
                except socket.timeout:
                    continue
                t = threading.Thread(target=self.handle_client,
                                     args=(conn,), daemon=True)
                t.start()
                self.clients.append(conn)
                print(len(self.clients))
                self.broadcast(
                    f"server: Player {len(self.clients)} has joined the game.")
                if (len(self.clients) > 3):
                    print("Maximum number of players reached.")
                    break
                self.game()
        except KeyboardInterrupt:
            print("\nShutting down server...")

    def broadcast(self, message):
        """
        Send `message` to all connected clients.
        """
        for client in self.clients:
            try:
                client.sendall(message.encode())
            except:
                print("Error sending message to client.")

    def Closing(self):
        if input() == "C":
            self.server.close()

    def game(self):
        print("game started")
if __name__ == "__main__":
    s = server()
    s.start()
