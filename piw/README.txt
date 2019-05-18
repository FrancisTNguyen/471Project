
*********
* NAMES *
*********
CPCS 471 SEC 3:
THOMAS SMITH - 888911625
FRANK YOUNG - 889546446
FRANCIS NGUYEN - 891383804

CPCS 471 SEC 2:
ANDREW LOPEZ - 889833190


*****************************
* CLIENT AND SERVER PROJECT *
*****************************

*Tested and developed on Ubuntu 14.04 LTS.

*Written in Python

*Tools and software also used:
 -Github
 -Visual Studio
 -Discord


************************************
* HOW TO RUN THE CLIENT AND SERVER *
************************************
INVOKE SERVER: python server.py <port>

INVOKE CLIENT: python client.py "localhost" <port>

FTP: put filename.txt (uploads file on server)

FTP: get filename.txt (downloads file to server)

FTP: ls (lists all the files on server)

FTP: quit (exits the sever)


*******************
* PROTOCOL DESIGN *
*******************

1) What kinds of messages will be exchanged across the control channel?

	get - gets fies from server
	put - sends files to the server
	ls - lists the files on the server
	quit - closes the server

2) How should the other side respond to the messages?

	get - server will be sent the filename, it will then fetch the file
	put - client will send the filename and the size of the file.
	ls - server will get the list of the al the files in the directory and the client will display it.
	quit - client closes connection with the server.

3) What sizes/formats will the messages have?
	
	size - 2^15
	formats - utf-8 encoding

4) What message exchanges have to take place in order to setup a file transfer channel?
The filename, the size of the file and what command is needed (get/put)

5) How will the receiving side know when to start/stop receiving the file?
Size of the file is sent prior to the data so the server knows when the whole file has been sent.

6) How to avoid overflowing TCP buffers?
Data size sent is limted to 2^15 bytes in each packet.

