# Real-Time Food Order Data Pipeline

## Overview
This project is a small end-to-end real-time data engineering POC for a food delivery order tracking use case.

It simulates order events flowing through a streaming pipeline:

**Producer → Kafka → Consumer → SQLite → Streamlit Dashboard**

## Architecture
- **Producer**: Simulates food order events
- **Kafka**: Ingests and stores streaming events
- **Consumer**: Reads events, applies transformations, and writes processed data
- **SQLite**: Acts as the serving layer
- **Streamlit**: Displays live order and revenue metrics

## Tech Stack
- Python
- Apache Kafka
- SQLite
- Streamlit
- Docker

## Features
- Real-time order event ingestion
- Kafka-based event streaming
- Continuous consumer processing
- Idempotent storage using primary key + insert/replace
- Live dashboard for order tracking and metrics

## How to Run

### 1. Start Kafka
```bash
docker compose up -d
