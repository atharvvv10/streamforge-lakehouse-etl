# 🚀 StreamForge Lakehouse ETL
Modular, Scalable & Real-Time Lakehouse ETL Pipeline

streamforge-lakehouse-etl is a fully modular ETL framework designed for building modern Lakehouse + Streaming Data Pipelines.
Each component is decoupled into its own service so you can scale, replace, or extend parts independently — like a real production-grade data system.

## 🧱 Core Components Overview
| **Core Component**    | **Role**                        | **Technology**      | **Implementation (New Name)** | **Function**                                                     |
|------------------------|----------------------------------|----------------------|-------------------------------|------------------------------------------------------------------|
| **Messaging Bus**      | Event Ingestion & Decoupling     | Apache Kafka         | `streaming-server`            | Decoupled, fault-tolerant ingestion of real-time events.         |
| **Processing Layer**   | Stateful Stream Processing       | Apache Flink         | `stream-processor`            | Real-time ETL, filtering, transformation, and enrichment.        |
| **Object Storage**     | Persistent Data Lake Storage     | MinIO                | `minio-storage-service`       | S3-compatible object storage for raw + processed datasets.       |
| **Table Format**       | Lakehouse Table Management       | Apache Iceberg       | `iceberg-catalog-svc`         | Schema evolution + ACID transactions for lakehouse tables.       |
| **SQL Access**         | Distributed Query Engine         | Trino                | `query-engine`                | High-performance SQL querying over Iceberg tables.               |
| **Visualization**      | BI & Dashboarding               | Apache Superset      | `viz-dashboard`               | Interactive dashboards + visual analytics.                       |

## 📦 Project Structure
streamforge-lakehouse-etl/
│
├── data-emitter/           # Simulated or real data ingestion layer
├── stream-processor/       # Real-time streaming ETL logic
├── query-engine/           # SQL query engine configuration (Trino)
├── viz-dashboard/          # Dashboarding & BI (Superset)
├── orchestrator.yml        # Full system orchestration
└── LICENSE                 # MIT License

## 🎯 Objective

To build a production-style data pipeline that supports:

Real-time event ingestion

Stateful stream processing

Lakehouse-style storage & governance

SQL analytics engine

Dashboarding for insights

All packaged into clear, modular components.

## ⚙️ Getting Started
```bash
1️⃣ Clone the Repository
git clone https://github.com/atharvvv10/streamforge-lakehouse-etl.git
cd streamforge-lakehouse-etl

2️⃣ Start Individual Modules

Each folder is self-contained.
Typical workflow:

🔹 Start Kafka (streaming-server)

Produces and receives real-time clickstream/events.

🔹 Start Flink (stream-processor)

Applies ETL transforms, filtering, enrichment.

🔹 Start MinIO + Iceberg

Acts as your object store & table catalog.

🔹 Start Trino (query-engine)

Allows you to query Iceberg tables using SQL.

🔹 Start Superset (viz-dashboard)

Connects to Trino for dashboarding.

All services can be controlled through orchestrator.yml.
```

## 🧩 Why This Architecture?

🔄 Decoupled microservices → scalable & replaceable

⚡ Real-time ETL → immediate transformations

🧊 Lakehouse support via Iceberg → ACID + schema evolution

🔍 Interactive SQL queries → Trino for fast analytics

📊 Dashboards → complete end-to-end visibility

This mirrors real-world modern data engineering setups.

## 🛣️ Roadmap / Future Features

Support for Delta Lake or Apache Hudi

Fully dockerized version

CI/CD integration

Automated schema registry

Orchestrator upgrade (Airflow / Dagster)

Machine learning feature-store layer

## 🤝 Contributing

PRs are welcome!

Fork

Create feature branch

Commit changes

Open PR

## 📄 License

This project is licensed under the MIT License.
