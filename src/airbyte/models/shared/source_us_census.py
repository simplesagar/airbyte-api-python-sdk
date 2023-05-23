"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceUsCensusUsCensus(str, Enum):
    US_CENSUS = 'us-census'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceUsCensus:
    r"""The values required to configure the source."""
    
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Your API Key. Get your key <a href=\\"https://api.census.gov/data/key_signup.html\\">here</a>."""
    query_path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query_path') }})
    r"""The path portion of the GET request"""
    source_type: SourceUsCensusUsCensus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    query_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query_params'), 'exclude': lambda f: f is None }})
    r"""The query parameters portion of the GET request, without the api key"""
    