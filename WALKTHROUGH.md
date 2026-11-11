# Code Walkthrough — python-network-toolkit

A study guide to the code, grouped by folder. The subnet calculator gets the
most detail because it's the centerpiece; the smaller scripts get a short note
each, including the bugs that were fixed.

## subnet_calculator/subnet_calculator.py

The goal: given an IP and a subnet mask, work out the network, broadcast,
host count, wildcard mask, and prefix length — doing the binary math by hand.

**Validation.** `is_valid_ip` checks four numeric octets in 0–255.
`is_valid_mask` additionally checks each octet is one of the eight legal mask
values (255, 254, 252, …, 0) and that octets never increase — a real mask is a
run of 1-bits followed by 0-bits, so `255.255.0.255` is rejected.

**The core.** `calculate_subnet`:
```python
mask_binary = to_binary_string(mask)   # "255.255.255.0" -> "11111111111111111111111100000000"
ip_binary   = to_binary_string(ip)
ones  = mask_binary.count("1")         # prefix length, e.g. 24
zeros = mask_binary.count("0")         # host bits, e.g. 8
usable_hosts = max(2 ** zeros - 2, 0)  # minus network + broadcast; never negative
network_binary   = ip_binary[:ones] + "0" * zeros   # host bits -> 0
broadcast_binary = ip_binary[:ones] + "1" * zeros   # host bits -> 1
wildcard = ".".join(str(255 - int(o)) for o in mask.split("."))
```
`binary_to_dotted` converts the 32-bit strings back to dotted decimal by
slicing into four 8-bit chunks.

> **What was wrong before:** the old version built the network address by looping
> over `net_ip_octet` (a single leftover octet from a previous loop) instead of
> the list `net_ip_octets`, so it iterated the characters of one octet and
> produced a wrong network address. The rewrite is checked against Python's
> `ipaddress` module to guarantee correctness.

`random_host_in_subnet` picks a random value between the network and broadcast
octets — a handy way to get a valid address inside the range.

## socket_examples/

- **tcp_client.py** — opens a TCP socket to a web host, sends a raw HTTP GET, prints the reply. *Fix: the old code called `socket.close(0)` (the module) instead of `sock.close()` (the socket object).*
- **http_server.py** — binds a socket, accepts connections, and returns a small HTML page. *Fixes: `client.close()` took a bogus argument before; also added `SO_REUSEADDR` and a proper `Content-Length` header.*
- **http_client_test.py** — a tiny client to test the server.
- **port_check.py** — uses `connect_ex` to report whether each port in a list is open.

## packet_sniffer/sniffer.py

Uses scapy's `sniff()` to capture packets and a callback to log each packet's
timestamp and source/destination MAC to a file. It puts the interface into
promiscuous mode first. Needs root and a real NIC. *Cleanups: the scapy import
failure is handled gracefully, and the per-packet log uses a `with open(...)`
block instead of a dangling file handle.*

## system_utils/

Small standard-library exercises, each fixed to run:

- **host_info.py** — hostname, IP, and RAM usage via `psutil`; reverse-DNS lookup is wrapped in `try/except` because it fails on addresses with no PTR record.
- **threading_demo.py** — starts several threads. *Fix: the old code wrote `Thread(target=worker(n))`, which **called** the function on the main thread; it now passes `target=worker, args=(n,)` so the work actually runs on a new thread.*
- **argv_info.py** — prints argument info. *Fix: color names were accidentally glued into the f-strings (`f'...' 'yellow'`) and `'orange'` isn't a valid color; each argument is now printed safely in a loop.*
- **file_listing.py** — lists the current directory. *Fix: it referenced an undefined variable `files`; now uses the loop variable.*
- **file_exists_check.py** — checks a file exists and is readable. *Fix: used `os.R_okfile` (not a real constant); now uses `os.R_OK`, and the readability check is reachable.*
- **subprocess_demo.py** — runs `ls` two ways. *Fix: `os.system('ls , -la')` had a stray comma.*
- **ping_command_builder.py** / **python_version_info.py** — small platform/version helpers.
