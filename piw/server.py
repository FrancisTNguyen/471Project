import socket
import os
import sys
import glob




#gets port from start of code
port = sys.argv[1]
port = int(port, 10)

#this binds the port to the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', port))


# is listening for the client to connect
s.listen(1)
print("waiting on client, why dont you run it in another terminal?")

clientsocket, address = s.accept()
print("client has connected at address - ", address)



while True:

    choice = clientsocket.recv(8)

    LS = "ls".encode("utf-8")
    GET = "get".encode("utf-8")
    PUT = "put".encode("utf-8")
    QUIT = "quit".encode("utf-8")

    if QUIT in choice:
        clientsocket.close()
        print("Thank you, come back soon!")
        break

    if GET in choice:
        #access socket
        s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s2.bind(('',0))
        #Grabs the GET command from the client, max bytes of 500
        grabText = clientsocket.recv(500)
        #grab the file

        #opens file, then reads it in
        fileText = open(grabText, 'rb')
        fileRead = fileText.read()
        
        fileSize = len(fileRead)
        clientsocket.send(str(fileSize).encode("utf-8"))

        ephemPort = s2.getsockname()

        ephemPort.encode("utf-8")
        clientsocket.send(ephemPort)

        s2.listen(1)
        ephemPort, address = s2.accept()

        bytesSent = 0

        while bytesSent < fileSize:
            buffer = fileRead[bytesSent:bytesSent + 500]
            ephemPort.send(buffer)
            bytesSent += 500
        
        ephemPort.close()
        fileText.close()
        print("Get is a success")
    
    # if LS in choice:
    #     filename = request.split('|')[1]
    #     filepath = "%s%s%s" % ('./uploads', '/', filename)
    #     os.listdir(filepath)





