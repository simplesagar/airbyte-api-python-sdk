"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional

class SourceOrbOrbEnum(str, Enum):
    ORB = 'orb'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOrb:
    r"""The values required to configure the source."""
    
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Orb API Key, issued from the Orb admin console."""  
    source_type: SourceOrbOrbEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})  
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    r"""UTC date and time in the format 2022-03-01T00:00:00Z. Any data with created_at before this data will not be synced. For Subscription Usage, this becomes the `timeframe_start` API parameter."""  
    lookback_window_days: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lookback_window_days'), 'exclude': lambda f: f is None }})
    r"""When set to N, the connector will always refresh resources created within the past N days. By default, updated objects that are not newly created are not incrementally synced."""  
    numeric_event_properties_keys: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numeric_event_properties_keys'), 'exclude': lambda f: f is None }})
    r"""Property key names to extract from all events, in order to enrich ledger entries corresponding to an event deduction."""  
    plan_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('plan_id'), 'exclude': lambda f: f is None }})
    r"""Orb Plan ID to filter subscriptions that should have usage fetched."""  
    string_event_properties_keys: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('string_event_properties_keys'), 'exclude': lambda f: f is None }})
    r"""Property key names to extract from all events, in order to enrich ledger entries corresponding to an event deduction."""  
    subscription_usage_grouping_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subscription_usage_grouping_key'), 'exclude': lambda f: f is None }})
    r"""Property key name to group subscription usage by."""  
    