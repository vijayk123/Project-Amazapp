# Amazapp – End-to-End DevOps Project

This repository contains an end-to-end DevOps implementation of a simple Python-based e-commerce backend application.

The intention of this project was **not** to just make the application run, but to understand how things work in real production environments — what breaks, why it breaks, and how to fix it.

I followed a hands-on approach, faced real issues, and documented everything properly instead of hiding the problems.

---

## Why I Built This Project

I wanted to understand:
- How applications move from code to production
- How CI/CD actually works in practice
- How Kubernetes replaces traditional EC2 + systemd setups
- Why monitoring is important even when the app is running
- How IAM and permissions affect real cloud work

This project is a result of that learning.

---

## What This Project Covers

- Python Flask backend application
- Dockerizing the application
- CI using GitHub Actions
- Storing Docker images in AWS ECR
- Deploying the app on Kubernetes (EKS)
- Exposing the application using Service and Ingress
- Horizontal Pod Autoscaling (HPA)
- Monitoring using Prometheus and Grafana
- Debugging real-world issues (IAM, Ingress, HPA)
- Cleaning up AWS resources after usage

---

## High-Level Architecture
 
Developer
   |
GitHub
   |
GitHub Actions(CI)
   |
Docker Image
   |
AWS ECR
   |
Amazon EKS
   |
Kubernetes Deployement --> Service --> Ingress
   |
Prometheus(Metrics) --> Grafana(Dashboards)

## Tech Stack Used:

- Python (Flask)
- Git & GitHub
- GitHub Actions
- Docker
- Kubernetes
- Amazon EKS
- AWS ECR
- NGINX Ingress Controller
- Prometheus
- Grafana

---

## Repository Structure

amazapp-devops-project/
│
├── app/                  # Application code and Dockerfile
├── ci-cd/                # GitHub Actions pipeline
├── kubernetes/           # Deployment, Service, Ingress, HPA
├── monitoring/           # Prometheus & Grafana notes
├── troubleshooting/      # Issues I faced and how I fixed them
├── aws/                  # IAM, ECR, EKS notes
└── cleanup/              # Resource deletion steps



## Key Takeaways

Kubernetes solves operational problems, not application logic

Autoscaling depends on metrics, not configuration alone

Ingress always requires a Service

IAM errors usually mean permissions are correctly restricted

Monitoring is required even when everything looks fine