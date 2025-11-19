import socket
import threading
import json
import sys
from pathlib import Path

# путь к Scripts/Python
sys.path.append(str(Path(__file__).resolve().parent))


HOST = "0.0.0.0"
PORT = 5000
#SERVER
clients = {}        # conn → player_id
players = {}        # player_id → {"x":…, "y":…}
player_count = 0

def broadcast(data):
    msg = (json.dumps(data) + "\n").encode()
    for conn in list(clients.keys()):
        try:
            conn.sendall(msg)
        except:
            conn.close()
            del clients[conn]

def client_thread(conn):
    global player_count

    player_id = player_count
    player_count += 1

    clients[conn] = player_id
    players[player_id] = {"x": 0, "y": 0}

    broadcast({"type": "join", "id": player_id})

    try:
        while True:
            raw = conn.recv(1024)
            if not raw:
                break

            for line in raw.split(b"\n"):
                if not line.strip():
                    continue
                data = json.loads(line.decode())

                if data["type"] == "move":
                    p = players[player_id]
                    p["x"] += data["dx"]
                    p["y"] += data["dy"]

                    broadcast({
                        "type": "update",
                        "players": players
                    })

    except:
        pass

    conn.close()
    del clients[conn]
    del players[player_id]
    broadcast({"type": "leave", "id": player_id})


def main():
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen()

    print("SERVER STARTED")

    while True:
        conn, addr = s.accept()
        print("client connected:", addr)
        threading.Thread(target=client_thread, args=(conn,), daemon=True).start()


if __name__ == "__main__":
    main()
