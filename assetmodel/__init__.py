from __future__ import annotations
from importlib import import_module
import typing

if typing.TYPE_CHECKING:
    from .registration.autnum_record import AutnumRecord
    from .autonomous_system import AutonomousSystem
    from .registration.domain_record import DomainRecord
    from .fingerprint import Fingerprint
    from .domain.fqdn import FQDN
    from .network.ipv4_address import IPv4Address
    from .network.ipv4_netblock import IPv4Netblock
    from .network.ipv6_address import IPv6Address
    from .network.ipv6_netblock import IPv6Netblock
    from .network_endpoint import NetworkEndpoint
    from .organization import Organization
    from .service import Service
    from .socket_address import SocketAddress
    from .source import Source
    from .tls_certificate import TlsCertificate

__all__ = (
    'AutnumRecord',
    'AutonomousSystem',
    'DomainRecord',
    'Fingerprint',
    'FQDN',
    'IPv4Address',
    'IPv4Netblock',
    'IPv6Address',
    'IPv6Netblock',
    'NetworkEndpoint',
    'Organization',
    'Service',
    'SocketAddress',
    'Source',
    'TlsCertificate'
)

# A mapping of {<member name>: (package, <module name>)} defining dynamic imports
_dynamic_imports: 'dict[str, tuple[str, str]]' = {
    'AutnumRecord': (__spec__.parent, '.registration.autnum_record'),
    'AutonomousSystem': (__spec__.parent, '.autonomous_system'),
    'DomainRecord': (__spec__.parent, '.registration.domain_record'),
    'Fingerprint': (__spec__.parent, '.fingerprint'),
    'FQDN': (__spec__.parent, '.domain.fqdn'),
    'IPv4Address': (__spec__.parent, '.network.ipv4_address'),
    'IPv4Netblock': (__spec__.parent, '.network.ipv4_netblock'),
    'IPv6Address': (__spec__.parent, '.network.ipv6_address'),
    'IPv6Netblock': (__spec__.parent, '.network.ipv6_netblock'),
    'NetworkEndpoint': (__spec__.parent, 'network_endpoint'),
    'Organization': (__spec__.parent, '.organization'),
    'Service': (__spec__.parent, '.service'),
    'SocketAddress': (__spec__.parent, '.socket_address'),
    'Source': (__spec__.parent, '.source'),
    'TlsCertificate': (__spec__.parent, '.tls_certificate')
}

def __getattr__(attr_name: str) -> object:
    dynamic_attr = _dynamic_imports.get(attr_name)

    package, module_name = dynamic_attr

    if module_name == '__module__':
        result = import_module(f'.{attr_name}', package=package)
        globals()[attr_name] = result
        return result
    else:
        module = import_module(module_name, package=package)
        result = getattr(module, attr_name)
        g = globals()
        for k, (_, v_module_name) in _dynamic_imports.items():
            if v_module_name == module_name:
                g[k] = getattr(module, k)
        return result

def __dir__() -> 'list[str]':
    return list(__all__)