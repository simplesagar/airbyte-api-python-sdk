"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import sourcepatchrequest as shared_sourcepatchrequest
from ..shared import sourceresponse as shared_sourceresponse
from typing import Optional



@dataclasses.dataclass
class PatchSourceRequest:
    source_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'sourceId', 'style': 'simple', 'explode': False }})
    source_patch_request: Optional[shared_sourcepatchrequest.SourcePatchRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class PatchSourceResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    source_response: Optional[shared_sourceresponse.SourceResponse] = dataclasses.field(default=None)
    r"""Update a Source"""
    

