from assetmodel import FQDN, Source, IPv4Address, DomainRecord
import ipaddress

def test_fqdn():
    fqdn = FQDN(name='example.com')

    assert fqdn.name == 'example.com'

def test_fqdn_full():
    fqdn = FQDN(name='example.com')
    fqdn.source = Source(name='Test Source', confidence=80)
    fqdn.a_record = [IPv4Address(address='192.168.0.123')]
    fqdn.ns_record = [
        FQDN(name='ns1.example.com'),
        FQDN(name='ns2.example.com')
    ]
    fqdn.mx_record = [
        FQDN(name='smtp.example.com')
    ]
    fqdn.registration = DomainRecord(name='example.com')

    assert fqdn.a_record[0].address == ipaddress.IPv4Address('192.168.0.123')
    assert fqdn.mx_record[0].name == 'smtp.example.com'
    assert fqdn.ns_record[1].name == 'ns2.example.com'