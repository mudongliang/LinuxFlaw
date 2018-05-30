import socket
r, w = socket.socketpair()
w.send(b'X' * 1024)
r.recvfrom_into(bytearray(), 1024)
