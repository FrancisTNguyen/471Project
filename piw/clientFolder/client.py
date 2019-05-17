#client
#Thomas Smith

import socket
import os
import sys




#gets server address and port
address = sys.argv[1]
port = sys.argv[2]
port = int(port, 10)


#creates the connection socket on address and port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((address, port))

cmdsock = ''

while True:
    
    choice = input("FTP: ")
    
    print(choice)
    
    if choice == "quit":
        chh = choice[0:4].encode("utf-8")
        s.send(chh)
        s.close()
        break


   