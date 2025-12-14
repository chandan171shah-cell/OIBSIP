##  Simple console Client Chat Application using Python
This is a Python-based Simple console client chat application built using socket programming and multithreading.  
The project follows a client–server architecture where multiple clients can connect to a server and communicate with each other in real time.

## Files
- Server: listens for clients and broadcasts messages.
- Client: console client to join the chat and send/receive messages.

## Usage
- Start the server (defaults to port 5000):

```Bash
python Server.py
```

- Start a client (defaults to localhost:5000):

```bash
python Client.py [host] [port]
```

## Examples

`` Bash
python Server.py
python Client.py 127.0.0.1 5000


## Controls
 Type messages and press Enter to send.
 Type `/quit` to leave the chat.

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