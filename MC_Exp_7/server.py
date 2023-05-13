import kthread #pip install kthread
from time import sleep
import subprocess
import socket
def getips():
    ipadressen = {}
    def ping(ipadresse):
        try:
            outputcap = subprocess.run([f'ping', ipadresse, '-n', '1'], capture_output=True) #sends only one package, faster
            print(outputcap)
            ipadressen[ipadresse] = outputcap
        except Exception as Fehler:
            print(Fehler)
    t = [kthread.KThread(target = ping, name = f"ipgetter{ipend}", args=(f'192.168.215.{ipend}',)) for ipend in range(255)] #prepares threads
    [kk.start() for kk in t] #starts 255 threads
    while len(ipadressen) < 255:
        print('Searching network')
        sleep(.3)
    alldevices = []
    for key, item in ipadressen.items():
        if not 'unreachable' in item.stdout.decode('utf-8') and 'failure' not in item.stdout.decode('utf-8'): #checks if there wasn't neither general failure nor 'unrechable host'
            alldevices.append(key)
    return alldevices

allips = getips() 
print(allips)
# print(socket.gethostbyaddr(allips[0]))
import socket
import os
from _thread import *
ServerSideSocket = socket.socket()
# host = '192.168.1.5'
# host='192.168.215.69'
host='192.168.1.3' #put your machine ip address
port = 2004

ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)
def multi_threaded_client(connection):
    # connection.send(str.encode('Server is working:'))
    while True:
        # data = connection.recv(2048)
        data=input("Enter Message to Broadcast")
        # data="serverWorking"
        # response = 'Server message: ' + data
        if not data:
            break
        connection.sendall(str.encode(data))
    connection.close()
while True:
    Client, address = ServerSideSocket.accept()
    print(address)
    # ch=input(f"{socket.gethostbyaddr(address[0])[0]} wants to join \nPress ENTER to Accept And N to Reject")
    # if ch=='N'or'n':
    #     print("Connection Rejected")

    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()
