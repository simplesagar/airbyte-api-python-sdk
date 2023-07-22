"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceXeroAuthenticateViaXeroOAuth:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Enter your Xero application's access token"""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""Enter your Xero application's Client ID"""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""Enter your Xero application's Client Secret"""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""Enter your Xero application's refresh token"""
    token_expiry_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_expiry_date') }})
    r"""The date-time when the access token should be refreshed"""
    


class SourceXeroXero(str, Enum):
    XERO = 'xero'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceXero:
    r"""The values required to configure the source."""
    authentication: SourceXeroAuthenticateViaXeroOAuth = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authentication') }})
    source_type: SourceXeroXero = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""UTC date and time in the format YYYY-MM-DDTHH:mm:ssZ. Any data with created_at before this data will not be synced."""
    tenant_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tenant_id') }})
    r"""Enter your Xero organization's Tenant ID"""
    

