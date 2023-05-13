import socket 
hostMACAddress = '60:A5:E2:93:0A:C5' 
port = 5 # 3 is an arbitrary choice. However, it must match the port used by the client. 
backlog = 1 
size = 1024 
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM) 
s.bind((hostMACAddress,port)) 
s.listen(backlog) 
print("Waiting for Bluetooth Connection ... ") 
try: 
    client, address = s.accept() 
    print(f"Connected with {address}") 
    while 1: 
        data = client.recv(size) 
        if data: 
            print(data) 
    client.send(data) 
except: 
    print("Closing socket") 
    client.close() 
    s.close()