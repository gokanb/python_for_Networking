#!/usr/bin/env python3
"""Educational packet sniffer built on scapy.

Prompts for an interface, a packet count, a timeout, and an optional protocol
filter (arp / bootp / icmp), then captures packets and logs their timestamp and
source/destination MAC addresses to a file.

Requires root privileges and a real network interface, so it is meant to be run
on a Linux host, not in a sandbox.
"""

import logging
import subprocess
import sys
from datetime import datetime

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

try:
    from scapy.all import sniff
except ImportError:
    print("scapy is not installed. Install it with: pip install scapy")
    sys.exit(1)


def build_logger(log_file, protocol):
    """Return a callback that writes one line per captured packet."""
    def log_packet(packet):
        timestamp = datetime.now()
        label = "ALL" if protocol == "0" else protocol.upper()
        src = packet[0].src
        dst = packet[0].dst
        with open(log_file, "a", encoding="utf-8") as fh:
            fh.write(f"Time: {timestamp}  Protocol: {label}  SMAC: {src}  DMAC: {dst}\n")
    return log_packet


def main():
    print("This sniffer must run with root privileges.")
    interface = input("Interface to sniff on (e.g. eth0): ").strip()

    # Put the interface into promiscuous mode so it sees all traffic.
    subprocess.call(["ifconfig", interface, "promisc"])

    count = int(input("Number of packets to capture (0 = until timeout): ") or "0")
    timeout = int(input("Seconds to run the capture (0 = no limit): ") or "0")
    protocol = input("Protocol filter (arp | bootp | icmp | 0 for all): ").strip() or "0"
    log_file = input("Log file name: ").strip() or "capture.log"

    print("\nStarting capture...")
    callback = build_logger(log_file, protocol)

    if protocol == "0":
        sniff(iface=interface, count=count, timeout=timeout, prn=callback)
    elif protocol in ("arp", "bootp", "icmp"):
        sniff(iface=interface, filter=protocol, count=count, timeout=timeout, prn=callback)
    else:
        print("Unknown protocol.")
        sys.exit(1)

    print(f"\nDone. See '{log_file}' for the captured packets.")


if __name__ == "__main__":
    main()
