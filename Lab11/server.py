import socket
import threading
from tkinter import *
from tkinter import scrolledtext

def client_thread(conn, addr, username):
    print(f"Connected by {addr} with username {username}")
    while True:
        message = conn.recv(1024).decode()
        if not message:
            break
        print(f"Received from {addr} ({username}): {message}")
        broadcast(f"{username}: {message}")
    conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen()

    while True:
        conn, addr = server.accept()
        username = conn.recv(1024).decode()
        thread = threading.Thread(target=client_thread, args=(conn, addr, username))
        thread.start()

def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode())
        except:
            clients.remove(client)

def on_send_message():
    message = entry_message.get()
    if message:
        broadcast(f"{username}: {message}")
        entry_message.delete(0, END)

if __name__ == "__main__":
    clients = []
    
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    # Tkinter GUI for server (optional)
    server_gui = Tk()
    server_gui.title("Server")
    server_gui.geometry("400x300")

    log_text = scrolledtext.ScrolledText(server_gui, wrap=WORD)
    log_text.pack(expand=YES, fill=BOTH)

    server_gui.mainloop()
