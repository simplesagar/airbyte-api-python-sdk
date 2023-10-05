"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional

class SourceMailgunMailgun(str, Enum):
    MAILGUN = 'mailgun'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceMailgun:
    r"""The values required to configure the source."""
    private_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('private_key') }})
    r"""Primary account API key to access your Mailgun data."""
    SOURCE_TYPE: Final[SourceMailgunMailgun] = dataclasses.field(default=SourceMailgunMailgun.MAILGUN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    domain_region: Optional[str] = dataclasses.field(default='US', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain_region'), 'exclude': lambda f: f is None }})
    r"""Domain region code. 'EU' or 'US' are possible values. The default is 'US'."""
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""UTC date and time in the format 2020-10-01 00:00:00. Any data before this date will not be replicated. If omitted, defaults to 3 days ago."""
    

