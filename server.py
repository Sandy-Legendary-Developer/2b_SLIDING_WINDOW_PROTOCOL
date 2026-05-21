import socket 

s = socket.socket() 
s.bind(('localhost', 8000)) 
s.listen(5) 

c, addr = s.accept() 

size = int(input("Enter number of frames to send: ")) 
l = list(range(size)) 
window_size = int(input("Enter Window Size: ")) 

st = 0 
i = 0 

while True: 
    while i < len(l): 
        st += window_size 
        c.send(str(l[i:st]).encode()) 
        ack = c.recv(1024).decode() 
        if ack: 
            print(ack) 
            i += window_size
