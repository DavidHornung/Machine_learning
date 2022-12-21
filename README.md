
![unil_geneva-low-resolution-logo-white-on-transparent-background](https://user-images.githubusercontent.com/114933900/208516105-a174866e-93da-4a11-8a47-00200f17ce38.png)




![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Logo_Universit%C3%A9_de_Lausanne.svg/300px-Logo_Universit%C3%A9_de_Lausanne.svg.png)
  # DMML2022_Geneva
By Adrian Muino & David Hornung aka Gimli-coding



Brief description of the project : 


The project was to find the best machine learning model in order to classify french text in order of difficulty (A1,A2,B1,B2,C1,C2)

# Table of Contents

1. [Models ask by the faculty]().

2. [Models using tokenization]().

 3. [Linear regression using embeding](https://colab.research.google.com/github/Adrian-Muino/DMML2022_Geneva/blob/main/Colab_Notebooks/DMML-2022_Geneva_Embeding_Model.ipynb#scrollTo=AHaES7NAqweE).

 4. [Linear regression using pretrained models Heu Adrian tu trouveras un bon titre à ton model ;)]()


# Methodology

We decided to separate our work in 4 different colab from the simpliest model to the most complicated one.

</br>
<p align="center">
<img width="400" src="https://fontmeme.com/permalink/221219/6aa05142fb36f2c8e1508addfbe36dc0.png">
<p>
</br>
  
In the first colab "Models ask by the faculty" we do no data cleaning and keep the sentence has they are. We use spacy in order to tokenize our word and train the following models:

Linear Regression </br>
K-nearest neighbors algorithm </br>
Decision tree </br>
Random Forest </br>

We also used gridsearch and cross validation plot in the decision tree in order to find the best parameters with the highest accuracy.

</br>
<p align="center">
<img width="400" src="https://fontmeme.com/permalink/221219/f4054e7e06c7a18ca481271166811921.png">
<p>
</br>
<p align="center">
SPACY
<p>
spaCy is a popular natural language processing (NLP) library that includes a tokenizer for dividing a piece of text into individual tokens (commonly referred to as words, although in NLP the term "token" is more general and can refer to any part of a piece of text).

The spaCy tokenizer works by first dividing the text into sentences, using a combination of rules and machine learning models trained on a large dataset. It then divides each sentence into tokens, again using a combination of rules and machine learning models.

One of the key features of the spaCy tokenizer is its ability to handle a wide range of languages and writing systems, including languages with complex grammar and vocabulary, such as German and French, and languages with non-Latin scripts, such as Arabic and Chinese. The tokenizer is also able to handle a variety of text types, including social media posts, news articles, and academic papers.

Once the text has been tokenized, spaCy performs a number of additional NLP tasks, including part-of-speech tagging, named entity recognition, and dependency parsing. These tasks are used to extract structured information from the text and make it easier to analyze and manipulate.
<p align="center">
Natural Language Toolkit
<p>
The Natural Language Toolkit (NLTK) is a suite of libraries and resources for natural language processing (NLP) in the Python programming language. It provides tools for tasks such as tokenization (dividing text into individual words and punctuation), part-of-speech tagging (identifying the part of speech of each word), and named entity recognition (identifying named entities like person names, organizations, and locations).

NLTK also includes a number of resources and datasets for working with text, including a large collection of sample texts, word lists, and corpora (large collections of text). It also includes tools for working with other languages and writing systems, such as stemmers for reducing words to their base form and tools for working with machine translation.

To use NLTK, you first need to install the library and then import the relevant modules in your Python code. You can then use the functions and classes provided by NLTK to process text and perform various NLP tasks. For example, you can use the word_tokenize function to tokenize a piece of text into individual words, or the pos_tag function to tag the part of speech of each word.




</br>
<p align="center">
<img width="400" src="https://fontmeme.com/permalink/221219/99485c5ec53a29415b16a94c2100bc5c.png">
<p>
</br>
</br>
<p align="center">
<img width="400" src="https://user-images.githubusercontent.com/114933900/208532349-5a3facf6-3931-45d1-8df0-23612263a568.jpg">
<p>
  
  Word embeddings are a way to represent words as numerical vectors. The idea behind word embeddings is to capture the meaning of a word in a continuous, low-dimensional space, such that semantically similar words are close to each other in that space.

There are different ways to create word embeddings, but a common approach is to use a neural network to learn the embeddings from large amounts of text data. The neural network takes as input a one-hot encoded representation of a word, where each word in the vocabulary is represented by a unique vector with all zeros except for a 1 in the index corresponding to that word. The network then learns to map this one-hot encoded vector to a continuous, low-dimensional space through an embedding layer.

Once the network has learned the embeddings, they can be used as input to other machine learning models, such as natural language processing (NLP) tasks like text classification or language translation. The advantage of using word embeddings is that they capture the meaning of words in a way that is more meaningful for machine learning models than a one-hot encoded representation, which treats each word as an independent entity with no relationship to other words.

 </br>
</br>
<p align="center">
<img width="400" src="https://fontmeme.com/permalink/221219/89919f5ad9759f663241eca5f028525c.png">
<p>
</br>

## Summary of the results table : (TO BE COMPLETED)


## Link to the explainatory video : (TO BE COMPLETED)


