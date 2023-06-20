# DestinationSnowflake

The values required to configure the destination.


## Fields

| Field                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `credentials`                                                                                                                                                                                                                                                                                   | *Optional[Any]*                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                 |
| `database`                                                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                                              | Enter the name of the <a href="https://docs.snowflake.com/en/sql-reference/ddl-database.html#database-schema-share-ddl">database</a> you want to sync data into                                                                                                                                 | AIRBYTE_DATABASE                                                                                                                                                                                                                                                                                |
| `destination_type`                                                                                                                                                                                                                                                                              | [DestinationSnowflakeSnowflake](../../models/shared/destinationsnowflakesnowflake.md)                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                 |
| `file_buffer_count`                                                                                                                                                                                                                                                                             | *Optional[int]*                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                              | Number of file buffers allocated for writing data. Increasing this number is beneficial for connections using Change Data Capture (CDC) and up to the number of streams within a connection. Increasing the number of file buffers past the maximum number of streams has deteriorating effects | 10                                                                                                                                                                                                                                                                                              |
| `host`                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                                              | Enter your Snowflake account's <a href="https://docs.snowflake.com/en/user-guide/admin-account-identifier.html#using-an-account-locator-as-an-identifier">locator</a> (in the format <account_locator>.<region>.<cloud>.snowflakecomputing.com)                                                 | accountname.us-east-2.aws.snowflakecomputing.com                                                                                                                                                                                                                                                |
| `jdbc_url_params`                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                              | Enter the additional properties to pass to the JDBC URL string when connecting to the database (formatted as key=value pairs separated by the symbol &). Example: key1=value1&key2=value2&key3=value3                                                                                           |                                                                                                                                                                                                                                                                                                 |
| `loading_method`                                                                                                                                                                                                                                                                                | *Optional[Any]*                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                              | Select a data staging method                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                 |
| `role`                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                                              | Enter the <a href="https://docs.snowflake.com/en/user-guide/security-access-control-overview.html#roles">role</a> that you want to use to access Snowflake                                                                                                                                      | AIRBYTE_ROLE                                                                                                                                                                                                                                                                                    |
| `schema`                                                                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                                              | Enter the name of the default <a href="https://docs.snowflake.com/en/sql-reference/ddl-database.html#database-schema-share-ddl">schema</a>                                                                                                                                                      | AIRBYTE_SCHEMA                                                                                                                                                                                                                                                                                  |
| `username`                                                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                                              | Enter the name of the user you want to use to access the database                                                                                                                                                                                                                               | AIRBYTE_USER                                                                                                                                                                                                                                                                                    |
| `warehouse`                                                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                                              | Enter the name of the <a href="https://docs.snowflake.com/en/user-guide/warehouses-overview.html#overview-of-warehouses">warehouse</a> that you want to sync data into                                                                                                                          | AIRBYTE_WAREHOUSE                                                                                                                                                                                                                                                                               |