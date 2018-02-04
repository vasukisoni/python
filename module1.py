#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kanha
#
# Created:     19/09/2014
# Copyright:   (c) kanha 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import socket

hostname = "127.0.0.1"
port = 5000

s= socket.socket()
s.bind((hostname, port))

s.listen(1)
c,addr = s.accept()

print ("Connection from " + str(addr))

def main():
    data = c.recv(1024)

    while True:

        if not data:
            break
        print ("Data recieved is --> " + data)
        data = str(data).upper()
        print ("senddata is " + data)


        s.send(data)

    s.close()

if __name__ == "__main__":
    main()
