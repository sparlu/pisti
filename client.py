import socket
import sys

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ='localhost'
port=10000
server_address = (host,port)
print(sys.stderr, "%s baglanti %s port" % server_address)
my_socket.connect(server_address)
while(1):
    mesaj = input('mesajınızı giriniz : ')
    try:

            gond = bytes(mesaj,"utf-8")
            my_socket.sendto(gond, (host,port))


            alinan_mesaj = 0
            gelen_mesaj = len(mesaj)
            while alinan_mesaj<gelen_mesaj:
                data = my_socket.recv(1024)
                gelen_mesaj += len(data)
                print(sys.stderr, "%s" %data)

    finally:
        print(sys.stderr, 'soket kapatilacak')
        my_socket.close()

