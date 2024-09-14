from enum import Enum

class IpAddressType(str, Enum):
    ipv4 = 'IPv4'
    ipv6 = 'IPv6'
