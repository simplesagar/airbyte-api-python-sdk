# DestinationPulsar

The values required to configure the destination.


## Fields

| Field                                                                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                              | Example                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `batching_enabled`                                                                                                                                                                                                                                                                                       | *bool*                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | Control whether automatic batching of messages is enabled for the producer.                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                          |
| `batching_max_messages`                                                                                                                                                                                                                                                                                  | *int*                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | Maximum number of messages permitted in a batch.                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                          |
| `batching_max_publish_delay`                                                                                                                                                                                                                                                                             | *int*                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                       |  Time period in milliseconds within which the messages sent will be batched.                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                          |
| `block_if_queue_full`                                                                                                                                                                                                                                                                                    | *bool*                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | If the send operation should block when the outgoing message queue is full.                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                          |
| `brokers`                                                                                                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | A list of host/port pairs to use for establishing the initial connection to the Pulsar cluster.                                                                                                                                                                                                          | broker1:6650,broker2:6650                                                                                                                                                                                                                                                                                |
| `compression_type`                                                                                                                                                                                                                                                                                       | [DestinationPulsarCompressionType](../../models/shared/destinationpulsarcompressiontype.md)                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | Compression type for the producer.                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                          |
| `destination_type`                                                                                                                                                                                                                                                                                       | [DestinationPulsarPulsar](../../models/shared/destinationpulsarpulsar.md)                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | N/A                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                          |
| `max_pending_messages`                                                                                                                                                                                                                                                                                   | *int*                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | The maximum size of a queue holding pending messages.                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                          |
| `max_pending_messages_across_partitions`                                                                                                                                                                                                                                                                 | *int*                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | The maximum number of pending messages across partitions.                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                          |
| `producer_name`                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                       | Name for the producer. If not filled, the system will generate a globally unique name which can be accessed with.                                                                                                                                                                                        | airbyte-producer                                                                                                                                                                                                                                                                                         |
| `producer_sync`                                                                                                                                                                                                                                                                                          | *Optional[bool]*                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                       | Wait synchronously until the record has been sent to Pulsar.                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                          |
| `send_timeout_ms`                                                                                                                                                                                                                                                                                        | *int*                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | If a message is not acknowledged by a server before the send-timeout expires, an error occurs (in ms).                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                          |
| `topic_namespace`                                                                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | The administrative unit of the topic, which acts as a grouping mechanism for related topics. Most topic configuration is performed at the namespace level. Each tenant has one or multiple namespaces.                                                                                                   | default                                                                                                                                                                                                                                                                                                  |
| `topic_pattern`                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | Topic pattern in which the records will be sent. You can use patterns like '{namespace}' and/or '{stream}' to send the message to a specific topic based on these values. Notice that the topic name will be transformed to a standard naming convention.                                                | sample.topic                                                                                                                                                                                                                                                                                             |
| `topic_tenant`                                                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | The topic tenant within the instance. Tenants are essential to multi-tenancy in Pulsar, and spread across clusters.                                                                                                                                                                                      | public                                                                                                                                                                                                                                                                                                   |
| `topic_test`                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                       | Topic to test if Airbyte can produce messages.                                                                                                                                                                                                                                                           | test.topic                                                                                                                                                                                                                                                                                               |
| `topic_type`                                                                                                                                                                                                                                                                                             | [DestinationPulsarTopicType](../../models/shared/destinationpulsartopictype.md)                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | It identifies type of topic. Pulsar supports two kind of topics: persistent and non-persistent. In persistent topic, all messages are durably persisted on disk (that means on multiple disks unless the broker is standalone), whereas non-persistent topic does not persist message into storage disk. |                                                                                                                                                                                                                                                                                                          |
| `use_tls`                                                                                                                                                                                                                                                                                                | *bool*                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | Whether to use TLS encryption on the connection.                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                          |