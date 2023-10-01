"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Final, Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationVerticaSSHTunnelMethodPasswordAuthentication:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host"""
    tunnel_user_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user_password') }})
    r"""OS-level password for logging into the jump server host"""
    TUNNEL_METHOD: Final[str] = dataclasses.field(default='SSH_PASSWORD_AUTH', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and password authentication"""
    tunnel_port: Optional[int] = dataclasses.field(default=22, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port'), 'exclude': lambda f: f is None }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationVerticaSSHTunnelMethodSSHKeyAuthentication:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    ssh_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssh_key') }})
    r"""OS-level user account ssh key credentials in RSA PEM format ( created with ssh-keygen -t rsa -m PEM -f myuser_rsa )"""
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host."""
    TUNNEL_METHOD: Final[str] = dataclasses.field(default='SSH_KEY_AUTH', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and ssh key"""
    tunnel_port: Optional[int] = dataclasses.field(default=22, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port'), 'exclude': lambda f: f is None }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationVerticaSSHTunnelMethodNoTunnel:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    TUNNEL_METHOD: Final[str] = dataclasses.field(default='NO_TUNNEL', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""No ssh tunnel needed to connect to database"""
    




@dataclasses.dataclass
class DestinationVerticaSSHTunnelMethod:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationVertica:
    r"""The values required to configure the destination."""
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    r"""Name of the database."""
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""Hostname of the database."""
    schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema') }})
    r"""Schema for vertica destination"""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Username to use to access the database."""
    DESTINATION_TYPE: Final[str] = dataclasses.field(default='vertica', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    jdbc_url_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jdbc_url_params'), 'exclude': lambda f: f is None }})
    r"""Additional properties to pass to the JDBC URL string when connecting to the database formatted as 'key=value' pairs separated by the symbol '&'. (example: key1=value1&key2=value2&key3=value3)."""
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""Password associated with the username."""
    port: Optional[int] = dataclasses.field(default=5433, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    r"""Port of the database."""
    tunnel_method: Optional[Union[DestinationVerticaSSHTunnelMethodNoTunnel, DestinationVerticaSSHTunnelMethodSSHKeyAuthentication, DestinationVerticaSSHTunnelMethodPasswordAuthentication]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method'), 'exclude': lambda f: f is None }})
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    

