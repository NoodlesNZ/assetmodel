from __future__ import annotations
from importlib import import_module
import typing

if typing.TYPE_CHECKING:
    from .autnum_record import AutnumRecord
    from .autonomous_system import AutonomousSystem
    from .domain_record import DomainRecord
    from .fingerprint import Fingerprint
    from .fqdn import FQDN
    from .ip_address import IpAddress
    from .netblock import Netblock
    from .network_endpoint import NetworkEndpoint
    from .organization import Organization
    from .service import Service
    from .socket_address import SocketAddress
    from .tls_certificate import TlsCertificate

__all__ = (
    'AutnumRecord',
    'AutonomousSystem',
    'DomainRecord',
    'Fingerprint',
    'FQDN',
    'IpAddress',
    'Netblock',
    'NetworkEndpoint',
    'Organization',
    'Service',
    'SocketAddress',
    'TlsCertificate'
)

# A mapping of {<member name>: (package, <module name>)} defining dynamic imports
_dynamic_imports: 'dict[str, tuple[str, str]]' = {
    'AutnumRecord': (__spec__.parent, '.autnum_record'),
    'AutonomousSystem': (__spec__.parent, '.autonomous_system'),
    'DomainRecord': (__spec__.parent, '.domain_record'),
    'Fingerprint': (__spec__.parent, '.fingerprint'),
    'FQDN': (__spec__.parent, '.fqdn'),
    'IpAddress': (__spec__.parent, '.ip_address'),
    'Netblock': (__spec__.parent, '.netblock'),
    'NetworkEndpoint': (__spec__.parent, 'network_endpoint'),
    'Organization': (__spec__.parent, '.organization'),
    'Service': (__spec__.parent, '.service'),
    'SocketAddress': (__spec__.parent, '.socket_address'),
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