"""A tiny HTTP server: accept a connection, print the request, return a page."""

import socket


def main(host="localhost", port=8080):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(5)
    print(f"Listening on http://{host}:{port} (Ctrl+C to stop)")

    try:
        while True:
            client, address = sock.accept()
            print(f"Request from {address}")
            print(client.recv(1024).decode(errors="ignore"))
            body = "<html><body><h1>It works!</h1></body></html>"
            response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(body)}\r\n\r\n{body}"
            client.send(response.encode())
            client.close()   # close() takes no argument
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        sock.close()


if __name__ == "__main__":
    main()
