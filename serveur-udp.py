
import socket

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024

# Create a datagram socket
connexion_principale= socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
connexion_principale.bind((localIP, localPort))
print("UDP server up and listening") 
# Listen for incoming datagrams
msg_recu = b""
while msg_recu != b"fin":
      

      bytesAddressPair = connexion_principale.recvfrom(bufferSize)

      message = bytesAddressPair[0]

      address = bytesAddressPair[1]

      clientMsg = "Message from Client:{}".format(message)
      clientIP  = "Client IP Address:{}".format(address)
    
      print(clientMsg)
      print(clientIP)
      
connexion_avec_client.close()
connexion_principale.close()


