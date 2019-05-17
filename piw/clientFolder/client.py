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


while True:
    
    choice = input("FTP: ")
    
    if choice == "quit":
        chh = choice[0:4].encode("utf-8")
        s.send(chh)
        s.close()
        break

    if choice == "get":
        sentCMD = choice[0:4].encode("utf-8")
        s.send(sentCMD)
        
        fileSent = choice[5:]
        fileSent = fileSent.encode("utf-8")
        s.send(fileSent)
        print("You have requested file: ", fileText.decode("utf-8"))

        fileSize = s.recv(500)

        if "XX".encode("utf-8") in fileSize:
            print("File not found")
        else:

            newPort = s.recv(500)
            newPort = int(newPort, 10)
            newSock = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
            newSock.connect((serverAddr, ePort))

            recData = recvAll(newSock, int(fileSize))

            newFile = open(fileSent, 'wb')
            newFile.write(recData.encode("utf-8"))

            newFile.close()
            newSock.close()

