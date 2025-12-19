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

    def handle_client(self, conn):
        try:
            while True:
                data = conn.recv(1024)
                self.broadcast(data)
                print(data)
        except:
            pass

    def reasiving_massage():
        print("x")

    def start(self):
        self.server.settimeout(1)
        try:
            while True:
                try:
                    conn, addr = self.server.accept()
                    if conn:
                        self.PlayerNUM[f"conn number {0}".format(
                            len(self.clients))] = conn
                        print("1 person connected")
                        print(self.PlayerNUM)
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
        Send bytes `message` to all connected clients.
        """
        for client in self.clients:
            try:
                client.sendall(message)
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
