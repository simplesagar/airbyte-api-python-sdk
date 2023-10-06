"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final

class SourceShortioShortio(str, Enum):
    SHORTIO = 'shortio'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceShortio:
    r"""The values required to configure the source."""
    domain_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain_id') }})
    secret_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret_key') }})
    r"""Short.io Secret Key"""
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated."""
    SOURCE_TYPE: Final[SourceShortioShortio] = dataclasses.field(default=SourceShortioShortio.SHORTIO, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

