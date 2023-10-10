"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional

class DestinationKeenKeen(str, Enum):
    KEEN = 'keen'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationKeen:
    r"""The values required to configure the destination."""
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""To get Keen Master API Key, navigate to the Access tab from the left-hand, side panel and check the Project Details section."""
    project_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_id') }})
    r"""To get Keen Project ID, navigate to the Access tab from the left-hand, side panel and check the Project Details section."""
    DESTINATION_TYPE: Final[DestinationKeenKeen] = dataclasses.field(default=DestinationKeenKeen.KEEN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    infer_timestamp: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('infer_timestamp'), 'exclude': lambda f: f is None }})
    r"""Allow connector to guess keen.timestamp value based on the streamed data."""
    

