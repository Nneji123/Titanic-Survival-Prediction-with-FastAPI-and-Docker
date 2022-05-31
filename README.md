# Titanic Survival Prediction with FastAPI and Docker
An API machine learning model used to predict if someone survived the Titanic crash. Built with FastAPI and Docker.

[![Language](https://img.shields.io/badge/language-python-blue.svg?style=flat)](https://www.python.org)
[![Framework](https://img.shields.io/badge/framework-FastAPI-brightgreen.svg?style=flat)](http://www.fastapi.org/news.html)
![hosted](https://img.shields.io/badge/Heroku-430098?style=flat&logo=heroku&logoColor=white)
![build](https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat)

## Problem Statement
The RMS Titanic, a luxury steamship, sank in the early hours of April 15, 1912, off the coast of Newfoundland in the North Atlantic after sideswiping an iceberg during its maiden voyage. Of the 2,240 passengers and crew on board, more than 1,500 lost their lives in the disaster.

So in this project I tried to develop an accurate model that could predict the chance of someone surviving the disaster

## Preview
![Screenshot 2022-05-31 090345](https://user-images.githubusercontent.com/101701760/171123842-ff6cd965-c849-44dd-8ca7-22bac6a007fa.png)


## Data
The data used was gotten from [kaggle](https://www.kaggle.com/datasets/heptapod/titanic)

## Algorithm Used
In this project I tested 6 different classification algorithms namely:
2. Decision Tree
3. Random Forest

The final model used for the app was the Random Classifier model which had the best accuracy.


## Requirements
To run a demo do the following:
1. Clone the repository.
2. Install the requirements from the requirements.txt file:
```
pip install -r requirements.txt
```
3. Then from your command line run:
```
python -m uvicorn --port 5000 --host 127.0.0.1 titanic_ml_api:app --reload 
```
Then you can view the site on your local server: http://127.0.0.1:5000/ 

## Building Docker image
To build the docker container image;
1. Install docker
1. Clone the repository
2. Then from your command line run:
```
docker build . -t [image-name]

```

## Deployment
The site can be deployed to heroku and can also be viewed here: 
