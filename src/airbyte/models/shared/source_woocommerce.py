"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields

class SourceWoocommerceWoocommerce(str, Enum):
    WOOCOMMERCE = 'woocommerce'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceWoocommerce:
    r"""The values required to configure the source."""
    
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Customer Key for API in WooCommerce shop"""
    api_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_secret') }})
    r"""Customer Secret for API in WooCommerce shop"""
    shop: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shop') }})
    r"""The name of the store. For https://EXAMPLE.com, the shop name is 'EXAMPLE.com'."""
    source_type: SourceWoocommerceWoocommerce = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date you would like to replicate data from. Format: YYYY-MM-DD"""
    