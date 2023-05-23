"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceApifyDatasetApifyDataset(str, Enum):
    APIFY_DATASET = 'apify-dataset'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceApifyDataset:
    r"""The values required to configure the source."""
    
    dataset_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('datasetId') }})
    r"""ID of the dataset you would like to load to Airbyte."""
    source_type: SourceApifyDatasetApifyDataset = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    clean: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clean'), 'exclude': lambda f: f is None }})
    r"""If set to true, only clean items will be downloaded from the dataset. See description of what clean means in <a href=\\"https://docs.apify.com/api/v2#/reference/datasets/item-collection/get-items\\">Apify API docs</a>. If not sure, set clean to false."""
    