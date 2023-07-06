# Hyperparameter tuning of ANN using Metahueristic Algorithms for Heart Disease Prediction

## Team Members
1. Gummuluri Venkata Ravi Ram
2. Mogilipalem Hemanth Kumar
3. Jayanth Prathipati

## Description
  This project focuses on developing a heart disease prediction application by leveraging metaheuristic algorithms for hyperparameter tuning of Artificial Neural Networks (ANN). The study compares the performance, time complexity, and space complexity of three metaheuristic algorithms, namely Genetic Algorithm (GA), Ant Colony Algorithm (ACA), and Particle Swarm Optimisation (PSO) , to identify the algorithm that produces the highest accuracy model. By implementing these algorithms, we aim to create an application that accurately predicts heart disease risk based on relevant patient data.
  This will be containing seperate implementations of GA, MMAS-ACO and PSO for hyperparameter tuning.

## Contents
0. heart.csv (dataset)
1. geneticALgo.ipynb
2. antColony.ipynb
3. particleSwarm.ipynb
4. folder webapp consisting of dependencies to run web app
5. folder app consisting of flask-API to test backend

## Requirements
* Numpy
* Pandas
* Tensorflow
* Seaborn
* Keras
* Flask

## Steps of Exection
* Download all notebooks as well as dataset (heart.csv) to the same folder.
* _GeneticAlgo.ipynb_ initially contains conventional tuning algos.
* _GeneticAlgo.ipynb_ , _antColony.ipynb_, _particleSwarm.ipynb_ has cellwise code to run in a Python 3.0 environment where the training cells may take as long as 30 minutes.
* API consists of app.py which is the Flask API that can be run in python 3.0 environment which gives the URL for local server. Postman can be used for testing purpose.
* Web App To launch the web application, run the following command:
streamlit run app.py his command will start the development server and display the local URL where the app can be accessed (usually http://localhost:8501).

