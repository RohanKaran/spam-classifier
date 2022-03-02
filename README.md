![FastAPI](https://img.shields.io/badge/Backend-FastAPI-green)
![ReactJS](https://img.shields.io/badge/Frontend-ReactJS-blue)
![API](https://img.shields.io/badge/API-TensorFlow-orange)
![API](https://img.shields.io/badge/Model-Keras-darkgreen)

# Spam Classifier

## Demo
<hr/>

View the live app [here](https://spamham.netlify.app)

## About
<hr/>

#### Datasets: 
[Dataset 1](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection) and [Dataset 2](https://archive.ics.uci.edu/ml/datasets/YouTube+Spam+Collection) are collected from [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php).

#### Model:
- A specific architecture of a neural network is created, still a "blank slate" in terms of what it "knows". Its core structure is that of a LSTM (long-short-term-memory), a specific kind of recurrent neural network with some clever modifications aimed at enhancing its ability to "remember" things between non-adjacent locations in a sequence, such as two displaced positions in a string of text;
- The network is trained: that means it will progressively adapt its internal (many thousands of) parameters in order to best reproduce the input training set. Each individual neuron in the network is a relatively simple component - the "intelligence" coming from their sheer quantity and the particular choice of parameters determining which neurons affect which other and by how much;
- Once the training process has finished, the script carefully saves everything (model, tokenizer and associated metadata) in a format that can be later loaded by the backend in a stand-alone way.

#### Web Application Details:
- [Backend](https://github.com/RohanKaran/spam-classifier): FastAPI 
- [Frontend](https://github.com/RohanKaran/spam-cls-frontend): ReactJS
