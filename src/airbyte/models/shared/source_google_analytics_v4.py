"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from typing import Final, Optional, Union

class SourceGoogleAnalyticsV4CredentialsServiceAccountKeyAuthenticationAuthType(str, Enum):
    SERVICE = 'Service'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceGoogleAnalyticsV4CredentialsServiceAccountKeyAuthentication:
    r"""Credentials for the service"""
    credentials_json: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_json') }})
    r"""The JSON key of the service account to use for authorization"""
    AUTH_TYPE: Final[Optional[SourceGoogleAnalyticsV4CredentialsServiceAccountKeyAuthenticationAuthType]] = dataclasses.field(default=SourceGoogleAnalyticsV4CredentialsServiceAccountKeyAuthenticationAuthType.SERVICE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    


class SourceGoogleAnalyticsV4CredentialsAuthenticateViaGoogleOauthAuthType(str, Enum):
    CLIENT = 'Client'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceGoogleAnalyticsV4CredentialsAuthenticateViaGoogleOauth:
    r"""Credentials for the service"""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of your Google Analytics developer application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Client Secret of your Google Analytics developer application."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""The token for obtaining a new access token."""
    access_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token'), 'exclude': lambda f: f is None }})
    r"""Access Token for making authenticated requests."""
    AUTH_TYPE: Final[Optional[SourceGoogleAnalyticsV4CredentialsAuthenticateViaGoogleOauthAuthType]] = dataclasses.field(default=SourceGoogleAnalyticsV4CredentialsAuthenticateViaGoogleOauthAuthType.CLIENT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class SourceGoogleAnalyticsV4Credentials:
    pass

class SourceGoogleAnalyticsV4GoogleAnalyticsV4(str, Enum):
    GOOGLE_ANALYTICS_V4 = 'google-analytics-v4'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceGoogleAnalyticsV4:
    r"""The values required to configure the source."""
    start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The date in the format YYYY-MM-DD. Any data before this date will not be replicated."""
    view_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('view_id') }})
    r"""The ID for the Google Analytics View you want to fetch data from. This can be found from the <a href=\\"https://ga-dev-tools.appspot.com/account-explorer/\\">Google Analytics Account Explorer</a>."""
    SOURCE_TYPE: Final[SourceGoogleAnalyticsV4GoogleAnalyticsV4] = dataclasses.field(default=SourceGoogleAnalyticsV4GoogleAnalyticsV4.GOOGLE_ANALYTICS_V4, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    credentials: Optional[Union[SourceGoogleAnalyticsV4CredentialsAuthenticateViaGoogleOauth, SourceGoogleAnalyticsV4CredentialsServiceAccountKeyAuthentication]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    r"""Credentials for the service"""
    custom_reports: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_reports'), 'exclude': lambda f: f is None }})
    r"""A JSON array describing the custom reports you want to sync from Google Analytics. See <a href=\\"https://docs.airbyte.com/integrations/sources/google-analytics-v4#data-processing-latency\\">the docs</a> for more information about the exact format you can use to fill out this field."""
    window_in_days: Optional[int] = dataclasses.field(default=1, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('window_in_days'), 'exclude': lambda f: f is None }})
    r"""The time increment used by the connector when requesting data from the Google Analytics API. More information is available in the <a href=\\"https://docs.airbyte.com/integrations/sources/google-analytics-v4/#sampling-in-reports\\">the docs</a>. The bigger this value is, the faster the sync will be, but the more likely that sampling will be applied to your data, potentially causing inaccuracies in the returned results. We recommend setting this to 1 unless you have a hard requirement to make the sync faster at the expense of accuracy. The minimum allowed value for this field is 1, and the maximum is 364."""
    

