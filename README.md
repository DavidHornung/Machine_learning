
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
  
In the first colab "Models ask by the faculty" we do no data cleaning and keep the sentence has they are. We tokenize our word and train the following models:
<p align="center">
Linear Regression </br>
<p>
Linear regression is a statistical method used to model the linear relationship between a dependent variable and one or more independent variables. In a linear regression model, the goal is to find the line of best fit that describes the relationship between the variables as accurately as possible.

The line of best fit is a line that is as close as possible to all the data points in a scatter plot of the variables. The line is defined by a mathematical equation of the form y = mx + b, where y is the dependent variable, x is the independent variable, m is the slope of the line, and b is the intercept (the point where the line crosses the y-axis).

To find the line of best fit, linear regression uses a method called least squares, which finds the line that minimizes the sum of the squared differences between the observed data points and the line. Once the line of best fit has been found, it can be used to make predictions about the dependent variable given new values of the independent variable(s).

Linear regression is a widely used statistical method that is simple to understand and implement, and it is often used as a baseline model for more complex regression methods. It is most appropriate when the relationship between the dependent and independent variables is approximately linear.
<p align="center">
K-nearest neighbors algorithm </br>
<p>
The K-nearest neighbors (KNN) algorithm is a non-parametric method used for classification and regression. In both cases, the goal is to predict the value of a target variable for a given data point by looking at the values of the target variable for the K nearest data points.

For classification, the target variable is a categorical variable with a fixed set of possible values, and the KNN algorithm assigns the data point to the most common category among its K nearest neighbors. For regression, the target variable is a continuous variable, and the KNN algorithm predicts the value of the target variable for the data point as the average of the values of the K nearest neighbors.

The KNN algorithm has a number of important hyperparameters:

K: The number of nearest neighbors to consider. A larger value of K will result in a smoother decision boundary, while a smaller value will result in a more complex boundary.

Distance metric: The method used to measure the distance between data points. Common options include Euclidean distance and Manhattan distance.

Weighting function: The method used to weight the contribution of each nearest neighbor to the prediction. A common option is to use a uniform weighting, which gives equal weight to all neighbors, but other options include weighting by distance or using a kernel function.

To use the KNN algorithm, you need to choose values for these hyperparameters and then find the K nearest neighbors for each data point using the chosen distance metric. You can then use the values of the target variable for the K nearest neighbors to make a prediction for the data point.
<p align="center">
Decision tree </br>
<p>
  A decision tree is a tree-like model used for classification and regression tasks. It is a type of supervised learning algorithm that is based on the idea of dividing the input space into regions based on the value of certain features, with the goal of achieving high accuracy in classifying or predicting the target variable.

In a decision tree, each internal node represents a decision based on the value of a feature, and each leaf node represents a prediction. The decision tree is constructed by training on a dataset and using an algorithm to find the feature and decision threshold that results in the highest accuracy.

For example, in a decision tree for classifying animals, an internal node might ask whether an animal has feathers, and the branches from that node would be "Yes" and "No." If the animal has feathers, the decision tree might ask whether the animal can fly, and the branches from that node would be "Yes" and "No." This process continues until the decision tree reaches a leaf node, at which point it makes a prediction about the class of the animal.

Decision trees are popular because they are easy to understand and interpret, and they can handle both categorical and continuous data. However, they can also be prone to overfitting, especially if they are allowed to grow too deep. To mitigate this risk, decision trees can be pruned to remove branches that do not contribute significantly to the accuracy of the model.
<p align="center">
Random Forest </br>
<p>
  Random forest is an ensemble learning method for classification and regression tasks. It is a type of supervised learning algorithm that uses multiple decision trees and combines their predictions to make a final prediction.

In a random forest model, each decision tree is trained on a random subset of the data, and a random subset of the features is used to make predictions at each node in the tree. This process is repeated many times, and the final prediction is made by averaging the predictions of all the decision trees in the forest.

Random forest models are popular because they tend to be more accurate than individual decision trees and are resistant to overfitting. They are also relatively easy to train and tune, and they can handle a large number of features and can work with both categorical and continuous data.

To use a random forest model, you need to choose the number of decision trees to include in the forest and set any other relevant hyperparameters, such as the maximum depth of the trees or the number of features to consider at each node. You can then train the model on your training data and use it to make predictions on new data.
  </br>
  </br>
We also used gridsearch and cross validation plot in the decision tree in order to find the best parameters with the highest accuracy.
<p align="center">
Gridsearch </br>
<p>
  Grid search is a method used to tune the hyperparameters of a machine learning model. It involves training the model with a range of different hyperparameter values and evaluating the performance of each set of hyperparameters using a validation set. The goal is to find the combination of hyperparameters that results in the best performance on the validation set.

In the case of the K-nearest neighbors (KNN) algorithm, some common hyperparameters that might be tuned using grid search include:

K: The number of nearest neighbors to consider when making a prediction.
Distance metric: The method used to measure the distance between data points.
Weighting function: The method used to weight the contribution of each nearest neighbor to the prediction.
To perform a grid search for KNN, you would define a range of values for each hyperparameter and then evaluate the performance of the model for every combination of hyperparameter values. For example, you might try values of K from 1 to 10 and evaluate the performance of the model for each value. You would then choose the combination of hyperparameters that resulted in the best performance on the validation set.

Grid search can be computationally expensive, as it involves training the model multiple times with different hyperparameter values. However, it is a widely used method for finding the optimal hyperparameters for a machine learning model.
  
  <p align="center">
Cross validation </br>
<p>

  Cross-validation is a method used to evaluate the performance of a machine learning model by training and evaluating the model multiple times on different subsets of the data. It is a way to validate the model's performance and avoid overfitting, which is when the model performs well on the training data but poorly on new, unseen data.

Cross-validation involves dividing the data into a number of folds, and then training and evaluating the model on each fold. There are several different types of cross-validation, but one of the most common is K-fold cross-validation, where the data is divided into K folds and the model is trained and evaluated K times, each time using a different fold as the validation set and the remaining folds as the training set. The final performance of the model is then calculated as the average performance across all K folds.

Cross-validation can be used with any type of machine learning model, including decision trees. To perform cross-validation for a decision tree, you would divide the data into K folds, train the decision tree on K-1 folds, and evaluate it on the remaining fold. You would then repeat this process K times, each time using a different fold as the validation set. The final performance of the decision tree would be calculated as the average performance across all K folds.

Cross-validation is a valuable tool for evaluating the performance of a machine learning model and ensuring that it is robust and generalizable to new data. It is especially important when the amount of available data is limited, as it allows you to make the most of the data you have by training and evaluating the model multiple times.

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


