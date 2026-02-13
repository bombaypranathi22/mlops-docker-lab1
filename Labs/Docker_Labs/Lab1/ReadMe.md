# Docker Lab 1 – Wine Classification (Random Forest)

## Overview

This lab demonstrates how to containerize a machine learning training pipeline using Docker.  
The application trains a Random Forest classifier on the Wine dataset from scikit-learn and evaluates its performance using accuracy and a classification report.

Compared to the baseline lab, I implemented the following changes:
- Tuned Random Forest hyperparameters for improved performance
- Added runtime logging (run date, accuracy, and classification report)
- Structured the project into a reproducible Docker-based workflow so the experiment can be run consistently across different machines

This ensures that the ML experiment is portable and reproducible using Docker.

---

## Project Structure

Lab1/
├── Dockerfile
├── ReadMe.md
└── src/
├── main.py
└── requirements.txt

- `Dockerfile` – Defines the Docker image and runtime environment  
- `src/main.py` – Trains and evaluates the Random Forest model  
- `src/requirements.txt` – Python dependencies  
- `ReadMe.md` – Instructions and documentation for this lab  

---

## Steps to Run the Lab

### 1. Clone the Repository

```bash
git clone https://github.com/bombaypranathi22/mlops-docker-lab1.git
cd mlops-docker-lab1/Labs/Docker_Labs/Lab1
2. Build the Docker Image
docker build -t lab1:v1 .
This command builds a Docker image called lab1:v1 using the provided Dockerfile.
3. Run the Container
docker run --rm lab1:v1
When the container runs successfully, you should see:
Training success message
Run date and time
Test accuracy
Classification report for the Wine dataset

Example Output
Training successful ✅
Run date: 2026-02-13 19:40:51
Test accuracy: 1.0000

precision    recall  f1-score   support
0       1.00      1.00      1.00        12
1       1.00      1.00      1.00        14
2       1.00      1.00      1.00        10

accuracy                           1.00        36
macro avg       1.00      1.00      1.00        36
weighted avg    1.00      1.00      1.00        36
