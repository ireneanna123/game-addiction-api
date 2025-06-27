# 🎮 Game Addiction Detection (Text Classification)

This project is a simple machine learning system that predicts whether a user's text reflects signs of **game addiction**. It includes a trained classifier model, a web-based frontend, and a REST API.

---

## 📌 Features

- 🔍 Classifies text as `Addicted` or `Not Addicted`
- 🧠 Trained using a cleaned and balanced dataset from Kaggle
- 🌐 API-based prediction (hosted on Render)
- 💻 Simple HTML frontend with batch testing support
- ✅ Easily extensible and interpretable

---
## 🗃️ Dataset Source
> 🎯 **Dataset:** [Digital Game Addiction Data (Version 2)](https://www.kaggle.com/datasets/jocelyndumlao/digital-game-addiction-data-version-2)  
> 👤 **Author:** jocelyndumlao  
> 📎 **Note:** A cleaned and relabeled version of this dataset was used for better accuracy and balance.
> ## 🛠️ How It Works

1. **User inputs** a sentence about gaming behavior.
2. **The sentence is sent** to an ML model via API.
3. **The model classifies** the sentence as `"Addicted"` or `"Not Addicted"` based on patterns in the text.

---

## 📊 Model Overview

- **Algorithm:** Logistic Regression
- **Vectorizer:** TF-IDF
- **Frameworks:** `scikit-learn`, `Flask`
- **Training/Testing:** 80/20 split
- **Accuracy:** Varies with dataset quality (see evaluation)

---

