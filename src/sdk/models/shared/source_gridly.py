"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils

class SourceGridlyGridlyEnum(str, Enum):
    GRIDLY = 'gridly'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGridly:
    r"""The values required to configure the source."""
    
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})  
    grid_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grid_id') }})
    r"""ID of a grid, or can be ID of a branch"""  
    source_type: SourceGridlyGridlyEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})  
    