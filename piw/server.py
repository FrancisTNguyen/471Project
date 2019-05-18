import socket
import os
import sys
import glob

# gets port from start of code
port = sys.argv[1]
port = int(port, 10)

# this binds the port to the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', port))


# is listening for the client to connect
s.listen(1)
print("waiting on client, why dont you run it in another terminal?")

clientsocket, address = s.accept()
print("client has connected at address - ", address)

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

    #grabbing the command
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

        # Grabs the GET command from the client, max bytes of 500
        grabText = clientsocket.recv(1024)
        # grab the file

        # opens file, then reads it in
        fileText = open(grabText, 'rb')
        fileRead = fileText.read()

        fileSize = len(fileRead)
        clientsocket.send(str(fileSize).encode("utf-8"))

        # access socket
        s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s2.bind(('', 0))

        ephemPort = s2.getsockname()[1]

        ephemPort = str(ephemPort).encode("utf-8")
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

    if PUT in choice:
        #need to grab the file name from client
        grabPutText = clientsocket.recv(1024)
        grabputText = grabPutText.decode("utf-8")

        #need to grab the file size from client
        fileSize = clientsocket.recv(1024)
        #need to read the file with while loop
        s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s3.bind(('', 0))
        ephemPort = s3.getsockname()[1]
        ephemPort = str(ephemPort).encode("utf-8")
        clientsocket.send(ephemPort)
        s3.listen(1)

        fileText, address = s3.accept()

        fileGet = recvAll(fileText, int(fileSize))

        fileVar = open(grabPutText, "wb")
        fileVar.write(fileGet.encode("utf-8"))

        #close
        fileText.close()
        fileVar.close()


    # if LS in choice:
    #     filename = request.split('|')[1]
    #     filepath = "%s%s%s" % ('./uploads', '/', filename)
    #     os.listdir(filepath)
