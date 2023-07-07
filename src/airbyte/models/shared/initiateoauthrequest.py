"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import oauthactornames as shared_oauthactornames
from ..shared import oauthinputconfiguration as shared_oauthinputconfiguration
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class InitiateOauthRequest:
    r"""POST body for initiating OAuth via the public API"""
    name: shared_oauthactornames.OAuthActorNames = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    redirect_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('redirectUrl') }})
    r"""The URL to redirect the user to with the OAuth secret stored in the secret_id query string parameter after authentication is complete."""
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspaceId') }})
    r"""The workspace to create the secret and eventually the full source."""
    o_auth_input_configuration: Optional[shared_oauthinputconfiguration.OAuthInputConfiguration] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('oAuthInputConfiguration'), 'exclude': lambda f: f is None }})
    r"""Arbitrary vars to pass for OAuth depending on what the source/destination spec requires."""
    

