"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceAzureBlobStorageAzureBlobStorage(str, Enum):
    AZURE_BLOB_STORAGE = 'azure-blob-storage'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceAzureBlobStorage:
    r"""The values required to configure the source."""
    azure_blob_storage_account_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_account_key') }})
    r"""The Azure blob storage account key."""
    azure_blob_storage_account_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_account_name') }})
    r"""The account's name of the Azure Blob Storage."""
    azure_blob_storage_container_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_container_name') }})
    r"""The name of the Azure blob storage container."""
    format: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format') }})
    r"""Input data format"""
    source_type: SourceAzureBlobStorageAzureBlobStorage = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    azure_blob_storage_blobs_prefix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_blobs_prefix'), 'exclude': lambda f: f is None }})
    r"""The Azure blob storage prefix to be applied"""
    azure_blob_storage_endpoint: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_endpoint'), 'exclude': lambda f: f is None }})
    r"""This is Azure Blob Storage endpoint domain name. Leave default value (or leave it empty if run container from command line) to use Microsoft native from example."""
    azure_blob_storage_schema_inference_limit: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_schema_inference_limit'), 'exclude': lambda f: f is None }})
    r"""The Azure blob storage blobs to scan for inferring the schema, useful on large amounts of data with consistent structure"""
    

