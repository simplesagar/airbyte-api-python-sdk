"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Any, Optional

class DestinationAzureBlobStorageAzureBlobStorageEnum(str, Enum):
    AZURE_BLOB_STORAGE = 'azure-blob-storage'

class DestinationAzureBlobStorageFormatJSONLinesNewlineDelimitedJSONFormatTypeEnum(str, Enum):
    JSONL = 'JSONL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationAzureBlobStorageFormatJSONLinesNewlineDelimitedJSON:
    r"""Output data format"""
    
    format_type: DestinationAzureBlobStorageFormatJSONLinesNewlineDelimitedJSONFormatTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type') }})  
    
class DestinationAzureBlobStorageFormatCSVCommaSeparatedValuesNormalizationFlatteningEnum(str, Enum):
    r"""Whether the input json data should be normalized (flattened) in the output CSV. Please refer to docs for details."""
    NO_FLATTENING = 'No flattening'
    ROOT_LEVEL_FLATTENING = 'Root level flattening'

class DestinationAzureBlobStorageFormatCSVCommaSeparatedValuesFormatTypeEnum(str, Enum):
    CSV = 'CSV'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationAzureBlobStorageFormatCSVCommaSeparatedValues:
    r"""Output data format"""
    
    flattening: DestinationAzureBlobStorageFormatCSVCommaSeparatedValuesNormalizationFlatteningEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flattening') }})
    r"""Whether the input json data should be normalized (flattened) in the output CSV. Please refer to docs for details."""  
    format_type: DestinationAzureBlobStorageFormatCSVCommaSeparatedValuesFormatTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type') }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationAzureBlobStorage:
    r"""The values required to configure the destination."""
    
    azure_blob_storage_account_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_account_key') }})
    r"""The Azure blob storage account key."""  
    azure_blob_storage_account_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_account_name') }})
    r"""The account's name of the Azure Blob Storage."""  
    destination_type: DestinationAzureBlobStorageAzureBlobStorageEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})  
    format: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format') }})
    r"""Output data format"""  
    azure_blob_storage_container_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_container_name'), 'exclude': lambda f: f is None }})
    r"""The name of the Azure blob storage container. If not exists - will be created automatically. May be empty, then will be created automatically airbytecontainer+timestamp"""  
    azure_blob_storage_endpoint_domain_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_endpoint_domain_name'), 'exclude': lambda f: f is None }})
    r"""This is Azure Blob Storage endpoint domain name. Leave default value (or leave it empty if run container from command line) to use Microsoft native from example."""  
    azure_blob_storage_output_buffer_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_output_buffer_size'), 'exclude': lambda f: f is None }})
    r"""The amount of megabytes to buffer for the output stream to Azure. This will impact memory footprint on workers, but may need adjustment for performance and appropriate block size in Azure."""  
    azure_blob_storage_spill_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_spill_size'), 'exclude': lambda f: f is None }})
    r"""The amount of megabytes after which the connector should spill the records in a new blob object. Make sure to configure size greater than individual records. Enter 0 if not applicable"""  
    