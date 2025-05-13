# Dockerized CI/CD Deployment with GitHub Actions to AWS EC2

This project demonstrates a full DevOps CI/CD pipeline using **GitHub Actions**, **Docker**, **Docker Hub**, and **AWS EC2**. It consists of two separate workflows:

- Workflow 1 – CI:** Build Docker image and push to Docker Hub
- Workflow 2 – CD:** SSH into AWS EC2, pull the latest image, and restart the container

---

## Tech Stack

- Docker** for containerization
- GitHub Actions** for CI/CD automation
- Docker Hub** as container registry
- AWS EC2** for cloud deployment

---

## Project Structure

├── app   # source code
├── Dockerfile
├── .github/
│ └── workflows/
│ ├── ci.yml # CI: Build and push Docker image to Docker Hub
│ └── cd.yml # CD: SSH into EC2, pull and deploy container
└── README.md


---

## CI Workflow – Build & Push Docker Image (`ci.yml`)

**Trigger:** On push to `main` branch  
**Steps:**
- Checkout code
- Login to Docker Hub using secrets
- Build Docker image and tag with latest commit hash or `latest`
- Push image to Docker Hub

---

## CD Workflow – Deploy to AWS EC2 ('cd.yml')

**Trigger:** On successful Docker push (or manual/cron trigger)  
**Steps:**
- Connect to AWS EC2 via SSH (using GitHub secret)
- Pull latest image from Docker Hub
- Stop and remove existing container
- Start a new container using the latest image

---

## Required GitHub Secrets

| Secret Name         | Purpose                            |
|---------------------|------------------------------------|
| `DOCKER_USERNAME`   | Docker Hub username                |
| `DOCKER_PASSWORD`   | Docker Hub password or access token|
| `EC2_HOST`          | Public IP or DNS of EC2 instance   |
| `EC2_USER`          | EC2 username (e.g., `ubuntu`)      |
| `EC2_SSH_KEY`       | Private SSH key (base64-encoded)   |

---

## Deployment Commands on EC2 (handled in CD workflow)

# Stop and remove existing container
docker stop flask-app || true
docker rm flask-app || true
          
# pull docker image from dockerhub
docker pull techpoint247/flask-to-do-app

# Run new container
docker run -d -p 8000:8000 --name flask-app techpoint247/flask-to-do-app


