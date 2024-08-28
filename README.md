

<h1 align="center"> Email/SMS Spam Classifier</h1>

<p align="center"> 
<img src="website/static/images/letter-8195496_1280.jpg" height="600px" width="900px">
</p>

## [App Link](http://3.90.173.204:8080/home)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) 
![GitHub Actions](https://img.shields.io/badge/githubactions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2> :floppy_disk: Table of Content</h2>

 
  * [Introduction](#Introduction)
  * [Problem Statement](#Problem-Statement)
  * [Objectives](#Objectives)
  * [Data Summary](#Data-Summary)
  * [Steps Involved](#Steps-Involved)
  * [EDA](#EDA)
  * [Algorithms used](#Algorithms-used)
  * [Conclusion](#Conclusion)


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)


<h2> 📄 Introduction</h2>

The SMS/Email Spam Classifier project utilizes machine learning to automatically identify and filter out spam messages from legitimate ones. By analyzing message content and characteristics, the classifier distinguishes between spam and non-spam messages with high accuracy. Through training on labeled datasets and evaluation on test datasets, the project aims to develop a robust spam detection system. Integration of this classifier into messaging platforms enhances security and usability by reducing the impact of unwanted spam messages.


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)


<h2> ❓ Problem Statement</h2>


The SMS/Email Spam Classifier project addresses the challenge of efficiently filtering out unwanted spam messages from legitimate ones. With the exponential growth of digital communication, users face an increasing volume of spam, leading to inconvenience, privacy concerns, and potential security risks. By developing a reliable spam detection system using machine learning techniques, this project aims to provide users with a seamless and secure messaging experience, free from the nuisance of unsolicited spam content.




![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2> 🎯 Objectives: </h2>

1. Develop a robust machine learning model to accurately classify SMS and email messages as either spam or legitimate.
2. Explore and analyze various feature extraction techniques to capture the distinguishing characteristics of spam messages.
3. Implement hyperparameter tuning and cross-validation to optimize the model's performance and generalization capabilities.
4. Provide an intuitive user interface for users to interact with the spam classifier, ensuring ease of use and accessibility.
5. Evaluate the effectiveness of the classifier using performance metrics such as precision, recall, and F1-score, aiming for high accuracy and reliability in spam detection.
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2> :book: Data Summary </h2>

The data contained 5,574 messages including spam and non-spam

The dataset contains the following information:

* **Messages**

* **Class** - Spam/Ham


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2> 📑 Steps involved </h2>

1. Exploring the data: Analyzing the features and target variable, checking for null values and duplicates, plotting the distribution of target variable, etc.

2. Text Preprocessing using stemming,stop words removal,tokenization,lower casing..etc

3. Future extraction using Count vectorizer and TFIDF

3. Train test split

4. Develop different models and evaluate them.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2>🛠️ EDA </h2>

In this project, the dependent variable is ‘Spam or Ham’, the prediction of which gives us message is spam or not

![image](images/spam_vs_ham.png)
![image](images/Number_of_Characters_in_Ham_Vs_Spam.png)
![image](images/Spam_Word_Cloud.png)
![image](images/Ham_Word_Cloud.png)

We can observe that the dataset is unbalanced.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2>Getting Started</h2>

1.[RawData](https://github.com/Muhliscm/spam_classifer/blob/main/spam.csv) <br>
2.[Exploratory Data Analysis scripts](https://github.com/Muhliscm/spam_classifer/blob/main/01_EDA.ipynb)<br>
3.[Machine learning model building scripts](https://github.com/Muhliscm/spam_classifer/blob/main/01_Model_building.ipynb)<br>


<h2>💻 Algorithms used</h2>

* Logistic Regression

* Kernal-SVM

* SVM
  
* Random Forest
  
* KNN

* Decision Tree

* Naive Bayes	


<h3> Model Comparison </h3>

All the models are evaluated on the basis of the following evaluation metrics.

![image](images/model_perfomance.png)

Selected Naive Bayes based on precision score

<h3> Best Hyper-parameters </h3>

* Naive Bayes:

- 'nb__alpha': 1.0
- 'tfidf__max_features': 3000
- 'tfidf__ngram_range': (1, 2)
  

<h2>:bulb: Conclusion</h2>

This project focuses on finding spam messages

* In eda we found that spam message have high median character count

* Among all these models Naive Bayes gives us a precision of of 100%


 
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- CREDITS -->
<h2 id="credits"> :scroll: Credits</h2>

MUHLIS CM | Data Scientist | Machine Learning Engineer 

<p> <i> Contact me for Data Science Project Collaborations</i></p>

[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/muhliscm/)
[![GitHub Badge](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Muhliscm)


