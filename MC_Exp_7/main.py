from flask import Flask,render_template,request
import socket
app=Flask(__name__)

def client_connect():
    ClientMultiSocket = socket.socket()
    host = '192.168.1.3'
    port = 2004
    print('Waiting for connection response')
    try:
        ClientMultiSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
    # res = ClientMultiSocket.recv(1024)
    # while True:
    # Input = input('Hey there: ')
    # ClientMultiSocket.send(str.encode(Input))
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))

    # ClientMultiSocket.close()
    return res.decode('utf-8')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/client',methods=['GET','POST'])
def client():
    if request.method=='POST':
        result=client_connect()
        return render_template('client.html',result=result)
    return render_template('client.html')

if __name__=="__main__":
    app.run(host='0.0.0.0')