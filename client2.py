import socket

s = socket.socket()

ip = "127.0.0.1"
port = int(input("Friend's port: "))

s.connect((ip, port))

msg = " "

while msg != "q":
    m = input("You: ")
    s.send(m.encode())
    m2 = s.recv(1024)
    msg = m2.decode()
    print("%s : %s"%(port, msg))

print("Exiting...")
s.close()
