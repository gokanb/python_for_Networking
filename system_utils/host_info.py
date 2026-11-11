"""Print basic information about the local host: name, IP, and memory usage.

Reverse-DNS lookup of an address is included as an optional demo; it is wrapped
in a try/except because it fails on hosts that have no PTR record.
"""

import socket

import psutil


def main():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print(f"Computer name: {host_name}")
    print(f"IP address   : {ip_address}")
    print(f"RAM used     : {psutil.virtual_memory().percent}%")

    # Optional reverse-DNS demo. This often fails on local addresses, so we
    # handle the error instead of letting it crash the script.
    try:
        name, aliases, addresses = socket.gethostbyaddr(ip_address)
        print(f"Reverse DNS  : {name} {aliases} {addresses}")
    except socket.herror:
        print("Reverse DNS  : no PTR record for this address.")


if __name__ == "__main__":
    main()
