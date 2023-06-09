# -*- coding: utf-8 -*-
"""DMML_2022_Geneva_Functions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/Adrian-Muino/DMML2022_Geneva/blob/main/Code/DMML_2022_Geneva_Functions.ipynb
"""

import spacy
sp_sm = spacy.load('fr_core_news_sm')
def spacy_tokenizer_sm(df):
    # Create token object, which is used to create documents with linguistic annotations.
    mytokens = sp_sm(df)

    # Lemmatize each token and convert each token into lowercase
    mytokens = [ word.lemma_.lower().strip() for word in mytokens ]
  
    # Return preprocessed list of tokens
    return mytokens

import nltk
from nltk.tokenize import word_tokenize
# Define cleaning function
def nltk_tokenizer(doc):

    # Tokenize
    doc = word_tokenize(doc)

    # Remove uppercase and white spaces
    doc = [word.lower().strip() for word in doc]
    
    return doc

# Create tokenizer function
import spacy
sp = spacy.load('fr_core_news_sm')
def spacy_tokenizer_2(df):
    # Create token object, which is used to create documents with linguistic annotations.
    mytokens = sp(df)

    # Lemmatize each token and convert each token into lowercase
    mytokens = [ word.lemma_.lower().strip() for word in mytokens ]
    
    # Remove stop words and punctuation
    mytokens = [ word for word in mytokens]

    sentence=" ".join(mytokens)

    return sentence

from sklearn.metrics import recall_score, precision_score, f1_score, accuracy_score
def evaluate(y_true, pred):
  """
  This method calculates the model performance metrics. Since it is a multi-class
  classification, we decided to take the weighted average 
  for the metrics that are calculated for each class.

  """

  report = {
      'accuracy':accuracy_score(y_true, pred),
      'recall':recall_score(y_true, pred, average='macro'),
      'precision':precision_score(y_true, pred, average='macro'),
      'f1_score':f1_score(y_true, pred, average='macro')
  }

  return report

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
def plot_confusion_matrix(y_true, pred, model):
  
  """
  A method plotting the models into a confusion matrix.
  """

  cf_matrix = confusion_matrix(y_true, pred)

  disp = ConfusionMatrixDisplay(confusion_matrix=cf_matrix,
                              display_labels=model.classes_)
    
  disp.plot()


reports = {}

import tensorflow_hub as hub
import tensorflow_text as text

preprocessor = hub.KerasLayer("https://tfhub.dev/google/universal-sentence-encoder-cmlm/multilingual-preprocess/2")
encoder = hub.KerasLayer("https://tfhub.dev/google/universal-sentence-encoder-cmlm/multilingual-base/1")

def get_embeddings(sentences):
  '''return BERT-like embeddings of input text
  Args:
    - sentences: list of strings
  Output:
    - BERT-like embeddings: tf.Tensor of shape=(len(sentences), 768)
  '''
  preprocessed_text = preprocessor(sentences)
  return encoder(preprocessed_text)['pooled_output']


get_embeddings([
    "Les coûts kilométriques réels peuvent diverger sensiblement des valeurs moyennes en fonction du moyen de transport utilisé, du taux d'occupation ou du taux de remplissage, de l'infrastructure utilisée, de la topographie des lignes, du flux de trafic, etc."]
)

from keras import backend as K
def balanced_recall(y_true, y_pred):
    """This function calculates the balanced recall metric
    recall = TP / (TP + FN)
    """
    recall_by_class = 0
    # iterate over each predicted class to get class-specific metric
    for i in range(y_pred.shape[1]):
        y_pred_class = y_pred[:, i]
        y_true_class = y_true[:, i]
        true_positives = K.sum(K.round(K.clip(y_true_class * y_pred_class, 0, 1)))
        possible_positives = K.sum(K.round(K.clip(y_true_class, 0, 1)))
        recall = true_positives / (possible_positives + K.epsilon())
        recall_by_class = recall_by_class + recall
    return recall_by_class / y_pred.shape[1]

from keras import backend as K
def balanced_precision(y_true, y_pred):
    """This function calculates the balanced precision metric
    precision = TP / (TP + FP)
    """
    precision_by_class = 0
    # iterate over each predicted class to get class-specific metric
    for i in range(y_pred.shape[1]):
        y_pred_class = y_pred[:, i]
        y_true_class = y_true[:, i]
        true_positives = K.sum(K.round(K.clip(y_true_class * y_pred_class, 0, 1)))
        predicted_positives = K.sum(K.round(K.clip(y_pred_class, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        precision_by_class = precision_by_class + precision
    # return average balanced metric for each class
    return precision_by_class / y_pred.shape[1]

from keras import backend as K
def balanced_f1_score(y_true, y_pred):
    """This function calculates the F1 score metric"""
    precision = balanced_precision(y_true, y_pred)
    recall = balanced_recall(y_true, y_pred)
    return 2 * ((precision * recall) / (precision + recall + K.epsilon()))

import numpy as np
def predict_class(reviews,model):
  '''predict class of input text
  Args:
    - reviews (list of strings)
    - model to be used
  Output:
    - class (list of int)
  '''
  return [np.argmax(pred) for pred in model.predict(reviews)]
