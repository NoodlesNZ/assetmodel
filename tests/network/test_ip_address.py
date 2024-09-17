from assetmodel import IPv4Address, IPv6Address
import ipaddress
from pydantic import ValidationError
import pytest

def test_ip_address_v4():
    address = '192.168.2.1'
    ip = IPv4Address(address=address)

    assert ip.address == ipaddress.IPv4Address(address)

def test_ip_address_v6():
    address = '2600:1415:18::6860:a990'
    ip = IPv6Address(address=address)

    assert ip.address == ipaddress.IPv6Address(address)

def test_invalid_ip_address_v4():
    address = '2600:1415:18::6860:a990'

    with pytest.raises(ValidationError):
        IPv4Address(address=address)