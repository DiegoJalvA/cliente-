import socket
import threading
import time
from tqdm import tqdm

# Pedir la IP y el puerto del servidor
host = input("Ingresa la IP del servidor: ")
port = int(input("Ingresa el puerto del servidor: "))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Simular animación de conexión con tqdm
print("Conectando al servidor...")
with tqdm(total=100, desc="Conectando", unit="%", ncols=50) as pbar:
    for _ in range(10):  # Simular la conexión en 10 pasos
        time.sleep(0.3)  # Simula el tiempo de espera
        pbar.update(10)

client_socket.connect((host, port))
print("\n✅ Conexión establecida con el servidor.")

# Enviar nombre de usuario
username = input("Elige tu nombre de usuario: ")
client_socket.sendall(username.encode())


def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"\n{data.decode()}\n{username}: ", end="")
        except:
            break


threading.Thread(target=receive_messages, daemon=True).start()

while True:
    message = input(f"{username}: ")
    if message.lower() == "salir":
        break

    client_socket.sendall(message.encode())

client_socket.close()
print("Desconectado del servidor.")