import socket
import threading

# Pedir la IP y el puerto del servidor
host = input("Ingresa la IP del servidor: ")
port = int(input("Ingresa el puerto del servidor: "))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

print("Conectado al servidor. Escribe 'salir' para desconectarte.")


def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"\n{data.decode()}\nCliente: ", end="")
        except:
            break


threading.Thread(target=receive_messages, daemon=True).start()

while True:
    message = input("Cliente: ")
    if message.lower() == "salir":
        break
    client_socket.sendall(message.encode())

client_socket.close()
print("Desconectado del servidor.")
