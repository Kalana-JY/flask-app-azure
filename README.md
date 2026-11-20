# End-to-End DevOps Pipeline

A complete DevOps home-lab project demonstrating CI/CD automation, containerization, infrastructure deployment, Kubernetes orchestration, monitoring, and troubleshooting practices.

## Project Overview

This project implements an end-to-end DevOps workflow for a Flask-based To-Do API. The application is developed, tested, containerized, deployed, monitored, and maintained using modern DevOps tools and practices.

The pipeline covers the entire software delivery lifecycle:

- Source Control with Git and Azure Repos
- Pull Request Validation
- Automated CI/CD using Azure Pipelines
- Docker Containerization
- Linux VM Deployment using Systemd and Nginx
- Kubernetes Deployment with Minikube
- Windows IIS Frontend Deployment
- Monitoring with Prometheus and Grafana
- Incident Troubleshooting

---

## Architecture

```text
Developer
    │
    ▼
Azure Repos
    │
    ▼
Pull Request Validation
    │
    ▼
Azure Pipeline
    │
    ├── Unit Tests (PyTest)
    ├── Docker Build
    ├── Docker Push (Docker Hub)
    │
    ▼
Deployment Stages
    │
    ├── Linux VM
    │      ├── Systemd
    │      └── Nginx
    │
    ├── Kubernetes (Minikube)
    │
    └── Windows IIS Frontend
           │
           ▼
Monitoring Stack
    ├── Prometheus
    ├── Node Exporter
    └── Grafana
```

## Technology Stack

### Application
- Python 3.11
- Flask
- SQLite
- Gunicorn

### Source Control & CI/CD
- Git
- Azure Repos
- Azure Pipelines

### Containerization
- Docker
- Docker Hub

### Infrastructure
- Ubuntu Server
- Windows Server
- VirtualBox

### Orchestration
- Kubernetes
- Minikube
- Kubectl

### Web Services
- Nginx
- IIS

### Monitoring
- Prometheus
- Grafana
- Node Exporter

### Testing
- PyTest

---

## Features

✅ REST API for managing To-Do items

✅ Automated unit testing

✅ Docker image builds

✅ Continuous Integration with Azure Pipelines

✅ Pull Request validation

✅ Automated Linux deployment

✅ Nginx reverse proxy configuration

✅ Kubernetes deployment and scaling

✅ Windows IIS frontend deployment

✅ Prometheus metrics collection

✅ Grafana dashboards and alerting

✅ Troubleshooting documentation

---

## API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

### List Todos

```http
GET /todos
```

### Create Todo

```http
POST /todos
```

Request:

```json
{
  "title": "Learn DevOps"
}
```

---

## CI/CD Workflow

### Continuous Integration

1. Developer pushes code.
2. Pull Request validation starts.
3. Pipeline installs dependencies.
4. Unit tests run automatically.
5. Docker image is built.
6. Docker image is pushed to Docker Hub.

### Continuous Deployment

1. Deploy to Linux VM.
2. Restart Systemd service.
3. Verify health endpoint.
4. Update Kubernetes deployment.
5. Deploy frontend to IIS.

---

## Linux Deployment

The application runs as a Systemd service behind Nginx.

Components:

- Ubuntu Server
- Gunicorn
- Systemd
- Nginx

---

## Kubernetes Deployment

Docker images are deployed to Minikube.

### Kubernetes Resources

- Deployment
- Service
- Readiness Probe

### Operations

- Scale replicas
- Rolling updates
- Rollbacks
- Pod inspection
- Log analysis

---

## Monitoring & Observability

### Prometheus

Responsible for:

- Application Metrics
- Infrastructure Metrics
- Availability Monitoring

### Grafana

Provides dashboards for:

- CPU Usage
- Memory Usage
- Request Metrics
- Application Health

### Alerts

- High CPU Usage
- Service Down
- Target Unreachable

---

## Project Structure

```text
devops-project/
│
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── azure-pipelines.yml
│
├── deploy/
│   ├── deploy-linux.sh
│   ├── healthcheck.sh
│   └── deploy-iis.ps1
│
├── k8s/
│   └── deployment.yaml
│
├── monitoring/
│   ├── prometheus.yml
│   └── docker-compose.yml
│
├── frontend/
│   └── index.html
│
└── TROUBLESHOOTING.md
```

---

## Troubleshooting

Common scenarios covered:

- Failed PR validation
- Docker build failures
- Container startup issues
- ImagePullBackOff
- CrashLoopBackOff
- Nginx configuration problems
- Linux service failures
- IIS deployment issues
- Grafana alert investigations

---

## Lessons Learned

- Designing complete CI/CD workflows
- Automating deployments
- Managing Docker containers
- Working with Kubernetes
- Monitoring production environments
- Troubleshooting real-world DevOps issues

---

## Future Enhancements

- Azure Kubernetes Service (AKS)
- Terraform Infrastructure as Code
- Helm Charts
- Security Scanning
- Azure Key Vault Integration
- Blue-Green Deployments

---

## Author

Kalana Jayawardhana

DevOps Engineer | Cloud Enthusiast | Kubernetes | CI/CD | Automation

---

⭐ If you found this project useful, consider giving it a star.