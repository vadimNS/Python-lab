import socket
import threading
from tkinter import *

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            log_text.insert(END, message + "\n")
        except:
            break

def send_message():
    message = entry_message.get()
    if message:
        client.send(message.encode())
        entry_message.delete(0, END)

def on_closing():
    client.send("quit".encode())
    client.close()
    root.quit()

if __name__ == "__main__":
    root = Tk()
    root.title("Chat Client")
    root.geometry("400x300")

    log_text = Text(root, wrap=WORD)
    log_text.pack(expand=YES, fill=BOTH)

    entry_message = Entry(root)
    entry_message.pack(expand=YES, fill=X)

    send_button = Button(root, text="Send", command=send_message)
    send_button.pack()

    username = input("Enter your username: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))
    client.send(username.encode())

    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
