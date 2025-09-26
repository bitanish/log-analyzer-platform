# Log Analyzer Platform

A **real-time log aggregation and analysis platform** that ingests logs from multiple services, processes them, and provides a searchable dashboard for insights.

---

## 🚀 Features

* **Log Producers**: Services emit structured logs.
* **Log Ingestion**: Logs are streamed into Kafka for high-throughput handling.
* **Log Consumers**: Consumers process, enrich, and forward logs to storage.
* **Storage**: Logs stored in Elasticsearch for fast querying.
* **Query API**: FastAPI/Django backend for log queries.
* **Frontend Dashboard**: React-based UI for live log tailing, search, and charts.
* **Monitoring**: Prometheus + Grafana for ingestion rate, latency, and service health.

---

## 📂 Project Structure

```bash
log-analyzer-platform/
│
├── api_service/         # Query API service (FastAPI/Django)
├── config/              # Configurations for services
├── docker/              # Docker setup files
├── frontend/            # React dashboard (UI for logs)
├── log_consumer/        # Log consumer service (reads from Kafka)
├── log_producer/        # Log producer service (simulates/emits logs)
├── docker-compose.yml   # Orchestration for local setup
├── LICENSE
└── README.md
```

---

## ⚙️ Tech Stack

* **Streaming**: Apache Kafka
* **Backend**: FastAPI / Django
* **Storage**: Elasticsearch
* **Frontend**: React + Material UI
* **Monitoring**: Prometheus + Grafana
* **Deployment**: Docker, Docker Compose

---

## 🛠️ Setup & Installation

### 1. Clone Repository

```bash
git clone https://github.com/bitanish/log-analyzer-platform.git
cd log-analyzer-platform
```

### 2. Start Services (Docker Compose)

```bash
docker-compose up --build
```

### 3. Access Dashboard

* **Frontend**: `http://localhost:3000`
* **API Service**: `http://localhost:8000`
* **Grafana**: `http://localhost:3001`

---

## 📌 Roadmap

* [ ] Add user authentication
* [ ] Add alerting system for error thresholds
* [ ] Support multi-tenant logging
* [ ] Advanced search filters in dashboard

---

## 📜 License

MIT License – free to use and adapt.
