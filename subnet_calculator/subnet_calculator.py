"""Subnet calculator.

Takes an IPv4 address and a subnet mask and works out, using manual binary
math (the way you'd do it by hand studying for a networking exam):

    - the network address
    - the broadcast address
    - the number of usable hosts
    - the wildcard mask
    - the prefix length (mask bits)

It can also generate a random valid host address inside the subnet.

Run it interactively:
    python subnet_calculator.py

Or import ``calculate_subnet(ip, mask)`` and use the returned dictionary.
"""

import random
import sys


VALID_MASK_OCTETS = {0, 128, 192, 224, 240, 248, 252, 254, 255}


def is_valid_ip(ip):
    """Return True if ``ip`` is a syntactically valid IPv4 address."""
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False
    return True


def is_valid_mask(mask):
    """Return True if ``mask`` is a valid, contiguous subnet mask."""
    parts = mask.split(".")
    if len(parts) != 4 or not all(p.isdigit() for p in parts):
        return False
    octets = [int(p) for p in parts]
    if any(o not in VALID_MASK_OCTETS for o in octets):
        return False
    # A real mask is all 1s then all 0s, so octets never increase.
    return octets[0] >= octets[1] >= octets[2] >= octets[3]


def to_binary_string(dotted):
    """Convert a dotted-decimal address to a 32-character binary string."""
    return "".join(format(int(octet), "08b") for octet in dotted.split("."))


def binary_to_dotted(binary):
    """Convert a 32-character binary string back to dotted decimal."""
    octets = [str(int(binary[i:i + 8], 2)) for i in range(0, 32, 8)]
    return ".".join(octets)


def calculate_subnet(ip, mask):
    """Calculate subnet details for an IP/mask pair.

    Returns a dict with network, broadcast, host count, wildcard mask,
    and prefix length. Raises ValueError on invalid input.
    """
    if not is_valid_ip(ip):
        raise ValueError(f"Invalid IP address: {ip}")
    if not is_valid_mask(mask):
        raise ValueError(f"Invalid subnet mask: {mask}")

    mask_binary = to_binary_string(mask)
    ip_binary = to_binary_string(ip)

    ones = mask_binary.count("1")        # prefix length (e.g. 24)
    zeros = mask_binary.count("0")       # host bits

    # Usable hosts = 2^(host bits) - 2, but never negative (/31, /32).
    usable_hosts = max(2 ** zeros - 2, 0)

    # Network = IP's network bits + all zeros; broadcast = + all ones.
    network_binary = ip_binary[:ones] + "0" * zeros
    broadcast_binary = ip_binary[:ones] + "1" * zeros

    # Wildcard mask is the bitwise inverse of the subnet mask.
    wildcard = ".".join(str(255 - int(o)) for o in mask.split("."))

    return {
        "network": binary_to_dotted(network_binary),
        "broadcast": binary_to_dotted(broadcast_binary),
        "usable_hosts": usable_hosts,
        "wildcard": wildcard,
        "prefix": ones,
    }


def random_host_in_subnet(ip, mask):
    """Return a random host address inside the given subnet."""
    result = calculate_subnet(ip, mask)
    net_octets = [int(o) for o in result["network"].split(".")]
    bc_octets = [int(o) for o in result["broadcast"].split(".")]
    host = [str(random.randint(lo, hi)) for lo, hi in zip(net_octets, bc_octets)]
    return ".".join(host)


def _prompt_valid(prompt, validator):
    """Keep prompting until the input passes ``validator``."""
    while True:
        value = input(prompt).strip()
        if validator(value):
            return value
        print("  [-] Invalid input, please try again.")


def main():
    try:
        ip = _prompt_valid("Enter an IP address: ", is_valid_ip)
        mask = _prompt_valid("Enter a subnet mask: ", is_valid_mask)
        result = calculate_subnet(ip, mask)

        print()
        print(f"Network address  : {result['network']}")
        print(f"Broadcast address: {result['broadcast']}")
        print(f"Usable hosts     : {result['usable_hosts']}")
        print(f"Wildcard mask    : {result['wildcard']}")
        print(f"Prefix length    : /{result['prefix']}")
        print()

        if input("Generate a random host in this subnet? (y/n) ").strip().lower() == "y":
            print(f"Random host: {random_host_in_subnet(ip, mask)}")
    except KeyboardInterrupt:
        print("\nAborted by user.")
        sys.exit()


if __name__ == "__main__":
    main()
