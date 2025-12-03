🚀 StreamForge Analytics Platform
Real-Time Data Lakehouse for High-Velocity Event Streams
🎯 I. Objective & Architectural Overview

StreamForge is a modern, production-ready Real-Time Data Lakehouse engineered for continuous ingestion, low-latency streaming transformations, scalable object storage, and distributed analytics.

Below is the fully bordered architecture table:

+---------------------+-------------------+----------------------------+---------------------------------------------------------------+
| Core Component      | Technology        | Service Name               | Purpose                                                       |
+---------------------+-------------------+----------------------------+---------------------------------------------------------------+
| Messaging Bus       | Apache Kafka      | streaming-server           | High-throughput, persistent event ingestion                  |
| Processing Layer    | Apache Flink      | stream-processor           | Stateful real-time ETL, filtering, enrichment                |
| Object Storage      | MinIO             | minio-storage-service      | S3-compatible durable storage                                |
| Table Format        | Apache Iceberg    | iceberg-catalog-svc        | ACID transactions, schema evolution, time travel             |
| SQL Query Engine    | Trino             | query-engine               | Distributed SQL execution on top of Iceberg tables           |
| Visualization Layer | Apache Superset   | viz-dashboard              | Dashboards, analytics exploration, BI capabilities           |
+---------------------+-------------------+----------------------------+---------------------------------------------------------------+

📂 II. Project File Structure
streamforge-analytics/
├── data-emitter/                 
│   ├── stream_source.py
│   ├── python_deps.txt
│   └── Dockerfile
│
├── stream-processor/             
│   ├── sql-client/
│   │   ├── flink_runtime.yaml
│   │   └── cli_builder.Dockerfile
│   └── sql-jobs/
│       └── transform_pipeline.sql
│
├── query-engine/                 
│   └── iceberg_catalog.properties
│
├── viz-dashboard/                
│   ├── web_config.py
│   ├── init_superuser.sh
│   └── viz_app.docker
│
├── orchestrator.yml              
└── COPYRIGHT.txt                 

🛠️ III. Environment Setup
Prerequisites
+------------------------+
|   REQUIRED SOFTWARE    |
+------------------------+
| Docker Desktop / Engine|
| Docker Compose v2+     |
| >= 16GB RAM recommended|
+------------------------+

1. Clone the Repository
git clone <your-repo-url>
cd streamforge-analytics

2. Launch Entire Platform
docker compose -f orchestrator.yml up --build -d

🌐 IV. Access Endpoints
+-------------------------+--------------------------+-------------------------------+-------------------------------+
| Service                 | Container Name           | URL                           | Credentials                  |
+-------------------------+--------------------------+-------------------------------+-------------------------------+
| Flink Job Manager UI    | stream-job-master        | http://localhost:8084         | None                         |
| MinIO Console           | object-storage-svc       | http://localhost:9002         | minio-admin / minio-password-1|
| Trino Web UI           | trino-query-server       | http://localhost:8889         | None                         |
| Superset Dashboard      | data-visualization-app   | http://localhost:9099         | viz_master / superstrongpassword |
+-------------------------+--------------------------+-------------------------------+-------------------------------+

🌊 V. Data Processing Flow
A. Event Generation — data-emitter/stream_source.py
+-------------------------------------------+
|   STREAM EVENT TYPES GENERATED            |
+-------------------------------------------+
| • Page Views                              |
| • Product Clicks                          |
| • Add-To-Cart Events                      |
| • Checkout Initiation                     |
| • Purchase Events                         |
+-------------------------------------------+


Synthetic JSON events → published to Kafka topic:
user-activity-stream

B. Real-Time ETL — Flink SQL

Flink performs:

+---------------------------------------------------------------+
|                    FLINK ETL PIPELINE                        |
+---------------------------------------------------------------+
| SOURCE: Kafka topic 'user-activity-stream'                    |
| TRANSFORM: Filter purchases where transaction_value > 50      |
| SINK: Write into Iceberg table (Avro format via MinIO)        |
+---------------------------------------------------------------+

C. Querying Iceberg Tables (via Trino)

Access Trino shell:

docker compose -f orchestrator.yml exec query-engine trino --user analytics_user


Run SQL:

USE iceberg_data_lake.marketing_events;

SELECT *
FROM processed_conversions
LIMIT 5;

📜 VI. Project Metadata
+----------------------+----------------------------------------+
| Field                | Details                                |
+----------------------+----------------------------------------+
| License              | MIT License (see COPYRIGHT.txt)        |
| Author               | Atharv Chougale © 2025                 |
| Project              | StreamForge Analytics Platform         |
+----------------------+----------------------------------------+

