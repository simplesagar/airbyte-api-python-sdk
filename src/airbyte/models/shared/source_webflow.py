"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceWebflowWebflow(str, Enum):
    WEBFLOW = 'webflow'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceWebflow:
    r"""The values required to configure the source."""
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""The API token for authenticating to Webflow. See https://university.webflow.com/lesson/intro-to-the-webflow-api"""
    site_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('site_id') }})
    r"""The id of the Webflow site you are requesting data from. See https://developers.webflow.com/#sites"""
    source_type: SourceWebflowWebflow = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

