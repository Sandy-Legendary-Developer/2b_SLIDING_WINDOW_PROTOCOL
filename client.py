import socket 

s = socket.socket() 
s.connect(('localhost', 8000)) 

while True: 
    data = s.recv(1024).decode() 
    if not data: 
        break 
    print("Received:", data) 
    s.send("Acknowledgement received from the client".encode()) 

s.close()
