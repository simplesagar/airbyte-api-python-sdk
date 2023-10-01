"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional, Union

class SourceFileSecureFileFormat(str, Enum):
    r"""The Format of the file which should be replicated (Warning: some formats may be experimental, please refer to the docs)."""
    CSV = 'csv'
    JSON = 'json'
    JSONL = 'jsonl'
    EXCEL = 'excel'
    EXCEL_BINARY = 'excel_binary'
    FEATHER = 'feather'
    PARQUET = 'parquet'
    YAML = 'yaml'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceFileSecureStorageProviderSFTPSecureFileTransferProtocol:
    r"""The storage Provider or Location of the file(s) which should be replicated."""
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    STORAGE: Final[str] = dataclasses.field(default='SFTP', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    port: Optional[str] = dataclasses.field(default='22', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceFileSecureStorageProviderSCPSecureCopyProtocol:
    r"""The storage Provider or Location of the file(s) which should be replicated."""
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    STORAGE: Final[str] = dataclasses.field(default='SCP', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    port: Optional[str] = dataclasses.field(default='22', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceFileSecureStorageProviderSSHSecureShell:
    r"""The storage Provider or Location of the file(s) which should be replicated."""
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    STORAGE: Final[str] = dataclasses.field(default='SSH', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    port: Optional[str] = dataclasses.field(default='22', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceFileSecureStorageProviderAzBlobAzureBlobStorage:
    r"""The storage Provider or Location of the file(s) which should be replicated."""
    storage_account: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage_account') }})
    r"""The globally unique name of the storage account that the desired blob sits within. See <a href=\\"https://docs.microsoft.com/en-us/azure/storage/common/storage-account-overview\\" target=\\"_blank\\">here</a> for more details."""
    STORAGE: Final[str] = dataclasses.field(default='AzBlob', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    sas_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sas_token'), 'exclude': lambda f: f is None }})
    r"""To access Azure Blob Storage, this connector would need credentials with the proper permissions. One option is a SAS (Shared Access Signature) token. If accessing publicly available data, this field is not necessary."""
    shared_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shared_key'), 'exclude': lambda f: f is None }})
    r"""To access Azure Blob Storage, this connector would need credentials with the proper permissions. One option is a storage account shared key (aka account key or access key). If accessing publicly available data, this field is not necessary."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceFileSecureStorageProviderS3AmazonWebServices:
    r"""The storage Provider or Location of the file(s) which should be replicated."""
    STORAGE: Final[str] = dataclasses.field(default='S3', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    aws_access_key_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_access_key_id'), 'exclude': lambda f: f is None }})
    r"""In order to access private Buckets stored on AWS S3, this connector would need credentials with the proper permissions. If accessing publicly available data, this field is not necessary."""
    aws_secret_access_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_secret_access_key'), 'exclude': lambda f: f is None }})
    r"""In order to access private Buckets stored on AWS S3, this connector would need credentials with the proper permissions. If accessing publicly available data, this field is not necessary."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceFileSecureStorageProviderGCSGoogleCloudStorage:
    r"""The storage Provider or Location of the file(s) which should be replicated."""
    STORAGE: Final[str] = dataclasses.field(default='GCS', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    service_account_json: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service_account_json'), 'exclude': lambda f: f is None }})
    r"""In order to access private Buckets stored on Google Cloud, this connector would need a service account json credentials with the proper permissions as described <a href=\\"https://cloud.google.com/iam/docs/service-accounts\\" target=\\"_blank\\">here</a>. Please generate the credentials.json file and copy/paste its content to this field (expecting JSON formats). If accessing publicly available data, this field is not necessary."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceFileSecureStorageProviderHTTPSPublicWeb:
    r"""The storage Provider or Location of the file(s) which should be replicated."""
    STORAGE: Final[str] = dataclasses.field(default='HTTPS', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    user_agent: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_agent'), 'exclude': lambda f: f is None }})
    r"""Add User-Agent to request"""
    




@dataclasses.dataclass
class SourceFileSecureStorageProvider:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceFileSecure:
    r"""The values required to configure the source."""
    dataset_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataset_name') }})
    r"""The Name of the final table to replicate this file into (should include letters, numbers dash and underscores only)."""
    provider: Union[SourceFileSecureStorageProviderHTTPSPublicWeb, SourceFileSecureStorageProviderGCSGoogleCloudStorage, SourceFileSecureStorageProviderS3AmazonWebServices, SourceFileSecureStorageProviderAzBlobAzureBlobStorage, SourceFileSecureStorageProviderSSHSecureShell, SourceFileSecureStorageProviderSCPSecureCopyProtocol, SourceFileSecureStorageProviderSFTPSecureFileTransferProtocol] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider') }})
    r"""The storage Provider or Location of the file(s) which should be replicated."""
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    r"""The URL path to access the file which should be replicated."""
    SOURCE_TYPE: Final[str] = dataclasses.field(default='file-secure', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    format: Optional[SourceFileSecureFileFormat] = dataclasses.field(default=SourceFileSecureFileFormat.CSV, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format'), 'exclude': lambda f: f is None }})
    r"""The Format of the file which should be replicated (Warning: some formats may be experimental, please refer to the docs)."""
    reader_options: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reader_options'), 'exclude': lambda f: f is None }})
    r"""This should be a string in JSON format. It depends on the chosen file format to provide additional options and tune its behavior."""
    

