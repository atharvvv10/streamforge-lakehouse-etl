SET 'state.backend' = 'filesystem';
SET 'state.checkpointing.dir' = 's3://flink-checkpoints/path/';
SET 'execution.checkpointing.mode' = 'EXACTLY_ONCE';
SET 'execution.checkpointing.interval' = '30 seconds';
SET 'execution.checkpointing.min-pause' = '10s';
SET 'parallelism.default' = '4';
SET 'table.exec.mini-batch.enabled' = 'true';
SHOW JARS;
DROP CATALOG IF EXISTS primary_lakehouse_catalog;
CREATE CATALOG primary_lakehouse_catalog WITH (
    'type' = 'iceberg',
    'catalog-impl' = 'org.apache.iceberg.catalog.hadoop.HadoopCatalog',
    'warehouse' = 's3://warehouse/analytics_root',
    'io-impl' = 'org.apache.iceberg.aws.s3.S3FileIO',
    's3.endpoint' = 'http://minio:9000',
    's3.path-style-access' = 'true',
    'client.region' = 'eu-central-1',
    's3.access-key-id' = 'datalakeuser',
    's3.secret-access-key' = 'securekey'
);
USE CATALOG primary_lakehouse_catalog;
DROP TABLE IF EXISTS event_ingress_stream;
CREATE TABLE IF NOT EXISTS event_ingress_stream (
    unique_event_id STRING,
    customer_id STRING,
    activity_type STRING,
    source_url STRING,
    session_guid STRING,
    client_platform STRING,
    event_ts_utc TIMESTAMP_LTZ(3) METADATA FROM 'timestamp',
    location_data ROW<lat_coord DOUBLE, lon_coord DOUBLE>,
    transaction_value DOUBLE
) WITH (
    'connector' = 'kafka',
    'topic' = 'clickstream',
    'properties.bootstrap.servers' = 'kafka-broker:9092',
    'scan.startup.mode' = 'group-offsets',
    'format' = 'json',
    'json.ignore-parse-errors' = 'true',
    'json.timestamp-format.standard' = 'SQL'
);
CREATE DATABASE IF NOT EXISTS primary_lakehouse_catalog.marketing_events;
DROP TABLE IF EXISTS primary_lakehouse_catalog.marketing_events.processed_conversions;
CREATE TABLE primary_lakehouse_catalog.marketing_events.processed_conversions
WITH (
    'format' = 'avro',
    'write.upsert.enabled' = 'true'
)
AS
SELECT
    unique_event_id,
    customer_id,
    activity_type AS marketing_action,
    source_url,
    session_guid,
    client_platform AS platform,
    event_ts_utc,
    location_data.lat_coord AS customer_latitude,
    location_data.lon_coord AS customer_longitude,
    transaction_value AS revenue_usd
FROM event_ingress_stream
WHERE activity_type = 'purchase'
  AND transaction_value > 50.0;