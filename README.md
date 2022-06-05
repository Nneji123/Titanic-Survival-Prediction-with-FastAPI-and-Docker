# Titanic Survival Prediction with FastAPI and Docker
[![Language](https://img.shields.io/badge/language-Python-blue.svg?style=flat)](https://www.python.org)
[![Framework](https://img.shields.io/badge/Keras-darkred.svg?style=flat&logo=keras&logoColor=white)](http://www.pytorch.org/news.html)
[![Framework](https://img.shields.io/badge/FastAPI-darkgreen.svg?style=flat&logo=fastapi&logoColor=white)](http://www.fastapi.org/news.html)
![hosted](https://img.shields.io/badge/Heroku-430098?style=flat&logo=heroku&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-blue?style=flat&logo=docker&logoColor=white)
![build](https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat)

A Machine Learning model deployed as an API and used to predict if someone survived the Titanic crash. Built with TensorFlow(Keras), FastAPI and Docker.

## Problem Statement
The RMS Titanic, a luxury steamship, sank in the early hours of April 15, 1912, off the coast of Newfoundland in the North Atlantic after sideswiping an iceberg during its maiden voyage. Of the 2,240 passengers and crew on board, more than 1,500 lost their lives in the disaster.

So in this project I tried to develop an accurate model that could predict the chance of someone surviving the disaster

## Preview
![Screenshot 2022-05-31 090345](https://user-images.githubusercontent.com/101701760/171123842-ff6cd965-c849-44dd-8ca7-22bac6a007fa.png)


## Data
The data used was gotten from [kaggle](https://www.kaggle.com/datasets/heptapod/titanic)

## Algorithm Used
In this project I tested 6 different classification algorithms namely:
1. Decision Tree
2. Random Forest

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
2. Clone the repository
3. Then from your command line run:
```
docker build . -t titanicapi

```
4. Run the docker container:
```
docker run -d --name mycontainer -p 5000:5000 titanicapi

```

Then you can view the site on your local server: http://127.0.0.1:5000/


## Deployment
The api can be deployed using the dockerfile or the procfile on heroku.

### Deployment with Dockerfile
Assuming you have git and heroku cli installed just carry out the following steps:

1. Clone the repository

```
git clone https://github.com/Nneji123/Titanic-Survival-Prediction-with-FastAPI-and-Docker.git
```

2. Change the working directory

```
cd Titanic-Survival-Prediction-with-FastAPI-and-Docker 
```

4. Create the heroku app

``` 
heroku create your-app-name 
```

Replace **your-app-name** with the name of your choosing.

4. Set the heroku cli git remote to that app

```
heroku git:remote your-app-name
```

5. Set the heroku stack setting to container
 
```
heroku stack:set container
```

6. Push to heroku
```
git push heroku main
```

### Deployment with Github
1. Clone the repository and copy the contents to your own repository on github
2. Deploy with Github and Heroku then you're done.


## Live Link
The api and its documentation can be viewed here: https://titanic-prediction-new.herokuapp.com/docs or https://titanic-prediction-new.herokuapp.com/redoc
