🌀 StreamForge Lakehouse ETL
A Modular, Distributed, Real-Time Lakehouse ETL Architecture

StreamForge Lakehouse ETL is a fully componentized data platform designed to simulate and demonstrate how modern real-time data systems work.

It is built using a Lakehouse + Streaming ETL philosophy:

Real-time event ingestion

Stateful stream processing

Object-storage-based lakehouse

Table formats with ACID guarantees

Distributed SQL querying

Dashboarding & analytics

Everything is separated into independent modules, allowing clean scalability and a true production-like pipeline.

🔥 Key Architectural Features

True decoupling → Every service is isolated, replacing one does not affect others

Real-time streaming → Kafka → Flink → MinIO → Iceberg

Lakehouse governance → Iceberg ensures schema evolution + transactions

High-performance analytics → Trino runs federated SQL over lakehouse

Visual consumption layer → Superset connects directly to Trino

Infra-neutral → Works with local machine, cloud, containers, or Kubernetes

🧱 Core Component Matrix
| **Component**         | **Role**                         | **Technology**       | **Service Name**              | **Detailed Function**                                                                                     |
|------------------------|-----------------------------------|-----------------------|-------------------------------|-----------------------------------------------------------------------------------------------------------|
| **Messaging Bus**      | Event ingestion / buffering       | Apache Kafka          | `streaming-server`            | Handles real-time clickstream ingestion with durability, replication, and consumer-group distribution.    |
| **Processing Layer**   | Stateful stream ETL + enrichment  | Apache Flink          | `stream-processor`            | Performs transformations, filtering, joins, watermarking, windowing, and pushes results downstream.       |
| **Object Storage**     | Central lakehouse data layer      | MinIO                 | `minio-storage-service`       | S3-compatible durable storage base for raw → bronze → silver → gold datasets.                            |
| **Table Format**       | Governance + transactions         | Apache Iceberg        | `iceberg-catalog-svc`         | Adds ACID compliance, schema evolution, metadata tracking, partitioning & snapshot table management.      |
| **Query Engine**       | Distributed SQL analytics         | Trino                 | `query-engine`                | Executes fast SQL queries across Iceberg tables with connector-based federation.                         |
| **Visualization**      | Dashboards + BI                   | Apache Superset       | `viz-dashboard`               | Creates interactive dashboards, charts & analytics connected directly to Trino.                           |

🏗️ High-Level Architecture Flow
          ┌────────────────────┐
          │   Data Emitter     │
          │  (Clickstreams)    │
          └─────────┬──────────┘
                    ▼
          ┌────────────────────┐
          │   Kafka Broker     │
          │ (streaming-server) │
          └─────────┬──────────┘
                    ▼
          ┌────────────────────┐
          │   Flink Processor  │
          │  (ETL + Enrich)    │
          └─────────┬──────────┘
                    ▼
        ┌──────────────────────────┐
        │   MinIO Object Storage   │
        │ (Lakehouse raw → curated)│
        └──────────┬──────────────┘
                   ▼
        ┌──────────────────────────┐
        │  Iceberg Table Catalog   │
        │ (ACID + Schema + Metadata)│
        └──────────┬──────────────┘
                   ▼
        ┌──────────────────────────┐
        │         Trino            │
        │ (Distributed SQL Engine) │
        └──────────┬──────────────┘
                   ▼
        ┌──────────────────────────┐
        │     Superset BI          │
        │ (Dashboards & Analytics) │
        └──────────────────────────┘

📂 Repository Structure
streamforge-lakehouse-etl/
│
├── data-emitter/               → Scripts / services generating synthetic clickstream data
│
├── stream-processor/           → Real-time ETL via Apache Flink
│
├── query-engine/               → Trino configuration + connectors
│
├── viz-dashboard/              → Superset setup for dashboards & charts
│
├── orchestrator.yml            → Multi-service orchestration file
│
└── LICENSE                     → MIT open-source license

⚙️ Detailed Module Breakdown
🟦 1. Data Emitter

Simulates clickstreams, events, or logs.

Produces events to Kafka topics

Mimics user activity (page views, clicks, sessions)

Configurable load generation

Perfect for testing streaming workloads.

🟧 2. Stream Processor (Flink)

Handles real-time transformation:

Parse → validate → clean → enrich

Stateful computations

Event time windowing

Joins with side-input datasets

Writes curated streams to MinIO/Iceberg

🟨 3. MinIO (Data Lake Storage)

Stores:

Raw tier ("Bronze")

Clean/curated tier ("Silver")

Aggregated/reporting tier ("Gold")

Fully S3-compatible — interchangeable with AWS S3.

🟩 4. Iceberg Catalog

Provides actual Lakehouse functionality:

Versioned table snapshots

Schema evolution without rewrites

Partition spec evolution

Rollbacks / time travel

ACID transactions

🟪 5. Trino Query Engine

A distributed SQL engine used by:

Analysts

Dashboards

BI tools

Data scientists

Supports ANSI SQL + Iceberg connector.

🟫 6. Superset Dashboard

Visualization layer where you:

Build dashboards

Run ad-hoc queries

View real-time trend lines, KPIs

Connect charts → Trino → Iceberg

🚀 Getting Started
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

🧭 End-to-End Data Flow Example

Emitter generates clickstream events

Events go into Kafka

Flink ETL transforms + enriches them

Processed data lands in MinIO

Iceberg tables track versions and schema

Trino performs SQL analytics

Superset visualizes results

🛣️ Roadmap (Planned)

Kubernetes-native Helm charts

CI/CD automation for each module

Auto schema detection for Iceberg

Batch-layer integration (Spark)

Data quality checks (Great Expectations)

ML feature-store extension

Alerts + monitoring module

🤝 Contributing

Pull requests are welcome!
Before submitting:

Follow the folder/module structure

Add documentation when introducing new features

Keep services decoupled

📄 License

MIT License — free for all personal, academic, and commercial use.
