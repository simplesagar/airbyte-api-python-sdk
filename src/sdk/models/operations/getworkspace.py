"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import workspaceresponse as shared_workspaceresponse
from typing import Optional


@dataclasses.dataclass
class GetWorkspaceRequest:
    
    workspace_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspaceId', 'style': 'simple', 'explode': False }})  
    

@dataclasses.dataclass
class GetWorkspaceResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    workspace_response: Optional[shared_workspaceresponse.WorkspaceResponse] = dataclasses.field(default=None)
    r"""Get a Workspace by the id in the path."""  
    