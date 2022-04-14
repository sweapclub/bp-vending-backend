# Vending Machine Back-end

This is a project for Technical Challenge.

## Description

This project base on Python with fastapi

## Getting Started

### Dependencies

* fastapi
* pydantic
* SQLAlchemy

### Installing & Run

```
git clone https://github.com/sweapclub/bp-vending-frontend
pip install -r requirements.txt
uvicorn src.main:app --reload
```

## Deploy with docker

```
docker build -t vending-machine-back:v1.0 .
docker run -d -p 3000:80 --name vd-back-end vending-machine-back:v1.0 
```
Don't forget to check port with front-end...

## Authors

Nuttasak Munhadee

Email : m.nuttasuk@gmail.com

Linkedin :  [Nuttasak Munhadee](https://www.linkedin.com/in/nuttasuk-munhadee/)