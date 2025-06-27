from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ Add this line
import pickle

app = Flask(__name__)
CORS(app)  # ✅ Add this line to allow frontend calls

# Load the model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return "🎮 Game Addiction Detection API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No input text provided."}), 400
    vect_text = vectorizer.transform([text.lower()])
    prediction = model.predict(vect_text)[0]
    result = "Addicted" if prediction == 1 else "Not Addicted"
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
