# 🌀 StreamForge Lakehouse ETL
A Modular, Distributed, Real-Time Lakehouse ETL Architecture

StreamForge Lakehouse ETL is a fully componentized data platform designed to simulate and demonstrate how modern real-time data systems work.

It is built using a Lakehouse + Streaming ETL philosophy:

1. Real-time event ingestion

2. Stateful stream processing

3. Object-storage-based lakehouse

4. Table formats with ACID guarantees

5. Distributed SQL querying

6. Dashboarding & analytics

Everything is separated into independent modules, allowing clean scalability and a true production-like pipeline.

## 🔥 Key Architectural Features

True decoupling → Every service is isolated, replacing one does not affect others

Real-time streaming → Kafka → Flink → MinIO → Iceberg

Lakehouse governance → Iceberg ensures schema evolution + transactions

High-performance analytics → Trino runs federated SQL over lakehouse

Visual consumption layer → Superset connects directly to Trino

Infra-neutral → Works with local machine, cloud, containers, or Kubernetes

## 🧱 Core Component Matrix
| **Component**         | **Role**                         | **Technology**       | **Service Name**              | **Detailed Function**                                                                                     |
|------------------------|-----------------------------------|-----------------------|-------------------------------|-----------------------------------------------------------------------------------------------------------|
| **Messaging Bus**      | Event ingestion / buffering       | Apache Kafka          | `streaming-server`            | Handles real-time clickstream ingestion with durability, replication, and consumer-group distribution.    |
| **Processing Layer**   | Stateful stream ETL + enrichment  | Apache Flink          | `stream-processor`            | Performs transformations, filtering, joins, watermarking, windowing, and pushes results downstream.       |
| **Object Storage**     | Central lakehouse data layer      | MinIO                 | `minio-storage-service`       | S3-compatible durable storage base for raw → bronze → silver → gold datasets.                            |
| **Table Format**       | Governance + transactions         | Apache Iceberg        | `iceberg-catalog-svc`         | Adds ACID compliance, schema evolution, metadata tracking, partitioning & snapshot table management.      |
| **Query Engine**       | Distributed SQL analytics         | Trino                 | `query-engine`                | Executes fast SQL queries across Iceberg tables with connector-based federation.                         |
| **Visualization**      | Dashboards + BI                   | Apache Superset       | `viz-dashboard`               | Creates interactive dashboards, charts & analytics connected directly to Trino.                           |

## 📂 Repository Structure
```bash
streamforge-lakehouse-etl/
│
├── data-emitter/
│   ├── Dockerfile
│   ├── producer.py
│   └── requirements.txt
│
├── query-engine/
│   └── iceberg.properties
│
├── stream-processor/
│   ├── sql-client/
│   │   ├── Dockerfile
│   │   └── flink-conf.yaml
│   │
│   └── sql-jobs/
│       └── clickstream-filtering.sql
│
├── viz-dashboard/
│   ├── Dockerfile
│   ├── superset_config.py
│   └── superset-init.sh
│
├── orchestrator.yml
├── LICENSE
└── README.md
```
## ⚙️ Detailed Module Breakdown
🟦 1. Data Emitter

- Simulates clickstreams, events, or logs.

- Produces events to Kafka topics

- Mimics user activity (page views, clicks, sessions)

- Configurable load generation

- Perfect for testing streaming workloads.

🟧 2. Stream Processor (Flink)

- Handles real-time transformation:

- Parse → validate → clean → enrich

- Stateful computations

- Event time windowing

- Joins with side-input datasets

- Writes curated streams to MinIO/Iceberg

🟨 3. MinIO (Data Lake Storage)

Stores:

- Raw tier ("Bronze")

- Clean/curated tier ("Silver")

- Aggregated/reporting tier ("Gold")

- Fully S3-compatible — interchangeable with AWS S3.

🟩 4. Iceberg Catalog

- Provides actual Lakehouse functionality:

- Versioned table snapshots

- Schema evolution without rewrites

- Partition spec evolution

- Rollbacks / time travel

- ACID transactions

🟪 5. Trino Query Engine

A distributed SQL engine used by:

- Analysts

- Dashboards

- BI tools

- Data scientists

- Supports ANSI SQL + Iceberg connector.

🟫 6. Superset Dashboard

Visualization layer where you:

- Build dashboards

- Run ad-hoc queries

- View real-time trend lines, KPIs

- Connect charts → Trino → Iceberg

## 🚀 Getting Started
```bash
1️⃣ Clone the repository

git clone https://github.com/atharvvv10/streamforge-lakehouse-etl.git
cd streamforge-lakehouse-etl

2️⃣ Set up environment variables

(If required by MinIO, Iceberg, Trino)

3️⃣ Start services

Depending on orchestration method:

Docker Compose

Kubernetes

Manual startup

The orchestrator.yml acts as your blueprint.
```

## 🧭 End-to-End Data Flow Example

1. Emitter generates clickstream events

2. Events go into Kafka

3. Flink ETL transforms + enriches them

4. Processed data lands in MinIO

5. Iceberg tables track versions and schema

6. Trino performs SQL analytics

7. Superset visualizes results

## 🛣️ Roadmap (Planned)

1. Kubernetes-native Helm charts

2. CI/CD automation for each module

3. Auto schema detection for Iceberg

4. Batch-layer integration (Spark)

5. Data quality checks (Great Expectations)

6. ML feature-store extension

7. Alerts + monitoring module

## 🤝 Contributing

Pull requests are welcome!
Before submitting:

- Follow the folder/module structure

- Add documentation when introducing new features

- Keep services decoupled

## 📄 License

MIT License — free for all personal, academic, and commercial use.
