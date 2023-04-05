"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional

class SourceCoinmarketcapDataTypeEnum(str, Enum):
    r"""/latest: Latest market ticker quotes and averages for cryptocurrencies and exchanges. /historical: Intervals of historic market data like OHLCV data or data for use in charting libraries. See <a href=\\"https://coinmarketcap.com/api/documentation/v1/#section/Endpoint-Overview\\">here</a>."""
    LATEST = 'latest'
    HISTORICAL = 'historical'

class SourceCoinmarketcapCoinmarketcapEnum(str, Enum):
    COINMARKETCAP = 'coinmarketcap'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceCoinmarketcap:
    r"""The values required to configure the source."""
    
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Your API Key. See <a href=\\"https://coinmarketcap.com/api/documentation/v1/#section/Authentication\\">here</a>. The token is case sensitive."""  
    data_type: SourceCoinmarketcapDataTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data_type') }})
    r"""/latest: Latest market ticker quotes and averages for cryptocurrencies and exchanges. /historical: Intervals of historic market data like OHLCV data or data for use in charting libraries. See <a href=\\"https://coinmarketcap.com/api/documentation/v1/#section/Endpoint-Overview\\">here</a>."""  
    source_type: SourceCoinmarketcapCoinmarketcapEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})  
    symbols: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('symbols'), 'exclude': lambda f: f is None }})
    r"""Cryptocurrency symbols. (only used for quotes stream)"""  
    