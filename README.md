|  <img width="600" height="400" src="https://user-images.githubusercontent.com/101266297/209135507-21954fa6-4a09-4331-ad82-4f2f50c8ec88.png">      | <img width="400" height="200" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Logo_Universit%C3%A9_de_Lausanne.svg/300px-Logo_Universit%C3%A9_de_Lausanne.svg.png"> |
| ----------- | ----------- |

# DMML2022_Geneva, Adrian Muino & David Hornung (Gimli-coding)

The project was to find the best machine learning model in order to classify french text in order of difficulty (A1,A2,B1,B2,C1,C2). This project is made for our master class in Data Mining and Machine Learning class at the Université de Lausanne HEC faculty. Results of predictions made by our models where submitted in a competition in kaggle
[Detecting the difficulty level of French texts (click to redirect)](https://www.kaggle.com/competitions/detecting-french-texts-difficulty-level-2022).

The utility of such project is to help identify the difficulty level of French sentences in order to improve someone’s skills. As it is important to read texts when you trying to learn a new language, these texts have to be at the reader’s language level. However, it is difficult to find texts that are close to someone’s knowledge level (A1 to C2).

For this reason, we have been asked to build a model for English speakers that predicts the difficulty of a French written text. This can be then used, e.g., in a recommendation system, to recommend texts, e.g, recent news articles that are appropriate for someone’s language level. If someone is at A1 French level, it is inappropriate to present a text at B2 level, as he or she won’t be able to understand it. Ideally, a text should have many known words and may have a few words that are unknown so that the person can improve.

# Results
Our journey in this competition, ended up with various models stored in this GitHub in 4 different colabs classified from the simpliest model to the most complicated one.

The accuracy improvements in our models are illustrated here under :

<img width="1000" src="https://user-images.githubusercontent.com/114933900/208974347-0e640dd3-8c55-4e01-9b8b-67a3b3737591.png">


## [1. Mandatory models (click to redirect)](https://github.com/Adrian-Muino/DMML2022_Geneva/blob/main/Code/1.DMML_2022_Geneva_Mandatory_Models.ipynb)
In this first colab we were not allowed to clean the data and had to keep the sentence has they were. We also were asked to implement 4 classification models (Logistic Regression, Random Forest, K-Nearest Neighbors and Decision Tree). Here are our results :

<img width="800" src="https://user-images.githubusercontent.com/101266297/209134864-7231e754-2b73-4832-9b92-86694b135633.png">


## [2. Improved Models (click to redirect)](https://github.com/Adrian-Muino/DMML2022_Geneva/blob/main/Code/2.DMML_2022_Geneva_Improved_Models.ipynb)

|index|Ridge Classifier NLTK|Logistic Regression NLTK|SGD Classifier NLTK|Logistic Regression Spacy|Ridge Classifier Spacy|SGD Classifier Spacy|Perceptron Classifier NLTK|Random Forest NLTK|Gradient Boosting Classifier Spacy|Gradient Boosting Classifier NLTK|Random Forest Spacy|Perceptron Classifier Spacy|XGB Classifier Spacy|XGB Classifier NLTK|KNN NLTK|KNN Spacy|Decision Tree Spacy|Decision Tree NLTK|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Accuracy|0\.48854166666666665|0\.4864583333333333|0\.48333333333333334|0\.47708333333333336|0\.46458333333333335|0\.46145833333333336|0\.44583333333333336|0\.4322916666666667|0\.43020833333333336|0\.41875|0\.41770833333333335|0\.41041666666666665|0\.40729166666666666|0\.39166666666666666|0\.3572916666666667|0\.33958333333333335|0\.325|0\.296875|
|Recall|0\.4896766905572185|0\.48852107075520407|0\.48386468743737976|0\.4776555731965663|0\.4647618612515534|0\.4622889351326636|0\.44498705396339355|0\.4351173994605668|0\.4309994131908083|0\.42071245998685197|0\.4172968419288397|0\.41035209950055634|0\.40737400249510963|0\.3933612614746378|0\.35709204798993505|0\.3390992681026839|0\.32595430350852556|0\.2982364650808825|
|Precision|0\.4874729561439978|0\.48299665579640344|0\.48257092371353894|0\.47618103606302115|0\.4659453701846607|0\.4627936346991008|0\.4463002013881355|0\.4482502907205976|0\.42936668491439|0\.42179947255457995|0\.4210112635890541|0\.419992178466476|0\.40633065314814026|0\.3982022538874536|0\.3793709754833736|0\.3878947666751313|0\.31748948015157624|0\.29848434876120966|
|F1 Score|0\.48364906264711555|0\.4820740600661711|0\.48013099700829986|0\.4747294688325296|0\.4619179523466987|0\.4604249706134107|0\.4445842616422033|0\.42420255015331937|0\.4260735394885707|0\.413796342271942|0\.4093378028521228|0\.4117283025225354|0\.4004317790331446|0\.38183735819807363|0\.3255541547284067|0\.31931761937572006|0\.3203328970233061|0\.2928699322685451|


## [3. Linear regression using embeding (click to redirect)](https://github.com/Adrian-Muino/DMML2022_Geneva/blob/main/Code/3.DMML_2022_Geneva_Embeding_Model.ipynb).

<img width="400" src="https://user-images.githubusercontent.com/114933900/208947363-6b57c2a0-20ff-40f9-bbf0-47139540f95c.png">


## [4. Bert & Tensor Model (click to redirect)](https://github.com/Adrian-Muino/DMML2022_Geneva/blob/main/Code/4.DMML_2022_Geneva_Bert%26Tensor_Model.ipynb)

<img width="400" src="https://fontmeme.com/permalink/221219/89919f5ad9759f663241eca5f028525c.png">


## [5. Link to the explainatory video] : (TO BE COMPLETED)


