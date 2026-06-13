# 📊 Prometheus & Grafana — Application Monitoring & Instrumentation

[![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)](https://prometheus.io/)
[![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)](https://grafana.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)

## 📚 About This Repository

This repository documents my hands-on experience building an **end-to-end application observability pipeline** using Prometheus and Grafana. I instrumented a Python Flask application with custom metrics from scratch, containerised it with Docker, deployed it on AWS EC2, and connected Grafana dashboards for real-time visualisation.

The project goes beyond infrastructure monitoring — it covers **application-level instrumentation**, which is what separates operational awareness from genuine observability. Every metric here is custom-defined inside the application code, not pulled from a node exporter.

## 🎯 What I Built

### Application Instrumentation

- ✅ Instrumented a Python Flask application with the `prometheus_client` library
- ✅ Defined custom metrics across all four Prometheus types: Counter, Gauge, Histogram, Summary
- ✅ Exposed a `/metrics` endpoint for Prometheus scraping
- ✅ Added `/health` and `/api/status` endpoints for application health reporting
- ✅ Tracked real application behaviour — request counts, response latency, uptime, active connections

### Containerisation

- ✅ Wrote a production-ready Dockerfile for the Flask application
- ✅ Built and tagged Docker image: `prometheus/custom_app_v1`
- ✅ Deployed container with `--restart always` policy for automatic recovery
- ✅ Configured port mapping for external scrape access

### Cloud Deployment

- ✅ Deployed containerised application on AWS EC2
- ✅ Configured AWS security groups to expose metrics endpoint on port 5001
- ✅ Pointed Prometheus scrape target to live EC2 instance
- ✅ Built Grafana dashboards connected to Prometheus data source
- ✅ Verified full pipeline: app → metrics endpoint → Prometheus → Grafana

## 📂 Repository Structure

```
prometheus_and_grafana/
├── Application_Instrument/     # Python Flask app instrumented with custom Prometheus metrics
├── docker_instrument/          # Dockerised version of the app — deployed on AWS EC2
└── Documentations/             # Notes, configuration references, and learning docs
```

### Application_Instrument/
Core Flask application with Prometheus instrumentation built in. Defines all custom metric types, exposes the `/metrics` endpoint, and runs locally for development and testing.

### docker_instrument/
Production-ready containerised version of the instrumented app. Includes the Dockerfile, built as `prometheus/custom_app_v1`, deployed on AWS EC2 with `--restart always` and port mapping `-p 5001:5001`.

### Documentations/
Setup guides, Prometheus configuration references, PromQL query notes, Grafana dashboard setup steps, and debugging notes from the build process.

## 🛠️ Technologies Used

- **Prometheus** — Metrics collection, scraping, and time-series storage
- **Grafana** — Dashboard visualisation and data querying
- **Python 3** — Application language
- **Flask** — Web framework for the instrumented application
- **prometheus_client** — Python library for defining and exposing custom metrics
- **Docker** — Application containerisation and image management
- **AWS EC2** — Cloud deployment platform
- **Ubuntu 24.04 LTS** — Operating system

## 💪 Skills Gained

### Prometheus Metric Types Mastered

```python
# Counter — tracks values that only increase (requests, errors, events)
REQUEST_COUNT = Counter(
    'flask_request_count',
    'Total HTTP Requests',
    ['method', 'endpoint', 'status']
)

# Gauge — tracks values that go up and down (active connections, queue size)
ACTIVE_REQUESTS = Gauge(
    'flask_active_requests',
    'Active HTTP Requests currently in progress'
)

# Histogram — tracks distribution of observed values (request duration buckets)
REQUEST_LATENCY = Histogram(
    'flask_request_latency_seconds',
    'HTTP Request Latency in seconds',
    ['endpoint']
)

# Summary — tracks quantiles over a sliding time window (p50, p95, p99)
REQUEST_SIZE = Summary(
    'flask_request_size_bytes',
    'HTTP Request Size in bytes'
)
```

### Prometheus Concepts Mastered

```
Scrape interval         # How often Prometheus pulls metrics
Targets                 # Endpoints Prometheus monitors
Labels                  # Key-value pairs that add context to metrics
PromQL                  # Query language for filtering and aggregating metrics
Data model              # Time-series with metric name + label set
Cardinality             # Number of unique label combinations — bounded vs unbounded
```

### Problems I Solved

**1. Metrics Endpoint Returning 404**

- ❌ Flask app running but `/metrics` returning 404
- ✅ Added `make_wsgi_app()` dispatcher and mounted correctly as a Flask route
- ✅ Understood how Prometheus expects the endpoint to be exposed

**2. Prometheus Not Scraping the EC2 Container**

- ❌ Prometheus showing target as DOWN despite container running
- ✅ Identified missing inbound rule in AWS security group for port 5001
- ✅ Added the rule and confirmed target went green in Prometheus UI

**3. Container Stopping After EC2 Deployment**

- ❌ Container exiting on SSH disconnect
- ✅ Added `-d` detach flag and `--restart always` restart policy
- ✅ Verified with `docker ps` that container persisted after logout

**4. Grafana Dashboard Showing No Data**

- ❌ Prometheus data source connected but all panels empty
- ✅ Verified Prometheus target was actively scraping (checked `/targets`)
- ✅ Corrected PromQL queries to use actual metric names from `/metrics`
- ✅ Adjusted time range window to match when scraping started

**5. High Cardinality Warning**

- ❌ Initial label design included unbounded values (user IDs, full URLs)
- ✅ Redesigned labels to use bounded sets (method, endpoint group, status code)
- ✅ Understood why cardinality explosion is a production anti-pattern

## 🏆 Project Outcomes

### Application_Instrument — Local Development

**What I Did:**
- Built Python Flask app with multiple instrumented endpoints
- Defined Counter, Gauge, Histogram, and Summary metric types
- Exposed `/metrics`, `/health`, and `/api/status` endpoints
- Validated metric output by curling the endpoint directly

**Result:**
- ✅ Custom application metrics visible in Prometheus format at `/metrics`
- ✅ Request counts, active connections, and latency tracked per endpoint
- ✅ Health and status endpoints returning structured JSON responses
- ✅ All four Prometheus metric types implemented and verified

### docker_instrument — Deployed on AWS EC2

**What I Did:**
- Wrote Dockerfile using `python:3.9-slim` as base image
- Built and tagged image as `prometheus/custom_app_v1:latest`
- Deployed on AWS EC2 with port mapping `-p 5001:5001` and `--restart always`
- Configured Prometheus `prometheus.yml` to scrape the EC2 target
- Built Grafana dashboard with panels for request rate, error rate, and response latency

**Result:**
- ✅ Containerised app running persistently on EC2 across reboots
- ✅ Prometheus scraping live metrics from EC2 instance on port 5001
- ✅ Grafana dashboards showing real-time application metrics
- ✅ Full observability pipeline operational end-to-end

## 📈 Project Stats

**Metric Types Implemented:** 4 (Counter, Gauge, Histogram, Summary)  
**Custom Metrics Defined:** 5+  
**Deployment Platform:** AWS EC2  
**Container Image:** `prometheus/custom_app_v1:latest`  
**Application Port:** 5001  
**Errors Debugged:** 5+  
**Concepts Mastered:** 30+

## 🔐 Security Practices Followed

- ✅ No hardcoded credentials in application code or Dockerfile
- ✅ AWS security group inbound rules scoped to required ports only
- ✅ Environment variables used for all configurable values
- ✅ Docker image built from minimal base (`python:3.9-slim`)
- ✅ `.gitignore` configured to exclude sensitive configuration files

## 🎓 Key Takeaways

### Why Application Instrumentation Matters

Generic system metrics — CPU, RAM, disk — tell you the machine is alive. They do not tell you the application is healthy. Custom application metrics expose what your code is actually doing: how many requests it's handling, how fast it's responding, where it's failing, and what's happening inside the process at any given moment.

Instrumenting at the application level is the difference between knowing a server is up and knowing your service is working.

### The Full Observability Pipeline

```
Flask Application
       │
       ▼
/metrics endpoint  ←── prometheus_client library exposes metrics here
       │
       ▼
Prometheus Server  ←── scrapes /metrics every N seconds, stores time-series
       │
       ▼
Grafana Dashboard  ←── queries Prometheus via PromQL, visualises in real time
```

### Real-World Application

This knowledge directly applies to:

- Production application monitoring and alerting in DevOps and SRE roles
- SLA and error-rate reporting backed by real application data
- Debugging latency issues using Histogram bucket analysis
- Building observability into CI/CD pipelines before code hits production
- Integrating with Alertmanager for automated incident notifications

## 🤝 Contributing

This is a personal learning repository. Feel free to fork and use for your own learning journey.

---

⭐ **Star this repo if you're building your own monitoring stack!**

