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
socket.getaddrinfo('localhost', 8080)
s.connect((address, port))


def recvAll(sock, numBytes):

    # Initialize buffers
    recvBuff = ""
    tmpBuff = ""

    # Loop until the buffer is greater than number of bytes total
    while len(recvBuff) < numBytes:

        # Receive 65536 bytes of data
        tmpBuff = sock.recv(65536)

        # Check if all the data has been sent
        if not tmpBuff:
            break

        # Append the data to itself
        recvBuff += tmpBuff.decode("utf-8")

    # Return the data
    return recvBuff



while True:
    
    choice = input("FTP: ")
    
    if choice == "quit":
        chh = choice[0:4].encode("utf-8")
        s.send(chh)
        s.close()
        break

    elif "get" in choice:
    
        sentCMD = choice[0:3].encode("utf-8")
        s.send(sentCMD)
        
        fileSent = choice[4:]
        fileSent = fileSent.encode("utf-8")
        s.send(fileSent)
        print("You have requested file: ", fileSent.decode("utf-8"))

        fileSize = s.recv(1024)

        if "XX".encode("utf-8") in fileSize:
            print("File not found")
        else:

            newPort = s.recv(32)
            newPort = int(newPort,10)
            newSock = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
            newSock.connect((address, newPort))

            recData = recvAll(newSock, int(fileSize))

            newFile = open(fileSent, 'wb')
            newFile.write(recData.encode("utf-8"))

            newFile.close()
            newSock.close()

