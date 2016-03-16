import socket
import sys

#TCP/IP soket olusturuluyor
'''
    socket.AF_INET =A pair (host, port)
    socket.SOCK_STREAM = socket type
'''

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# soket port'a bind ediliyor
server_address = ('localhost', 10000)
print(sys.stderr, "port %s port %s adresinden  baslatiliyor " % server_address)
my_socket.bind(server_address)

my_socket.listen(2)
print(sys.stderr, "baglanti bekleniyor")
connection, client_address = my_socket.accept()
while True:

    try:
        print(sys.stderr, client_address)
        while True:
            data = connection.recv(1024)
            print(sys.stderr, " %s data geldi" % data)
            if data:
                print(sys.stderr, " gelen data clientlara gonderildi")
                connection.sendall(data)
            else:
                print(sys.stderr, client_address)
                break
    finally:
        connection.close()

