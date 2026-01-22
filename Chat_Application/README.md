##  Simple console Client Chat Application using Python
This is a Python-based Simple console client chat application built using socket programming and multithreading.  
The project follows a client–server architecture where multiple clients can connect to a server and communicate with each other in real time.

## Files
- Server: listens for clients and broadcasts messages.
- Client: console client to join the chat and send/receive messages.

## Examples
python Server.py
python Client.py 127.0.0.1 5000

## Notes
- This is a simple demonstration using TCP sockets and threads; it's suitable for LAN/local testing.
- For production use, consider message framing, authentication, encryption (TLS), and robust error handling.

## 🛠️ Tech Stack
- Python 3.x
- socket
- threading
- sys

## 📂 Project Structure

chat-app/ │── server.py │── client.py │── README.md
