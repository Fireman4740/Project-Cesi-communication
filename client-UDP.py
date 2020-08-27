import socket


serverAddressPort   = ("127.0.0.1", 20001)

bufferSize          = 1024
msg_a_envoyer = b""
msgFromClient = 'azeaze222'
bytesToSend         = str.encode(msgFromClient)

# Create a UDP socket at client side

connexion_avec_serveur = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
connexion_avec_serveur.connect((serverAddressPort))


# Send to server using created UDP socket
print("Connexion établie avec le serveur sur l'adresse et le port {}".format(serverAddressPort))


connexion_avec_serveur.sendto(bytesToSend, serverAddressPort)

msgFromServer = connexion_avec_serveur.recvfrom(bufferSize)
connexion_avec_serveur.send(msgFromClient)

msg = "Message from Server {}".format(msgFromServer[0])

print(msg)
