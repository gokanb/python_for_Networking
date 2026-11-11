"""Open a TCP socket to a web server, send a raw HTTP request, print the reply."""

import socket


def main(target_host="www.google.com", port=80):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Connecting to {target_host}:{port} ...")
    sock.connect((target_host, port))
    print("Connected.")

    request = f"GET / HTTP/1.1\r\nHost: {target_host}\r\n\r\n"
    sock.send(request.encode())

    data = sock.recv(4096)
    print(f"Received {len(data)} bytes")
    print(data.decode(errors="ignore")[:500])

    sock.close()   # close the socket object, not the socket module


if __name__ == "__main__":
    main()
