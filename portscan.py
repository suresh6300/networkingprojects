import socket
import subprocess
import sys

from datetime import datetime

#blank your screen
#subprocess.call('clear',shell=True)

#ask for input
remoteServer=input("enter a remote host to scan:")
remoteServerIP = socket.gethostbyname(remoteServer)
 #print a nice banner with information on which host we are about to scan
print("-" *60)
print("please wait,scanning remote host", remoteServerIP)
print("-" *60)

#check the date and time the scan was started
t1=datetime.now()
#using the range function to specify ports
#also we will do error handling


try:
    for port in range(1,5000):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#AF_INET :: IPV4, AF_INET6 :: IPV6 
        result = sock.connect_ex((remoteServerIP, port))#remoteserver check from first port if it is true or false
        #socket[Low level implementation] :: connect() ---> not a python implementation || c implementation 
        #socket :: connect_ex() ---> python implementation :: error indicators 
        if result == 0:
            print("port {}:          open".format(port))
            sock.close()
except KeyboardInterrupt:
    print("you pressed Ctrl+C")
    sys.exit()
except socket.gaierror:
    print("hostname could not be resolved. existing")
    sys.exit()
except socket.error:
    print("couldn't connect to server")
    sys.exit()
    