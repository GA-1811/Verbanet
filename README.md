# Verbanet
This is a project mainly works on the principle of NLP under which it focusses on Text Classification. It can perform Multiple task including Text summarization, Sentiment Analysis and it can understand the text and can perform Spelling and Grammar checking on it. 

We used many concepts of NLP into it to make it totally workable. We first created the Models(Model, Model2, Model3). These Models contained the code that is the backbone of the whole project. 

We used the backend language Flask, to complete this project. Flask is actually a very easy to use language and  is much more development friendly language and thus was the first prefrence while creating the project. 

Model, 
This file contained the code related to Spelling and Grammar Correction where we user the libraries:-
textblob
Pyaspeller
These libraries helped us to create the code in very less amount of time. 

Model2, 
This file contained the code related to sentiment analysis. This was done with the help of library textblob. This library has its built in function known to be as Polarity. This function helped us to create the project for sentiment analysis by giving us the value range between 0 to 1. 

Model3, 
This file contained the code related to text summarzation. We used the library known to be Spacy. This library helped us to remove the stopwords, Puntuation tags, HTML tags and some of the Emoji, which could create the problem while reducing the length of it.
