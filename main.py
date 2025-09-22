from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# Model & vectorizer paths
rf_model_path = 'fake_news_rf_model.pkl'
lr_model_path = 'fake_news_lr_model.pkl'
vectorizer_path = 'vectorizer.pkl'

# Load models and vectorizer if files exist
if all(os.path.isfile(p) for p in [rf_model_path, lr_model_path, vectorizer_path]):
    with open(rf_model_path, 'rb') as f:
        rf_model = pickle.load(f)
    with open(lr_model_path, 'rb') as f:
        lr_model = pickle.load(f)
    with open(vectorizer_path, 'rb') as f:
        vectorizer = pickle.load(f)
else:
    print("❌ Model or Vectorizer file not found! Please train the models first.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    news_text = request.form['news_text']
    selected_model = request.form.get('model_choice')  # From dropdown in HTML

    # Vectorize input
    input_vector = vectorizer.transform([news_text])

    # Choose model
    if selected_model == "rf":
        prediction = rf_model.predict(input_vector)[0]
        model_used = "Random Forest"
    else:
        prediction = lr_model.predict(input_vector)[0]
        model_used = "Logistic Regression"

    # Prediction result
    result = '✅ True News' if prediction == 1 else '❌ Fake News'

    return render_template(
        'index.html',
        prediction_text=f"{result} (Predicted by {model_used})",
        original_text=news_text
    )

if __name__ == "__main__":
    app.run(debug=True)
