"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Any, Optional

class SourceZendeskSupportZendeskSupport(str, Enum):
    ZENDESK_SUPPORT = 'zendesk-support'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceZendeskSupport:
    r"""The values required to configure the source."""
    source_type: SourceZendeskSupportZendeskSupport = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The UTC date and time from which you'd like to replicate data, in the format YYYY-MM-DDT00:00:00Z. All data generated after this date will be replicated."""
    subdomain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subdomain') }})
    r"""This is your unique Zendesk subdomain that can be found in your account URL. For example, in https://MY_SUBDOMAIN.zendesk.com/, MY_SUBDOMAIN is the value of your subdomain."""
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    r"""Zendesk allows two authentication methods. We recommend using `OAuth2.0` for Airbyte Cloud users and `API token` for Airbyte Open Source users."""
    ignore_pagination: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ignore_pagination'), 'exclude': lambda f: f is None }})
    r"""Makes each stream read a single page of data."""
    

