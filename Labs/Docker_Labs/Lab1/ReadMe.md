
---

## My Implementation (Lab 1)

This Docker lab trains and evaluates a RandomForest model on the Wine dataset using scikit-learn.

### How to Run

From the Lab1 directory:

```bash
docker build -t lab1:v1 .
docker run --rm lab1:v1



docker build -t lab1:v1 .

docker save lab1:v1 > my_image.tar

docker run lab1:v1
