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

def main():
    hostname = "127.0.0.1"
    port = 5000
    s=socket.socket()
    s.connect((hostname,port))
    message= input("input message -->")

    while message != 'q':
        s.send(message)
        data=s.recv()
        print (data)
        message= input("input message -->")

    s.close()


if __name__ == '__main__':
    main()
