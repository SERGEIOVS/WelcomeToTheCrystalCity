import socket
import threading
import json
import sys
import time
import keyboard  # pip install keyboard

from pathlib import Path

# путь к Scripts/Python
sys.path.append(str(Path(__file__).resolve().parent))


#CLIENT

HOST = "127.0.0.1"
PORT = 5000

players = {}

def net_thread(sock):
    global players

    try:
        while True:
            raw = sock.recv(1024)
            if not raw:
                break

            for line in raw.split(b"\n"):
                if not line.strip():
                    continue

                data = json.loads(line.decode())

                if data["type"] == "update":
                    players = data["players"]

                elif data["type"] == "join":
                    print("Игрок вошёл:", data["id"])

                elif data["type"] == "leave":
                    print("Игрок вышел:", data["id"])

    except:
        pass
    sys.exit()


def main():
    sock = socket.socket()
    sock.connect((HOST, PORT))

    threading.Thread(target=net_thread, args=(sock,), daemon=True).start()

    print("Клиент запущен")

    while True:
        dx = dy = 0

        if keyboard.is_pressed("up"):
            dy = -1
        if keyboard.is_pressed("down"):
            dy = 1
        if keyboard.is_pressed("left"):
            dx = -1
        if keyboard.is_pressed("right"):
            dx = 1

        if dx != 0 or dy != 0:
            msg = json.dumps({"type": "move", "dx": dx, "dy": dy}) + "\n"
            sock.sendall(msg.encode())

        print("\033c", end="")
        print("Игроки в мире:")
        for pid, pos in players.items():
            print(f"{pid}: x={pos['x']} y={pos['y']}")

        time.sleep(0.1)


if __name__ == "__main__":
    main()
