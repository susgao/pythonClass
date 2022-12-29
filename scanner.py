#!/usr/bin/python3
import socket, sys
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1'
def basic():
	for port in range(1,100):
		r=s.connect_ex((host, port))
		if r == 0:
			print("{} port is open".format(port))
		s.close()
basic()

#def multiple():
	#host=sys.argv[1:]
	#for port in range(1,100):
		#r=s.connect_ex((host,port))
		#if r == 0:
			#print("{} is open".format(port))
