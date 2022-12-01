# Language-Detector
McGill AI Society Machine Learning Bootcamp final project Winter 2022. 

Training data obtained from WiLi-2018. 

# Project description 

This language classifier project is a web app that classifies the language of an input text. The scope of the project is ten of the most common languages in the world. We implemented a Multinomial Naive Bayes model from sklearn which took in a vectorized string using a vectorizor function we developed, as well as a bag of words containing 250 of the most common words per language. We developed the web's frontend using Flask. 

# Running the app 


# Repository organization 

Our repository consists of the data used to train the model, the script containing the model itself, and the script to build the web app. It additionally contains the deliverables required by the MAIS organizers. 

1. scripts/ 
- model.py
 -- implementation of the model, consisting of the vectorizor function, the development of the bag of words, and the measure of accuracy via confusion matrix.
 - app.py 
 -- implementation of the web app through Flask 

2. WiLi-2018/
- this folder contains all of the language data, split into training and test splits. The data is originally sourced from Wikipedia. 

3. deliverables/
- this folder contains the deliverables required by the MAIS organizers. 
