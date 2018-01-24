"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM, gethostbyaddr, SOCK_DGRAM
from threading import Thread


def udp_incoming_connections():
    while True:
        client, client_address = SERVER.recvfrom(BUFSIZ)
        SERVER.sendto("welcome bro! please enter your nick name", client_address)


def tcp_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Greetings from the cave! Now type your name and press enter!"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg == bytes("{quit}"):
            client.send(bytes("{quit}"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name))
            break
        elif msg[0:7] == bytes("{emoji}"):
            broadcast(msg, "")
        else:
            broadcast(msg, name + ": ")


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix) + msg)


clients = {}
addresses = {}

selected_protocol = input("Select a protocol [TCP|UDP]: ")
if selected_protocol == "TCP":
    HOST = gethostbyaddr(input("Enter Ip Address: "))[0]
    PORT = 4000
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    SERVER = socket(AF_INET, SOCK_STREAM)
    SERVER.bind(ADDR)

    if __name__ == "__main__":
        SERVER.listen(5)
        print("Waiting for connection...")
        ACCEPT_THREAD = Thread(target=accept_incoming_connections)
        ACCEPT_THREAD.start()
        ACCEPT_THREAD.join()
        SERVER.close()
elif selected_protocol == "UDP":
    print "udp selected"
    HOST = gethostbyaddr(input("Enter Ip Address: "))[0]
    PORT = 4000
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    SERVER = socket(AF_INET, SOCK_DGRAM)
    SERVER.bind(ADDR)

    if __name__ == "__main__":
        print("Waiting for connection...")
        ACCEPT_THREAD = Thread(target=accept_incoming_connections)
        ACCEPT_THREAD.start()
        ACCEPT_THREAD.join()
        SERVER.close()
else:
    print "Invalid protocol! Please try again later..."
