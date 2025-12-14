import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

clients = {}
clients_lock = threading.Lock()


def broadcast(message, exclude_conn=None):
	with clients_lock:
		for conn in list(clients.keys()):
			if conn is exclude_conn:
				continue
			try:
				conn.sendall(message.encode('utf-8'))
			except Exception:
				# If send fails, remove client
				remove_client(conn)


def remove_client(conn):
	with clients_lock:
		name = clients.pop(conn, None)
	try:
		conn.close()
	except Exception:
		pass
	if name:
		broadcast(f'-- {name} has left the chat --')


def handle_client(conn, addr):
	try:
		# First message should be the client's display name
		name_data = conn.recv(1024)
		if not name_data:
			conn.close()
			return
		name = name_data.decode('utf-8').strip()
		with clients_lock:
			clients[conn] = name
		broadcast(f'-- {name} has joined the chat --')

		while True:
			data = conn.recv(1024)
			if not data:
				break
			text = data.decode('utf-8').strip()
			if text == '/quit':
				break
			broadcast(f'{name}: {text}', exclude_conn=conn)
	except Exception:
		pass
	finally:
		remove_client(conn)


def run_server(host=HOST, port=PORT):
	print(f'Starting chat server on {host}:{port}...')
	server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_sock.bind((host, port))
	server_sock.listen()
	try:
		while True:
			conn, addr = server_sock.accept()
			thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
			thread.start()
	except KeyboardInterrupt:
		print('\nShutting down server...')
	finally:
		with clients_lock:
			for conn in list(clients.keys()):
				try:
					conn.sendall('Server is shutting down.'.encode('utf-8'))
				except Exception:
					pass
				try:
					conn.close()
				except Exception:
					pass
		server_sock.close()


if __name__ == '__main__':
	run_server()

