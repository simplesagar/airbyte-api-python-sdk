"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Any, Optional

class SourceS3FormatJsonlFiletype(str, Enum):
    JSONL = 'jsonl'

class SourceS3FormatJsonlUnexpectedFieldBehavior(str, Enum):
    r"""How JSON fields outside of explicit_schema (if given) are treated. Check <a href=\\"https://arrow.apache.org/docs/python/generated/pyarrow.json.ParseOptions.html\\" target=\\"_blank\\">PyArrow documentation</a> for details"""
    IGNORE = 'ignore'
    INFER = 'infer'
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceS3FormatJsonl:
    r"""This connector uses <a href=\\"https://arrow.apache.org/docs/python/json.html\\" target=\\"_blank\\">PyArrow</a> for JSON Lines (jsonl) file parsing."""
    block_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('block_size'), 'exclude': lambda f: f is None }})
    r"""The chunk size in bytes to process at a time in memory from each file. If your data is particularly wide and failing during schema detection, increasing this should solve it. Beware of raising this too high as you could hit OOM errors."""
    filetype: Optional[SourceS3FormatJsonlFiletype] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})
    newlines_in_values: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('newlines_in_values'), 'exclude': lambda f: f is None }})
    r"""Whether newline characters are allowed in JSON values. Turning this on may affect performance. Leave blank to default to False."""
    unexpected_field_behavior: Optional[SourceS3FormatJsonlUnexpectedFieldBehavior] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unexpected_field_behavior'), 'exclude': lambda f: f is None }})
    r"""How JSON fields outside of explicit_schema (if given) are treated. Check <a href=\\"https://arrow.apache.org/docs/python/generated/pyarrow.json.ParseOptions.html\\" target=\\"_blank\\">PyArrow documentation</a> for details"""
    


class SourceS3FormatAvroFiletype(str, Enum):
    AVRO = 'avro'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceS3FormatAvro:
    r"""This connector utilises <a href=\\"https://fastavro.readthedocs.io/en/latest/\\" target=\\"_blank\\">fastavro</a> for Avro parsing."""
    filetype: Optional[SourceS3FormatAvroFiletype] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})
    


class SourceS3FormatParquetFiletype(str, Enum):
    PARQUET = 'parquet'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceS3FormatParquet:
    r"""This connector utilises <a href=\\"https://arrow.apache.org/docs/python/generated/pyarrow.parquet.ParquetFile.html\\" target=\\"_blank\\">PyArrow (Apache Arrow)</a> for Parquet parsing."""
    batch_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batch_size'), 'exclude': lambda f: f is None }})
    r"""Maximum number of records per batch read from the input files. Batches may be smaller if there aren’t enough rows in the file. This option can help avoid out-of-memory errors if your data is particularly wide."""
    buffer_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('buffer_size'), 'exclude': lambda f: f is None }})
    r"""Perform read buffering when deserializing individual column chunks. By default every group column will be loaded fully to memory. This option can help avoid out-of-memory errors if your data is particularly wide."""
    columns: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('columns'), 'exclude': lambda f: f is None }})
    r"""If you only want to sync a subset of the columns from the file(s), add the columns you want here as a comma-delimited list. Leave it empty to sync all columns."""
    filetype: Optional[SourceS3FormatParquetFiletype] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})
    


class SourceS3FormatCSVFiletype(str, Enum):
    CSV = 'csv'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceS3FormatCSV:
    r"""This connector utilises <a href=\\"https: // arrow.apache.org/docs/python/generated/pyarrow.csv.open_csv.html\\" target=\\"_blank\\">PyArrow (Apache Arrow)</a> for CSV parsing."""
    additional_reader_options: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additional_reader_options'), 'exclude': lambda f: f is None }})
    r"""Optionally add a valid JSON string here to provide additional options to the csv reader. Mappings must correspond to options <a href=\\"https://arrow.apache.org/docs/python/generated/pyarrow.csv.ConvertOptions.html#pyarrow.csv.ConvertOptions\\" target=\\"_blank\\">detailed here</a>. 'column_types' is used internally to handle schema so overriding that would likely cause problems."""
    advanced_options: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('advanced_options'), 'exclude': lambda f: f is None }})
    r"""Optionally add a valid JSON string here to provide additional <a href=\\"https://arrow.apache.org/docs/python/generated/pyarrow.csv.ReadOptions.html#pyarrow.csv.ReadOptions\\" target=\\"_blank\\">Pyarrow ReadOptions</a>. Specify 'column_names' here if your CSV doesn't have header, or if you want to use custom column names. 'block_size' and 'encoding' are already used above, specify them again here will override the values above."""
    block_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('block_size'), 'exclude': lambda f: f is None }})
    r"""The chunk size in bytes to process at a time in memory from each file. If your data is particularly wide and failing during schema detection, increasing this should solve it. Beware of raising this too high as you could hit OOM errors."""
    delimiter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delimiter'), 'exclude': lambda f: f is None }})
    r"""The character delimiting individual cells in the CSV data. This may only be a 1-character string. For tab-delimited data enter '\t'."""
    double_quote: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('double_quote'), 'exclude': lambda f: f is None }})
    r"""Whether two quotes in a quoted CSV value denote a single quote in the data."""
    encoding: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encoding'), 'exclude': lambda f: f is None }})
    r"""The character encoding of the CSV data. Leave blank to default to <strong>UTF8</strong>. See <a href=\\"https://docs.python.org/3/library/codecs.html#standard-encodings\\" target=\\"_blank\\">list of python encodings</a> for allowable options."""
    escape_char: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('escape_char'), 'exclude': lambda f: f is None }})
    r"""The character used for escaping special characters. To disallow escaping, leave this field blank."""
    filetype: Optional[SourceS3FormatCSVFiletype] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})
    infer_datatypes: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('infer_datatypes'), 'exclude': lambda f: f is None }})
    r"""Configures whether a schema for the source should be inferred from the current data or not. If set to false and a custom schema is set, then the manually enforced schema is used. If a schema is not manually set, and this is set to false, then all fields will be read as strings"""
    newlines_in_values: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('newlines_in_values'), 'exclude': lambda f: f is None }})
    r"""Whether newline characters are allowed in CSV values. Turning this on may affect performance. Leave blank to default to False."""
    quote_char: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quote_char'), 'exclude': lambda f: f is None }})
    r"""The character used for quoting CSV values. To disallow quoting, make this field blank."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceS3S3AmazonWebServices:
    r"""Deprecated and will be removed soon. Please do not use this field anymore and use bucket, aws_access_key_id, aws_secret_access_key and endpoint instead. Use this to load files from S3 or S3-compatible services"""
    aws_access_key_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_access_key_id'), 'exclude': lambda f: f is None }})
    r"""In order to access private Buckets stored on AWS S3, this connector requires credentials with the proper permissions. If accessing publicly available data, this field is not necessary."""
    aws_secret_access_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_secret_access_key'), 'exclude': lambda f: f is None }})
    r"""In order to access private Buckets stored on AWS S3, this connector requires credentials with the proper permissions. If accessing publicly available data, this field is not necessary."""
    bucket: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bucket'), 'exclude': lambda f: f is None }})
    r"""Name of the S3 bucket where the file(s) exist."""
    endpoint: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('endpoint'), 'exclude': lambda f: f is None }})
    r"""Endpoint to an S3 compatible service. Leave empty to use AWS."""
    path_prefix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('path_prefix'), 'exclude': lambda f: f is None }})
    r"""By providing a path-like prefix (e.g. myFolder/thisTable/) under which all the relevant files sit, we can optimize finding these in S3. This is optional but recommended if your bucket contains many folders/files which you don't need to replicate."""
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Any file modified before this date will not be replicated."""
    


class SourceS3S3(str, Enum):
    S3 = 's3'

class SourceS3FileBasedStreamConfigFormatParquetFormatFiletype(str, Enum):
    PARQUET = 'parquet'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceS3FileBasedStreamConfigFormatParquetFormat:
    r"""The configuration options that are used to alter how to read incoming files that deviate from the standard formatting."""
    decimal_as_float: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('decimal_as_float'), 'exclude': lambda f: f is None }})
    r"""Whether to convert decimal fields to floats. There is a loss of precision when converting decimals to floats, so this is not recommended."""
    filetype: Optional[SourceS3FileBasedStreamConfigFormatParquetFormatFiletype] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})
    


class SourceS3FileBasedStreamConfigFormatJsonlFormatFiletype(str, Enum):
    JSONL = 'jsonl'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceS3FileBasedStreamConfigFormatJsonlFormat:
    r"""The configuration options that are used to alter how to read incoming files that deviate from the standard formatting."""
    filetype: Optional[SourceS3FileBasedStreamConfigFormatJsonlFormatFiletype] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})
    


class SourceS3FileBasedStreamConfigFormatCSVFormatFiletype(str, Enum):
    CSV = 'csv'

class SourceS3FileBasedStreamConfigFormatCSVFormatHeaderDefinitionUserProvidedHeaderDefinitionType(str, Enum):
    USER_PROVIDED = 'User Provided'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceS3FileBasedStreamConfigFormatCSVFormatHeaderDefinitionUserProvided:
    r"""How headers will be defined. `User Provided` assumes the CSV does not have a header row and uses the headers provided and `Autogenerated` assumes the CSV does not have a header row and the CDK will generate headers using for `f{i}` where `i` is the index starting from 0. Else, the default behavior is to use the header from the CSV file. If a user wants to autogenerate or provide column names for a CSV having headers, they can skip rows."""
    column_names: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('column_names') }})
    r"""The column names that will be used while emitting the CSV records"""
    header_definition_type: Optional[SourceS3FileBasedStreamConfigFormatCSVFormatHeaderDefinitionUserProvidedHeaderDefinitionType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('header_definition_type'), 'exclude': lambda f: f is None }})
    


class SourceS3FileBasedStreamConfigFormatCSVFormatHeaderDefinitionAutogeneratedHeaderDefinitionType(str, Enum):
    AUTOGENERATED = 'Autogenerated'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceS3FileBasedStreamConfigFormatCSVFormatHeaderDefinitionAutogenerated:
    r"""How headers will be defined. `User Provided` assumes the CSV does not have a header row and uses the headers provided and `Autogenerated` assumes the CSV does not have a header row and the CDK will generate headers using for `f{i}` where `i` is the index starting from 0. Else, the default behavior is to use the header from the CSV file. If a user wants to autogenerate or provide column names for a CSV having headers, they can skip rows."""
    header_definition_type: Optional[SourceS3FileBasedStreamConfigFormatCSVFormatHeaderDefinitionAutogeneratedHeaderDefinitionType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('header_definition_type'), 'exclude': lambda f: f is None }})
    


class SourceS3FileBasedStreamConfigFormatCSVFormatHeaderDefinitionFromCSVHeaderDefinitionType(str, Enum):
    FROM_CSV = 'From CSV'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceS3FileBasedStreamConfigFormatCSVFormatHeaderDefinitionFromCSV:
    r"""How headers will be defined. `User Provided` assumes the CSV does not have a header row and uses the headers provided and `Autogenerated` assumes the CSV does not have a header row and the CDK will generate headers using for `f{i}` where `i` is the index starting from 0. Else, the default behavior is to use the header from the CSV file. If a user wants to autogenerate or provide column names for a CSV having headers, they can skip rows."""
    header_definition_type: Optional[SourceS3FileBasedStreamConfigFormatCSVFormatHeaderDefinitionFromCSVHeaderDefinitionType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('header_definition_type'), 'exclude': lambda f: f is None }})
    


class SourceS3FileBasedStreamConfigFormatCSVFormatInferenceType(str, Enum):
    r"""How to infer the types of the columns. If none, inference default to strings."""
    NONE = 'None'
    PRIMITIVE_TYPES_ONLY = 'Primitive Types Only'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceS3FileBasedStreamConfigFormatCSVFormat:
    r"""The configuration options that are used to alter how to read incoming files that deviate from the standard formatting."""
    delimiter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delimiter'), 'exclude': lambda f: f is None }})
    r"""The character delimiting individual cells in the CSV data. This may only be a 1-character string. For tab-delimited data enter '\t'."""
    double_quote: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('double_quote'), 'exclude': lambda f: f is None }})
    r"""Whether two quotes in a quoted CSV value denote a single quote in the data."""
    encoding: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encoding'), 'exclude': lambda f: f is None }})
    r"""The character encoding of the CSV data. Leave blank to default to <strong>UTF8</strong>. See <a href=\\"https://docs.python.org/3/library/codecs.html#standard-encodings\\" target=\\"_blank\\">list of python encodings</a> for allowable options."""
    escape_char: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('escape_char'), 'exclude': lambda f: f is None }})
    r"""The character used for escaping special characters. To disallow escaping, leave this field blank."""
    false_values: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('false_values'), 'exclude': lambda f: f is None }})
    r"""A set of case-sensitive strings that should be interpreted as false values."""
    filetype: Optional[SourceS3FileBasedStreamConfigFormatCSVFormatFiletype] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})
    header_definition: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('header_definition'), 'exclude': lambda f: f is None }})
    r"""How headers will be defined. `User Provided` assumes the CSV does not have a header row and uses the headers provided and `Autogenerated` assumes the CSV does not have a header row and the CDK will generate headers using for `f{i}` where `i` is the index starting from 0. Else, the default behavior is to use the header from the CSV file. If a user wants to autogenerate or provide column names for a CSV having headers, they can skip rows."""
    inference_type: Optional[SourceS3FileBasedStreamConfigFormatCSVFormatInferenceType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('inference_type'), 'exclude': lambda f: f is None }})
    r"""How to infer the types of the columns. If none, inference default to strings."""
    null_values: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('null_values'), 'exclude': lambda f: f is None }})
    r"""A set of case-sensitive strings that should be interpreted as null values. For example, if the value 'NA' should be interpreted as null, enter 'NA' in this field."""
    quote_char: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quote_char'), 'exclude': lambda f: f is None }})
    r"""The character used for quoting CSV values. To disallow quoting, make this field blank."""
    skip_rows_after_header: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('skip_rows_after_header'), 'exclude': lambda f: f is None }})
    r"""The number of rows to skip after the header row."""
    skip_rows_before_header: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('skip_rows_before_header'), 'exclude': lambda f: f is None }})
    r"""The number of rows to skip before the header row. For example, if the header row is on the 3rd row, enter 2 in this field."""
    strings_can_be_null: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('strings_can_be_null'), 'exclude': lambda f: f is None }})
    r"""Whether strings can be interpreted as null values. If true, strings that match the null_values set will be interpreted as null. If false, strings that match the null_values set will be interpreted as the string itself."""
    true_values: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('true_values'), 'exclude': lambda f: f is None }})
    r"""A set of case-sensitive strings that should be interpreted as true values."""
    


class SourceS3FileBasedStreamConfigFormatAvroFormatFiletype(str, Enum):
    AVRO = 'avro'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceS3FileBasedStreamConfigFormatAvroFormat:
    r"""The configuration options that are used to alter how to read incoming files that deviate from the standard formatting."""
    double_as_string: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('double_as_string'), 'exclude': lambda f: f is None }})
    r"""Whether to convert double fields to strings. This is recommended if you have decimal numbers with a high degree of precision because there can be a loss precision when handling floating point numbers."""
    filetype: Optional[SourceS3FileBasedStreamConfigFormatAvroFormatFiletype] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})
    


class SourceS3FileBasedStreamConfigValidationPolicy(str, Enum):
    r"""The name of the validation policy that dictates sync behavior when a record does not adhere to the stream schema."""
    EMIT_RECORD = 'Emit Record'
    SKIP_RECORD = 'Skip Record'
    WAIT_FOR_DISCOVER = 'Wait for Discover'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceS3FileBasedStreamConfig:
    file_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_type') }})
    r"""The data file type that is being extracted for a stream."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the stream."""
    days_to_sync_if_history_is_full: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days_to_sync_if_history_is_full'), 'exclude': lambda f: f is None }})
    r"""When the state history of the file store is full, syncs will only read files that were last modified in the provided day range."""
    format: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format'), 'exclude': lambda f: f is None }})
    r"""The configuration options that are used to alter how to read incoming files that deviate from the standard formatting."""
    globs: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('globs'), 'exclude': lambda f: f is None }})
    r"""The pattern used to specify which files should be selected from the file system. For more information on glob pattern matching look <a href=\\"https://en.wikipedia.org/wiki/Glob_(programming)\\">here</a>."""
    input_schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('input_schema'), 'exclude': lambda f: f is None }})
    r"""The schema that will be used to validate records extracted from the file. This will override the stream schema that is auto-detected from incoming files."""
    legacy_prefix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('legacy_prefix'), 'exclude': lambda f: f is None }})
    r"""The path prefix configured in v3 versions of the S3 connector. This option is deprecated in favor of a single glob."""
    primary_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primary_key'), 'exclude': lambda f: f is None }})
    r"""The column or columns (for a composite key) that serves as the unique identifier of a record."""
    schemaless: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schemaless'), 'exclude': lambda f: f is None }})
    r"""When enabled, syncs will not validate or structure records against the stream's schema."""
    validation_policy: Optional[SourceS3FileBasedStreamConfigValidationPolicy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation_policy'), 'exclude': lambda f: f is None }})
    r"""The name of the validation policy that dictates sync behavior when a record does not adhere to the stream schema."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceS3:
    r"""NOTE: When this Spec is changed, legacy_config_transformer.py must also be modified to uptake the changes
    because it is responsible for converting legacy S3 v3 configs into v4 configs using the File-Based CDK.
    """
    bucket: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bucket') }})
    r"""Name of the S3 bucket where the file(s) exist."""
    source_type: SourceS3S3 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    streams: list[SourceS3FileBasedStreamConfig] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streams') }})
    r"""Each instance of this configuration defines a <a href=\\"https://docs.airbyte.com/cloud/core-concepts#stream\\">stream</a>. Use this to define which files belong in the stream, their format, and how they should be parsed and validated. When sending data to warehouse destination such as Snowflake or BigQuery, each stream is a separate table."""
    aws_access_key_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_access_key_id'), 'exclude': lambda f: f is None }})
    r"""In order to access private Buckets stored on AWS S3, this connector requires credentials with the proper permissions. If accessing publicly available data, this field is not necessary."""
    aws_secret_access_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_secret_access_key'), 'exclude': lambda f: f is None }})
    r"""In order to access private Buckets stored on AWS S3, this connector requires credentials with the proper permissions. If accessing publicly available data, this field is not necessary."""
    dataset: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataset'), 'exclude': lambda f: f is None }})
    r"""Deprecated and will be removed soon. Please do not use this field anymore and use streams.name instead. The name of the stream you would like this source to output. Can contain letters, numbers, or underscores."""
    endpoint: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('endpoint'), 'exclude': lambda f: f is None }})
    r"""Endpoint to an S3 compatible service. Leave empty to use AWS."""
    format: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format'), 'exclude': lambda f: f is None }})
    r"""Deprecated and will be removed soon. Please do not use this field anymore and use streams.format instead. The format of the files you'd like to replicate"""
    path_pattern: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('path_pattern'), 'exclude': lambda f: f is None }})
    r"""Deprecated and will be removed soon. Please do not use this field anymore and use streams.globs instead. A regular expression which tells the connector which files to replicate. All files which match this pattern will be replicated. Use | to separate multiple patterns. See <a href=\\"https://facelessuser.github.io/wcmatch/glob/\\" target=\\"_blank\\">this page</a> to understand pattern syntax (GLOBSTAR and SPLIT flags are enabled). Use pattern <strong>**</strong> to pick up all files."""
    provider: Optional[SourceS3S3AmazonWebServices] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider'), 'exclude': lambda f: f is None }})
    r"""Deprecated and will be removed soon. Please do not use this field anymore and use bucket, aws_access_key_id, aws_secret_access_key and endpoint instead. Use this to load files from S3 or S3-compatible services"""
    schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema'), 'exclude': lambda f: f is None }})
    r"""Deprecated and will be removed soon. Please do not use this field anymore and use streams.input_schema instead. Optionally provide a schema to enforce, as a valid JSON string. Ensure this is a mapping of <strong>{ \\"column\\" : \\"type\\" }</strong>, where types are valid <a href=\\"https://json-schema.org/understanding-json-schema/reference/type.html\\" target=\\"_blank\\">JSON Schema datatypes</a>. Leave as {} to auto-infer the schema."""
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""UTC date and time in the format 2017-01-25T00:00:00.000000Z. Any file modified before this date will not be replicated."""
    

