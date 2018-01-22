"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import Tkinter


def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(Tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()

def select_protocol(event=None):
    if selected_protocol.get() == "TCP":
        client_socket = socket(AF_INET, SOCK_STREAM)
    elif selected_protocol.get() == "UDP":
        client_socket = socket(socket.AF_INET, socket.SOCK_DGRAM)


top = Tkinter.Tk()
top.title("Chatter")

messages_frame = Tkinter.Frame(top)
my_msg = Tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Type your messages here.")
scrollbar = Tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = Tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.grid(column=1, row=0, sticky="NS")
msg_list.grid(column=0, row=0, sticky="NSEW")

entry_field = Tkinter.Entry(messages_frame, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.grid(column=0, row=1, sticky="EW")
send_button = Tkinter.Button(messages_frame, text="Send", command=send)
send_button.grid(column=0, row=2, sticky="EW")

emoji_frame = Tkinter.Frame(messages_frame)
emoji_frame.grid(column=0, row=3,  sticky="EW")
# photo = Tkinter.PhotoImage(file="emojiler/rsz_unamused_face_emoji.png", width=20, height=20)
# angry = Tkinter.Button(emoji_frame, image=photo, relief="flat").grid(row=2, column=0)
# angry2 = Tkinter.Button(emoji_frame, image=photo, relief="flat").grid(row=2, column=1)
# angry3 = Tkinter.Button(emoji_frame, image=photo, relief="flat").grid(row=2, column=2)
# angry4 = Tkinter.Button(emoji_frame, image=photo, relief="flat").grid(row=2, column=3)
# angry5 = Tkinter.Button(emoji_frame, image=photo, relief="flat").grid(row=2, column=4)
# angry6 = Tkinter.Button(emoji_frame, image=photo, relief="flat").grid(row=2, column=5)

photo2 = Tkinter.PhotoImage(file="emojiler/rsz_very_angry_emoji.png", width=20, height=20)
happy = Tkinter.Button(emoji_frame, image=photo2, relief="flat").grid(row=0, column=0)
happy2 = Tkinter.Button(emoji_frame, image=photo2, relief="flat").grid(row=0, column=1)
happy3 = Tkinter.Button(emoji_frame, image=photo2, relief="flat").grid(row=0, column=2)
happy4 = Tkinter.Button(emoji_frame, image=photo2, relief="flat").grid(row=0, column=3)
happy5 = Tkinter.Button(emoji_frame, image=photo2, relief="flat").grid(row=0, column=4)
happy6 = Tkinter.Button(emoji_frame, image=photo2, relief="flat").grid(row=0, column=5)

photo3 = Tkinter.PhotoImage(file="emojiler/rsz_tears_of_joy_emoji.png", width=20, height=20)
face = Tkinter.Button(emoji_frame, image=photo3, relief="flat").grid(row=1, column=0)
face2 = Tkinter.Button(emoji_frame, image=photo3, relief="flat").grid(row=1, column=1)
face3 = Tkinter.Button(emoji_frame, image=photo3, relief="flat").grid(row=1, column=2)
face4 = Tkinter.Button(emoji_frame, image=photo3, relief="flat").grid(row=1, column=3)
face5 = Tkinter.Button(emoji_frame, image=photo3, relief="flat").grid(row=1, column=4)
face6 = Tkinter.Button(emoji_frame, image=photo3, relief="flat").grid(row=1, column=5)
messages_frame.grid(row=0, column=0)


settings_frame = Tkinter.Frame(top)

protocol_frame = Tkinter.Frame(settings_frame)
selected_protocol = Tkinter.StringVar()

udp_button = Tkinter.Radiobutton(settings_frame, text="UDP", variable=selected_protocol, value="udp", command=send)
udp_button.grid(row=0, column=0)
tcp_button = Tkinter.Radiobutton(settings_frame, text="TCP", variable=selected_protocol, value="tcp", command=send)
tcp_button.grid(row=0, column=1)

host_msg =  Tkinter.StringVar()
host_msg.set("Enter IP Address")
ip_field = Tkinter.Entry(settings_frame, textvariable=host_msg)
ip_field.bind("<Return>", send)
ip_field.grid(column=0, row=1, columnspan=2, sticky="EW")

port_msg = Tkinter.StringVar()
port_msg.set("Enter Port Number")
ip_field = Tkinter.Entry(settings_frame, textvariable=port_msg)
ip_field.bind("<Return>", send)
ip_field.grid(column=0, row=2, columnspan=2, sticky="EW")

send_file_button = Tkinter.Button(settings_frame, text="Send File", relief="ridge").grid(row=3, column=0, columnspan=2,
                                                                                         sticky="EW")


protocol_frame.grid(row=1, column=0, padx=10)
settings_frame.grid(row=0, column=1, padx=10)

top.protocol("WM_DELETE_WINDOW", on_closing)


# ----Now comes the sockets part----
HOST = input("host ")
PORT = input("port ")
if not PORT:
    PORT = 8888
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
Tkinter.mainloop()


  # Starts GUI execution.
