# Food Delivery Pipeline & Monitoring Dashboard

This project simulates a **real‑time food delivery analytics platform**.  
Built end‑to‑end with Docker, Apache Airflow, PostgreSQL, and Apache Superset.

## 🚀 Quick Start
```bash
git clone https://github.com/yourname/food-delivery-pipeline-dashboard.git
cd food-delivery-pipeline-dashboard
make build-up   # starts Postgres, Airflow, Superset
```

- Airflow: <http://localhost:8080> (admin / admin)
- Superset: <http://localhost:8088> (admin / admin)

## 📊 KPIs Tracked
| Metric | Description |
|--------|-------------|
| **Total Deliveries** | Count of deliveries completed per hour/day |
| **Average Delivery Time** | Mean time (minutes) between pickup and drop‑off |
| **Cancellation Rate** | % of deliveries marked `is_cancelled = TRUE` |
| **On‑time Delivery %** | % delivered in ≤ 30 min |

## 🗄️ Tech Stack
- **Apache Airflow** 2.9 (LocalExecutor) orchestrates ETL
- **PostgreSQL** 15 stores raw & analytic tables
- **Apache Superset** 3.0 visualizes dashboards
- **Pandas**, **SQLAlchemy**, **Faker** for synthetic data
- **Docker Compose** for one‑command deployment

## 📂 Project Structure
```
.
├── dags/                   # Airflow DAGs
│   └── food_delivery_etl.py
├── data_generation/
│   └── generate_data.py    # bulk data generator
├── sql/
│   └── init.sql            # schema creation
├── docker-compose.yml
├── Makefile
└── README.md
```

## ✨ Dashboard
Once Superset is running:
1. Sign in (`admin/admin`)
2. Connect to the `food_delivery` Postgres database
3. Import `preload_dashboard.json` *(coming soon)* or build charts:
   - Table: `deliveries`
   - Charts: Delivery Trend, Avg. Delivery Time, Cancellation %
4. Save as **Food Delivery Monitoring**.

---

> **Author:** Adapted for food delivery by *Dhriti Sundar Saha* (2025)  
> Original inspiration: Abraham Koloboe’s e‑commerce data pipeline

