import socket
import threading
import sys


def receive_loop(sock):
	try:
		while True:
			data = sock.recv(1024)
			if not data:
				print('\n[Disconnected from server]')
				break
			print(data.decode('utf-8'))
	except Exception:
		pass
	finally:
		try:
			sock.close()
		except Exception:
			pass
		sys.exit(0)


def main():
	host = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
	port = int(sys.argv[2]) if len(sys.argv) > 2 else 5000

	name = input('Enter your name: ').strip()
	if not name:
		print('Name cannot be empty')
		return

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		sock.connect((host, port))
	except Exception as e:
		print(f'Unable to connect to {host}:{port} —', e)
		return

	# Send name as first message
	sock.sendall(name.encode('utf-8'))

	thread = threading.Thread(target=receive_loop, args=(sock,), daemon=True)
	thread.start()

	try:
		while True:
			msg = input()
			if msg.strip() == '':
				continue
			if msg == '/quit':
				try:
					sock.sendall('/quit'.encode('utf-8'))
				except Exception:
					pass
				break
			try:
				sock.sendall(msg.encode('utf-8'))
			except Exception:
				break
	except KeyboardInterrupt:
		pass
	finally:
		try:
			sock.close()
		except Exception:
			pass


if __name__ == '__main__':
	main()

