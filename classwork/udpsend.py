import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5006
MESSAGE = "Hello, World!"

print "UDP target IP:", socket.gethostname()
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (socket.gethostname(), UDP_PORT))
