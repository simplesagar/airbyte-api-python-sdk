"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Optional

class SourceIntercomIntercom(str, Enum):
    INTERCOM = 'intercom'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceIntercom:
    r"""The values required to configure the source."""
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Access token for making authenticated requests. See the <a href=\\"https://developers.intercom.com/building-apps/docs/authentication-types#how-to-get-your-access-token\\">Intercom docs</a> for more information."""
    source_type: SourceIntercomIntercom = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Client Id for your Intercom application."""
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    r"""Client Secret for your Intercom application."""
    

