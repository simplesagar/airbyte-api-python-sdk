# DestinationSnowflakeLoadingMethodAWSS3StagingEncryptionAESCBCEnvelopeEncryption

Staging data will be encrypted using AES-CBC envelope encryption.


## Fields

| Field                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                  | Required                                                                                                                                                                                                              | Description                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `encryption_type`                                                                                                                                                                                                     | [DestinationSnowflakeLoadingMethodAWSS3StagingEncryptionAESCBCEnvelopeEncryptionEncryptionType](../../models/shared/destinationsnowflakeloadingmethodawss3stagingencryptionaescbcenvelopeencryptionencryptiontype.md) | :heavy_check_mark:                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                   |
| `key_encrypting_key`                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                    | The key, base64-encoded. Must be either 128, 192, or 256 bits. Leave blank to have Airbyte generate an ephemeral key for each sync.                                                                                   |