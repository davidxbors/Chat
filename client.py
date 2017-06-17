import socket

ip = "127.0.0.1"
port = 5000

print("Your port is %s..."%port)
print("Give your port to your friend so he can contact you...")

s = socket.socket()

s.bind((ip, port))

s.listen(1)

msg = " "
c, addr = s.accept()
print("You are connected with: %s"%addr[0])

while msg != "q":
    m = c.recv(1024)
    print("%s : %s"%(addr[0], m.decode()))
    msg = input("You: ")
    c.send(msg.encode())

print("Exiting...")
s.close()
