from __future__ import annotations
from importlib import import_module
import typing

if typing.TYPE_CHECKING:
    from .ip_address_type import IpAddressType
    from .netblock_type import NetblockType

__all__ = (
    'IpAddressType',
    'NetblockType'
)

print(__spec__.parent)

# A mapping of {<member name>: (package, <module name>)} defining dynamic imports
_dynamic_imports: 'dict[str, tuple[str, str]]' = {
    'IpAddressType': (__spec__.parent, '.ip_address_type'),
    'NetblockType': (__spec__.parent, '.netblock_type')
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