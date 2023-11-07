# DocArrayHnswSearch

DocArrayHnswSearch is a lightweight Document Index implementation provided by Docarray that runs fully locally and is best suited for small- to medium-sized datasets. It stores vectors on disk in hnswlib, and stores all other data in SQLite.


## Fields

| Field                                                                                                                                                                                                    | Type                                                                                                                                                                                                     | Required                                                                                                                                                                                                 | Description                                                                                                                                                                                              | Example                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `destination_path`                                                                                                                                                                                       | *str*                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                       | Path to the directory where hnswlib and meta data files will be written. The files will be placed inside that local mount. All files in the specified destination directory will be deleted on each run. | /local/my_hnswlib_index                                                                                                                                                                                  |
| `mode`                                                                                                                                                                                                   | [Optional[shared.DestinationLangchainSchemasIndexingMode]](../../models/shared/destinationlangchainschemasindexingmode.md)                                                                               | :heavy_minus_sign:                                                                                                                                                                                       | N/A                                                                                                                                                                                                      |                                                                                                                                                                                                          |