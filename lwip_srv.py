import signal
import socket
import sys

USE_UDP = 1

def main():
	recvbyte = 0

	# Set signal handler for printing nrecvdata.
	signal.signal(signal.SIGINT, lambda signum, frame: print(recvbyte))

	# Set signal handler for clearing recvbyte.
	def clear_recvdata_byte(signum, frame):
		nonlocal recvbyte
		recvbyte = 0
	signal.signal(signal.SIGTSTP, clear_recvdata_byte)

	ADDR_PORT = ('', int(sys.argv[1]))	# (INADDR_ANY, port)

	if USE_UDP:
		sock_srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock_srv.bind(ADDR_PORT)
	else:
		sock_srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock_srv.bind(ADDR_PORT)
		sock_srv.listen()
		sock_cli, addr = sock_srv.accept()

	while True:
		if USE_UDP:
			# recvdata = sock_srv.recv(1472)
			recvdata, addrport = sock_srv.recvfrom(1472)
		else:
			recvdata = sock_cli.recv(1460)
		recvbyte += len(recvdata)
		print(addrport)

if __name__ == '__main__':
	main()
