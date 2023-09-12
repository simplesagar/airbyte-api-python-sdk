"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from typing import Any, Optional

class SourceLinkedinAdsAdAnalyticsReportConfigurationPivotCategory(str, Enum):
    r"""Choose a category to pivot your analytics report around. This selection will organize your data based on the chosen attribute, allowing you to analyze trends and performance from different perspectives."""
    COMPANY = 'COMPANY'
    ACCOUNT = 'ACCOUNT'
    SHARE = 'SHARE'
    CAMPAIGN = 'CAMPAIGN'
    CREATIVE = 'CREATIVE'
    CAMPAIGN_GROUP = 'CAMPAIGN_GROUP'
    CONVERSION = 'CONVERSION'
    CONVERSATION_NODE = 'CONVERSATION_NODE'
    CONVERSATION_NODE_OPTION_INDEX = 'CONVERSATION_NODE_OPTION_INDEX'
    SERVING_LOCATION = 'SERVING_LOCATION'
    CARD_INDEX = 'CARD_INDEX'
    MEMBER_COMPANY_SIZE = 'MEMBER_COMPANY_SIZE'
    MEMBER_INDUSTRY = 'MEMBER_INDUSTRY'
    MEMBER_SENIORITY = 'MEMBER_SENIORITY'
    MEMBER_JOB_TITLE = 'MEMBER_JOB_TITLE '
    MEMBER_JOB_FUNCTION = 'MEMBER_JOB_FUNCTION '
    MEMBER_COUNTRY_V2 = 'MEMBER_COUNTRY_V2 '
    MEMBER_REGION_V2 = 'MEMBER_REGION_V2'
    MEMBER_COMPANY = 'MEMBER_COMPANY'
    PLACEMENT_NAME = 'PLACEMENT_NAME'
    IMPRESSION_DEVICE_TYPE = 'IMPRESSION_DEVICE_TYPE'

class SourceLinkedinAdsAdAnalyticsReportConfigurationTimeGranularity(str, Enum):
    r"""Choose how to group the data in your report by time. The options are:<br>- 'ALL': A single result summarizing the entire time range.<br>- 'DAILY': Group results by each day.<br>- 'MONTHLY': Group results by each month.<br>- 'YEARLY': Group results by each year.<br>Selecting a time grouping helps you analyze trends and patterns over different time periods."""
    ALL = 'ALL'
    DAILY = 'DAILY'
    MONTHLY = 'MONTHLY'
    YEARLY = 'YEARLY'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceLinkedinAdsAdAnalyticsReportConfiguration:
    r"""Config for custom ad Analytics Report"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name for the custom report."""
    pivot_by: SourceLinkedinAdsAdAnalyticsReportConfigurationPivotCategory = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pivot_by') }})
    r"""Choose a category to pivot your analytics report around. This selection will organize your data based on the chosen attribute, allowing you to analyze trends and performance from different perspectives."""
    time_granularity: SourceLinkedinAdsAdAnalyticsReportConfigurationTimeGranularity = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time_granularity') }})
    r"""Choose how to group the data in your report by time. The options are:<br>- 'ALL': A single result summarizing the entire time range.<br>- 'DAILY': Group results by each day.<br>- 'MONTHLY': Group results by each month.<br>- 'YEARLY': Group results by each year.<br>Selecting a time grouping helps you analyze trends and patterns over different time periods."""
    


class SourceLinkedinAdsCredentialsAccessTokenAuthMethod(str, Enum):
    ACCESS_TOKEN = 'access_token'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceLinkedinAdsCredentialsAccessToken:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""The access token generated for your developer application. Refer to our <a href='https://docs.airbyte.com/integrations/sources/linkedin-ads#setup-guide'>documentation</a> for more information."""
    auth_method: Optional[SourceLinkedinAdsCredentialsAccessTokenAuthMethod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method'), 'exclude': lambda f: f is None }})
    


class SourceLinkedinAdsCredentialsOAuth20AuthMethod(str, Enum):
    O_AUTH2_0 = 'oAuth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceLinkedinAdsCredentialsOAuth20:
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The client ID of your developer application. Refer to our <a href='https://docs.airbyte.com/integrations/sources/linkedin-ads#setup-guide'>documentation</a> for more information."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The client secret of your developer application. Refer to our <a href='https://docs.airbyte.com/integrations/sources/linkedin-ads#setup-guide'>documentation</a> for more information."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""The key to refresh the expired access token. Refer to our <a href='https://docs.airbyte.com/integrations/sources/linkedin-ads#setup-guide'>documentation</a> for more information."""
    auth_method: Optional[SourceLinkedinAdsCredentialsOAuth20AuthMethod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method'), 'exclude': lambda f: f is None }})
    


class SourceLinkedinAdsLinkedinAds(str, Enum):
    LINKEDIN_ADS = 'linkedin-ads'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceLinkedinAds:
    r"""The values required to configure the source."""
    source_type: SourceLinkedinAdsLinkedinAds = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""UTC date in the format YYYY-MM-DD. Any data before this date will not be replicated."""
    account_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_ids'), 'exclude': lambda f: f is None }})
    r"""Specify the account IDs to pull data from, separated by a space. Leave this field empty if you want to pull the data from all accounts accessible by the authenticated user. See the <a href=\\"https://www.linkedin.com/help/linkedin/answer/a424270/find-linkedin-ads-account-details?lang=en\\">LinkedIn docs</a> to locate these IDs."""
    ad_analytics_reports: Optional[list[SourceLinkedinAdsAdAnalyticsReportConfiguration]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ad_analytics_reports'), 'exclude': lambda f: f is None }})
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    

