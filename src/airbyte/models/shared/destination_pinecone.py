"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional, Union

class DestinationPineconePinecone(str, Enum):
    PINECONE = 'pinecone'

class DestinationPineconeEmbeddingFakeMode(str, Enum):
    FAKE = 'fake'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationPineconeEmbeddingFake:
    r"""Use a fake embedding made out of random vectors with 1536 embedding dimensions. This is useful for testing the data pipeline without incurring any costs."""
    mode: Optional[DestinationPineconeEmbeddingFakeMode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    


class DestinationPineconeEmbeddingCohereMode(str, Enum):
    COHERE = 'cohere'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationPineconeEmbeddingCohere:
    r"""Use the Cohere API to embed text."""
    cohere_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cohere_key') }})
    mode: Optional[DestinationPineconeEmbeddingCohereMode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    


class DestinationPineconeEmbeddingOpenAIMode(str, Enum):
    OPENAI = 'openai'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationPineconeEmbeddingOpenAI:
    r"""Use the OpenAI API to embed text. This option is using the text-embedding-ada-002 model with 1536 embedding dimensions."""
    openai_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('openai_key') }})
    mode: Optional[DestinationPineconeEmbeddingOpenAIMode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class DestinationPineconeEmbedding:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationPineconeIndexing:
    r"""Pinecone is a popular vector store that can be used to store and retrieve embeddings."""
    index: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('index') }})
    r"""Pinecone index to use"""
    pinecone_environment: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pinecone_environment') }})
    r"""Pinecone environment to use"""
    pinecone_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pinecone_key') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationPineconeProcessingConfigModel:
    chunk_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chunk_size') }})
    r"""Size of chunks in tokens to store in vector store (make sure it is not too big for the context if your LLM)"""
    chunk_overlap: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chunk_overlap'), 'exclude': lambda f: f is None }})
    r"""Size of overlap between chunks in tokens to store in vector store to better capture relevant context"""
    metadata_fields: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata_fields'), 'exclude': lambda f: f is None }})
    r"""List of fields in the record that should be stored as metadata. The field list is applied to all streams in the same way and non-existing fields are ignored. If none are defined, all fields are considered metadata fields. When specifying text fields, you can access nested fields in the record by using dot notation, e.g. `user.name` will access the `name` field in the `user` object. It's also possible to use wildcards to access all fields in an object, e.g. `users.*.name` will access all `names` fields in all entries of the `users` array. When specifying nested paths, all matching values are flattened into an array set to a field named by the path."""
    text_fields: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text_fields'), 'exclude': lambda f: f is None }})
    r"""List of fields in the record that should be used to calculate the embedding. The field list is applied to all streams in the same way and non-existing fields are ignored. If none are defined, all fields are considered text fields. When specifying text fields, you can access nested fields in the record by using dot notation, e.g. `user.name` will access the `name` field in the `user` object. It's also possible to use wildcards to access all fields in an object, e.g. `users.*.name` will access all `names` fields in all entries of the `users` array."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationPinecone:
    r"""The values required to configure the destination."""
    destination_type: DestinationPineconePinecone = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    embedding: Union[DestinationPineconeEmbeddingOpenAI, DestinationPineconeEmbeddingCohere, DestinationPineconeEmbeddingFake] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('embedding') }})
    r"""Embedding configuration"""
    indexing: DestinationPineconeIndexing = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('indexing') }})
    r"""Pinecone is a popular vector store that can be used to store and retrieve embeddings."""
    processing: DestinationPineconeProcessingConfigModel = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processing') }})
    
