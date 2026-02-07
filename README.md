# 🚀 DevOps Microservices Platform  
**End-to-End DevOps | Kubernetes | CI/CD | Blue-Green | Observability | Resilience**
---
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue?logo=docker)
![Docker Compose](https://img.shields.io/badge/Docker%20Compose-Multi--Container-lightblue?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-blue?logo=kubernetes)
![Helm](https://img.shields.io/badge/Helm-Package%20Manager-0F1689?logo=helm)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?logo=githubactions)
![Blue-Green Deployment](https://img.shields.io/badge/Deployment-Blue--Green-brightgreen)
![Canary Deployment](https://img.shields.io/badge/Deployment-Canary-yellow)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-E6522C?logo=prometheus)
![Grafana](https://img.shields.io/badge/Grafana-Visualization-F46800?logo=grafana)
![k6](https://img.shields.io/badge/k6-Load%20Testing-7D64FF?logo=k6)

## 📌 Project Overview

This project demonstrates a **real-world DevOps implementation** for a microservices-based backend platform, focusing on **production readiness**, not just deployment.

The project covers:
- Zero-downtime deployments
- Safe rollbacks
- Kubernetes orchestration
- CI/CD automation
- Observability and metrics
- Load testing and resilience
- Autoscaling behavior and analysis

> It mirrors how DevOps is actually practiced in real engineering teams.

---

## 🧱 Architecture Overview

## Arc Diagram
![Architecture Diagram](assets/blue-green-deployment.png)



**Microservices**
- Auth Service  
- Orders Service  
- Payments Service  
- Notifications Service  

**High-Level Flow**
## Client
→ Kubernetes Service
→ Pod (Blue / Green Deployment)

Each service is:
- Independently containerized
- Deployed via CI/CD
- Managed by Kubernetes
- Observable through metrics

---

## 🛠 Technology Stack

- **Backend:** FastAPI (Python)  
- **Containerization:** Docker  
- **Orchestration:** Kubernetes (AKS)  
- **CI/CD:** GitHub Actions  
- **Deployment Strategy:** Blue-Green  
- **Monitoring:** Prometheus, Grafana  
- **Load Testing:** k6  
- **Autoscaling:** Kubernetes HPA  

---

## 🔵 Phase 0 — Environment & Foundations

**Goal:** Never struggle with setup again

**What was done**
- Linux CLI workflow
- Git branching and commits
- Python virtual environments
- Docker fundamentals

**Outcome**
- Clean, reproducible development environment
---

## 🔵 Phase 1 — Backend Microservices

**Goal:** Understand service behavior and boundaries

**What was done**
- Multiple FastAPI services
- Independent APIs
- Async request handling
- Clear service separation

**Outcome**
- All services respond correctly
- APIs are independently deployable

## Screenshots

![Swagger UI Diagram](assets/13.png)

![API UI Response](assets/14.png)


---

## 🔵 Phase 2 — Dockerization

**Goal:** Application runs identically everywhere

**What was done**
- Dockerfile per service
- Environment-based configuration
- Docker Compose for local orchestration

**Outcome**
- Full system starts with a single command
- Zero manual setup steps
---

## 🔵 Phase 3 — Kubernetes Core

**Goal:** Production-grade orchestration

**What was done**
- Kubernetes Deployments and Services
- Namespace isolation
- ConfigMaps and Secrets
- Declarative infrastructure

**Outcome**
- All services run inside Kubernetes
- Fully declarative cluster setup

## Screenshots

![kubectl get pods](assets/7.png)
![kubectl deployments](assets/3.png)
![kubectl get deployments](assets/10.png)

---

## 🔵 Phase 4 — CI/CD & Blue-Green Deployment

**Goal:** Zero-downtime deployments

**What was done**
- GitHub Actions CI/CD pipelines
- Image build and push on commit
- Automated Kubernetes deployments
- Blue-Green deployments for all services
- Instant rollback via service selector switch

**Why Blue-Green**
- No downtime
- Safe releases
- Fast rollback during incidents

**Outcome**
- One-click deployments
- Rollback in seconds

## Screenshots

### GitHub Actions pipeline runs
![GitHub Actions pipeline runs](assets/9.png)

### Blue–Green Deployment Traffic Switch
![Blue–Green Deployment Traffic Switch](assets/8.png)


---

## 🔵 Phase 5 — Observability

**Goal:** See failures before users do

**What was done**
- Prometheus metrics collection
- Grafana dashboards
- Metrics validation under load

**Outcome**
- CPU, memory, and pod metrics visible
- System behavior measurable

## Screenshots
### Grafana dashboards
![Grafana dashboards](assets/5.png)

![Grafana dashboards](assets/1.png)

### Prometheus metrics
![Prometheus metrics](assets/6.png)


▶️ **Grafana dashboards Explained**  
[Watch the video](assets/github.mp4)

---

## 🔵 Phase 6 — Backup & Disaster Recovery (Design)

**Goal:** Disaster recovery strategy

**What was evaluated**
- Velero for Kubernetes backups
- Object-storage-based restore model

**Design Decision**
- Platform is stateless
- No databases or persistent volumes
- Full DR execution intentionally deferred

**Why**
- Stateless workloads rely on redeploy, not restore
- Design clarity is more important than forced demos

**Outcome**
- DR approach clearly understood and documented
- Clear upgrade path for future stateful workloads

---

## 🔵 Phase 7 — Load, Failure & Resilience

### Load Testing
- k6 used to generate concurrent traffic
- Latency and error rates measured
- System remained stable under load

## Screenshots
![k6 load testing results](assets/4.png)

---

### Autoscaling (HPA)
- CPU-based Horizontal Pod Autoscaler configured
- Metrics validated
- Correct non-scaling behavior explained
  (service was not CPU-bound)

**Key Insight**
> Autoscaling should happen only when resource pressure exists.
> 
---

### Pod Failure Simulation
- Live pods deleted manually
- Kubernetes self-healing observed
- No service disruption

---

## 🎯 Key Learnings

- Zero-downtime is about process, not just tools
- Observability is mandatory in production
- Autoscaling must be driven by metrics, not assumptions
- Knowing **when not to scale** is critical
- DevOps is decision-making, not tool collection

---
## 🏁 Final Status

✅ Project Complete  
🚀 Production-oriented DevOps platform  

**Author:** Adharsh U  

## 📄 Research Paper

This research paper was prepared as part of the design and evaluation of this DevOps platform.

**Title:** Blue–Green and Canary Deployments in Cloud-Native DevOps  
**Format:** PDF  
[View Research Paper](research/blue-green-canary-devops.pdf)

