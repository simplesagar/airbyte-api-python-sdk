"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceOktaCredentialsAPITokenAuthType(str, Enum):
    API_TOKEN = 'api_token'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOktaCredentialsAPIToken:
    
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    r"""An Okta token. See the <a href=\\"https://docs.airbyte.com/integrations/sources/okta\\">docs</a> for instructions on how to generate it."""
    auth_type: SourceOktaCredentialsAPITokenAuthType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    
class SourceOktaCredentialsOAuth20AuthType(str, Enum):
    OAUTH2_0 = 'oauth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOktaCredentialsOAuth20:
    
    auth_type: SourceOktaCredentialsOAuth20AuthType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of your OAuth application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Client Secret of your OAuth application."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""Refresh Token to obtain new Access Token, when it's expired."""
    
class SourceOktaOkta(str, Enum):
    OKTA = 'okta'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOkta:
    r"""The values required to configure the source."""
    
    source_type: SourceOktaOkta = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    domain: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain'), 'exclude': lambda f: f is None }})
    r"""The Okta domain. See the <a href=\\"https://docs.airbyte.com/integrations/sources/okta\\">docs</a> for instructions on how to find it."""
    start_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'exclude': lambda f: f is None }})
    r"""UTC date and time in the format YYYY-MM-DDTHH:MM:SSZ. Any data before this date will not be replicated."""
    