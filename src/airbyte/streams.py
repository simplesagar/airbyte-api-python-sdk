"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from airbyte.models import operations, shared
from typing import Optional

class Streams:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def get_stream_properties(self, request: operations.GetStreamPropertiesRequest) -> operations.GetStreamPropertiesResponse:
        r"""Get stream properties"""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/streams'
        
        query_params = utils.get_query_params(operations.GetStreamPropertiesRequest, request)
        
        client = self._client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetStreamPropertiesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.StreamProperties])
                res.stream_properties = out
        elif http_res.status_code in [400, 403, 404]:
            pass

        return res

    