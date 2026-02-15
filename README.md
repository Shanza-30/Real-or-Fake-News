# 📰 Fake News Detector using Machine Learning

This project is a **web-based Fake News Detection system** built using **Python, Flask, and Machine Learning**. It helps users quickly identify whether a news article is **Real** or **Fake** by analyzing the text content using natural language processing techniques.


## 🚀 Project Overview

Fake news spreads rapidly on digital platforms and can mislead readers. This application provides a simple and effective solution by leveraging **TF-IDF text vectorization** and **machine learning classification models** to assess the authenticity of news articles.


## 🧠 Machine Learning Models Used

Two different models are implemented to allow comparison and flexibility:

 **Random Forest Classifier** 🌲
  An ensemble-based model that combines multiple decision trees to improve accuracy and robustness.

 **Logistic Regression** 📊
  A lightweight and efficient linear model that predicts the probability of a news article being real or fake.

Users can select which model to use at runtime.


## ✨ Key Features

* 📝 Enter any news article text for instant verification
* 🔄 Choose between **Random Forest** and **Logistic Regression** models
* 🎨 Color-coded results:

  * **Green** → Real News
  * **Red** → Fake News
* 🔍 Displays which model made the prediction (transparency)
* ⚡ Fast, lightweight, and easy-to-deploy **Flask web application**


## ⚙️ How It Works

1. User inputs news text through the web interface.
2. Text is preprocessed and converted into numerical features using **TF-IDF Vectorization**.
3. The selected machine learning model predicts whether the news is **Real** or **Fake**.
4. The result is displayed instantly with clear visual feedback.


## 🛠️ Technologies Used

* Python
* Flask
* scikit-learn
* TF-IDF Vectorizer
* HTML & CSS (for frontend UI)


## 📦 Deployment

The application is lightweight and can be easily deployed locally or on cloud platforms such as:

* Heroku
* Render
* PythonAnywhere


## 🔮 Future Enhancements

* 📈 Add deep learning models (LSTM, BERT) for improved accuracy
* 📊 Display prediction confidence scores
* 🧹 Advanced text preprocessing (lemmatization, named entity removal)
* 🌐 Deploy with a modern frontend (Streamlit / React)
* 📁 Enable bulk news verification via file upload


## 📌 Conclusion

This Fake News Detector demonstrates a complete **end-to-end NLP machine learning pipeline**, from text preprocessing and model training to real-time prediction via a web interface. It is an excellent project for learning **text classification, model comparison, and ML deployment**.
