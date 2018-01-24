"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM, SOCK_DGRAM
from threading import Thread
import Tkinter
import Tkinter, Tkconstants, tkFileDialog



class MyMessenger:
    def __init__(self, master):
        self.client_socket = socket()
        self.selected_protocol = Tkinter.StringVar()
        self.BUFSIZ = 1024
        self.my_msg = Tkinter.StringVar()
        self.msg_list = Tkinter.Listbox()
        self.master = master
        self.ip_address = Tkinter.StringVar()
        self.port_number = Tkinter.StringVar()
        self.photo = Tkinter.PhotoImage(file="emojiler/rsz_unamused_face_emoji.png", width=20, height=20)
        self.photo2 = Tkinter.PhotoImage(file="emojiler/rsz_very_angry_emoji.png", width=20, height=20)
        self.photo3 = Tkinter.PhotoImage(file="emojiler/rsz_tears_of_joy_emoji.png", width=20, height=20)


    def receive(self):
        """Handles receiving of messages."""
        while True:
            try:
                msg = self.client_socket.recv(self.BUFSIZ).decode("utf8")
                self.msg_list.insert(Tkinter.END, msg)
            except OSError:  # Possibly client has left the chat.
                break

    def send(self, event=None):  # event is passed by binders.

        """Handles sending of messages."""
        msg = self.my_msg.get()
        self.my_msg.set("")  # Clears input field.
        self.client_socket.send(bytes(msg))
        if msg == "{quit}":
            self.client_socket.close()
            self.master.quit()

    # def send_tread(self):
    #     tr = Thread(target=self.send())
    #     tr.start()

    def on_closing(self, event=None):
        """This function is to be called when the window is closed."""
        self.my_msg.set("{quit}")
        self.send()

    def start_connection(self, event=None):
        # ----Now comes the sockets part----
        HOST = self.ip_address.get()
        PORT = self.port_number.get()

        ADDR = (HOST, int(PORT))

        try:
            self.client_socket.connect(ADDR)
        except:
            print "Please enter a valid ip address and a port number"

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        receive_thread = Thread(target=self.receive)
        receive_thread.start()

    def update_protocol(self, event=None):
        if self.selected_protocol.get() == "tcp":
            self.client_socket = socket(AF_INET, SOCK_STREAM)
        elif self.selected_protocol.get() == "udp":
            self.client_socket = socket(AF_INET, SOCK_DGRAM)
        else:
            print str(self.selected_protocol) + "Please select a valid communication protocol"

    def file_location(self):
        self.filename = tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                                     filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        print self.filename

    def gui_builder(self):
        self.master.title("Chatter")

        messages_frame = Tkinter.Frame(self.master)
        # For the messages to be sent.
        self.my_msg.set("Type your messages here.")
        scrollbar = Tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
        # Following will contain the messages.
        self.msg_list = Tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
        scrollbar.grid(column=1, row=0, sticky="NS")
        self.msg_list.grid(column=0, row=0, sticky="NSEW")

        entry_field = Tkinter.Entry(messages_frame, textvariable=self.my_msg)
        entry_field.bind("<Return>", self.send)
        entry_field.grid(column=0, row=1, sticky="EW")
        send_button = Tkinter.Button(messages_frame, text="Send", command=self.send)
        send_button.grid(column=0, row=2, sticky="EW")

        emoji_frame = Tkinter.Frame(messages_frame)
        emoji_frame.grid(column=0, row=3, sticky="EW")

        angry = Tkinter.Button(emoji_frame, image=self.photo, relief="flat")
        angry.grid(row=0, column=6)
        angry2 = Tkinter.Button(emoji_frame, image=self.photo, relief="flat")
        angry2.grid(row=0, column=7)
        angry3 = Tkinter.Button(emoji_frame, image=self.photo, relief="flat")
        angry3.grid(row=0, column=8)
        angry4 = Tkinter.Button(emoji_frame, image=self.photo, relief="flat")
        angry4.grid(row=1, column=6)
        angry5 = Tkinter.Button(emoji_frame, image=self.photo, relief="flat")
        angry5.grid(row=1, column=7)
        angry6 = Tkinter.Button(emoji_frame, image=self.photo, relief="flat")
        angry6.grid(row=1, column=8)

        happy = Tkinter.Button(emoji_frame, image=self.photo2, relief="flat")
        happy.grid(row=0, column=0)
        happy2 = Tkinter.Button(emoji_frame, image=self.photo2, relief="flat")
        happy2.grid(row=0, column=1)
        happy3 = Tkinter.Button(emoji_frame, image=self.photo2, relief="flat")
        happy3.grid(row=0, column=2)
        happy4 = Tkinter.Button(emoji_frame, image=self.photo2, relief="flat")
        happy4.grid(row=0, column=3)
        happy5 = Tkinter.Button(emoji_frame, image=self.photo2, relief="flat")
        happy5.grid(row=0, column=4)
        happy6 = Tkinter.Button(emoji_frame, image=self.photo2, relief="flat")
        happy6.grid(row=0, column=5)

        face = Tkinter.Button(emoji_frame, image=self.photo3, relief="flat")
        face.grid(row=1, column=0)
        face2 = Tkinter.Button(emoji_frame, image=self.photo3, relief="flat")
        face2.grid(row=1, column=1)
        face3 = Tkinter.Button(emoji_frame, image=self.photo3, relief="flat")
        face3.grid(row=1, column=2)
        face4 = Tkinter.Button(emoji_frame, image=self.photo3, relief="flat")
        face4.grid(row=1, column=3)
        face5 = Tkinter.Button(emoji_frame, image=self.photo3, relief="flat")
        face5.grid(row=1, column=4)
        face6 = Tkinter.Button(emoji_frame, image=self.photo3, relief="flat")
        face6.grid(row=1, column=5)
        messages_frame.grid(row=0, column=0)

        settings_frame = Tkinter.Frame(self.master)

        protocol_frame = Tkinter.Frame(settings_frame)

        udp_button = Tkinter.Radiobutton(settings_frame, text="UDP", variable=self.selected_protocol, value="udp",
                                         command=self.update_protocol)
        udp_button.grid(row=0, column=0)
        tcp_button = Tkinter.Radiobutton(settings_frame, text="TCP", variable=self.selected_protocol, value="tcp",
                                         command=self.update_protocol)
        tcp_button.grid(row=0, column=1)

        self.ip_address.set("Enter IP address")
        ip_field = Tkinter.Entry(settings_frame, textvariable=self.ip_address)
        ip_field.grid(column=0, row=1, columnspan=2, sticky="EW")

        self.port_number.set("Enter Port number")
        port_field = Tkinter.Entry(settings_frame, textvariable=self.port_number)
        port_field.grid(column=0, row=2, columnspan=2, sticky="EW")

        start_connection_button = Tkinter.Button(settings_frame, text="Start Connection", command=self.start_connection,
                                                 relief="ridge")
        start_connection_button.grid(row=3, column=0, columnspan=2, sticky="EW")

        send_file_button = Tkinter.Button(settings_frame, text="Send File", relief="ridge",
                                          command=lambda: self.file_location())
        send_file_button.grid(row=4, column=0, columnspan=2, sticky="EW")

        protocol_frame.grid(row=1, column=0, padx=10)
        settings_frame.grid(row=0, column=1, padx=10)


top = Tkinter.Tk()
deneme = MyMessenger(top)
deneme.gui_builder()
# gui_tread = Thread(target=)
# gui_tread.start()
top.mainloop()

