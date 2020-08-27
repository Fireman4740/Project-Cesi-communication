import socket

hote = "localhost"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))
nbpacket = 8
msg='0011200221'
msg_a_envoyer = b""
while nbpacket != 0:

      nbpacket  -= 1
      if msg_a_envoyer == b"fin":
          print("Fermeture de la connexion")
          connexion_avec_serveur.close()
      else:
          for i in range(1):
              msg_a_envoyer =msg
    
             # Peut planter si vous tapez des caractères spéciaux
              msg_a_envoyer = msg_a_envoyer.encode()
              # On envoie le message
              connexion_avec_serveur.send(msg_a_envoyer)
              msg_recu = connexion_avec_serveur.recv(1024)

              print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents


