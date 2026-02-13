# Docker Lab 1 – Wine Classification (Random Forest)

## Overview
This lab demonstrates how to containerize a machine learning pipeline using Docker.  
The model trains a Random Forest classifier on the Wine dataset from scikit-learn and evaluates its accuracy.

I modified the baseline implementation by tuning model hyperparameters and structuring the code into a reproducible Docker workflow.

---

## Project Structure

Lab1/
│── Dockerfile  
│── ReadMe.md  
│── src/  
│   ├── main.py  
│   ├── requirements.txt  

---

## Steps to Run the Lab

### 1. Clone the Repository
```bash
git clone https://github.com/bombaypranathi22/mlops-docker-lab1.git
cd mlops-docker-lab1/Labs/Docker_Labs/Lab1

