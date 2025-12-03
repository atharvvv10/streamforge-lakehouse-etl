I. OBJECTIVE & ARCHITECTURAL OVERVIEW
-------------------------------------
StreamForge is a complete, production-style, real-time data
lakehouse architecture designed to ingest, process, store,
query, and visualize streaming clickstream events.

Core Components:
----------------
Component            Technology        Service Name
------------------------------------------------------------
Messaging Bus        Apache Kafka      streaming-server
Processing Layer     Apache Flink      stream-processor
Object Storage       MinIO             minio-storage-service
Table Format         Apache Iceberg    iceberg-catalog-svc
Query Engine         Trino             query-engine
Visualization        Apache Superset   viz-dashboard

Purpose Summary:
----------------
- Kafka: High-throughput event streaming layer
- Flink: Real-time ETL, filtering and stateful processing
- MinIO: S3-compatible persistent object store
- Iceberg: ACID table management with schema evolution
- Trino: High-speed SQL engine over Iceberg
- Superset: Visualization and dashboarding interface

------------------------------------------------------------

II. PROJECT FILE STRUCTURE
---------------------------
streamforge-analytics/
│
├── data-emitter/                     (Clickstream generator)
│     ├── stream_source.py
│     ├── python_deps.txt
│     └── Dockerfile
│
├── stream-processor/                 (Flink transformations)
│     ├── sql-client/
│     │     ├── flink_runtime.yaml
│     │     └── cli_builder.Dockerfile
│     └── sql-jobs/
│           └── transform_pipeline.sql
│
├── query-engine/                     (Trino-Iceberg config)
│     └── iceberg_catalog.properties
│
├── viz-dashboard/                    (Superset setup)
│     ├── web_config.py
│     ├── init_superuser.sh
│     └── viz_app.docker
│
├── orchestrator.yml                  (Master docker-compose)
└── COPYRIGHT.txt                     (MIT License)

------------------------------------------------------------

III. ENVIRONMENT SETUP
-----------------------

PREREQUISITES:
--------------
- Docker installed
- Docker Compose v2+
- 16GB RAM recommended

SETUP STEPS:
------------

Step 1: Clone the repository
----------------------------
git clone <your-repo-url>
cd streamforge-analytics

Step 2: Launch all microservices
--------------------------------
docker compose -f orchestrator.yml up --build -d

------------------------------------------------------------

IV. SERVICE ENDPOINTS
----------------------

Service                    Container Name          URL
------------------------------------------------------------
Flink Dashboard            stream-job-master       http://localhost:8084
MinIO Console              object-storage-svc      http://localhost:9002
Trino Web UI               trino-query-server      http://localhost:8889
Superset (Visualization)   data-visualization-app  http://localhost:9099

Credentials:
------------
MinIO:      minio-admin / minio-password-1
Superset:   viz_master / superstrongpassword

------------------------------------------------------------

V. DATA PROCESSING FLOW
------------------------

A. Event Generation
-------------------
File: data-emitter/stream_source.py
Function:
- Generates synthetic events (page views, clicks, purchases)
- Pushes JSON messages to Kafka topic: user-activity-stream

B. Real-Time ETL via Flink
---------------------------
File: stream-processor/sql-jobs/transform_pipeline.sql
Flow:
- Reads incoming Kafka JSON stream
- Extracts only successful purchase events
- Filters revenue > 50
- Writes cleaned data into an Iceberg table stored in MinIO

C. Querying Processed Data
---------------------------
Enter Trino:
docker compose -f orchestrator.yml exec query-engine trino --user analytics_user

Run SQL:
USE iceberg_data_lake.marketing_events;
SELECT * FROM processed_conversions LIMIT 5;

------------------------------------------------------------

VI. PROJECT METADATA
---------------------
License: MIT License (see COPYRIGHT.txt)
Author : Atharv Chougale (© 2025)
Project: StreamForge Analytics Platform
