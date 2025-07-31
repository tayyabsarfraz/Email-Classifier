# 📧 Email Spam Classifier (SVM + TF-IDF + Streamlit)

This project is an intelligent **Email Spam Classifier** built using modern Natural Language Processing (NLP) techniques and machine learning models. The system is designed to automatically classify email content as **Spam** or **Not Spam (Ham)** based on the text content.

---

## 🚀 Technologies & Tools Used

- 🐍 **Python 3**
- 🧠 **Scikit-learn** for machine learning models
- 🧾 **TfidfVectorizer** for feature extraction (text to numerical vector conversion)
- 📊 **LinearSVC (Support Vector Machine)** for classification
- 🧰 **Joblib** for model serialization
- 🌐 **Streamlit** for building a lightweight, interactive web interface
- 📁 **Pandas & NumPy** for data manipulation
- 🛠️ **Git & GitHub** for version control and deployment

---

## 📚 Methodology

1. **Text Vectorization**  
   Raw email text is transformed using **TF-IDF** to capture the importance of words while reducing the impact of frequently occurring ones.

2. **Train-Test Split**  
   Dataset is split using an 80/20 ratio with `stratify` to maintain label balance.

3. **Model Training**  
   A **Linear Support Vector Machine (LinearSVC)** is trained on the TF-IDF features for high performance and efficiency in high-dimensional text data.

4. **Model Evaluation**  
   The model is evaluated using multiple metrics to ensure robustness and reliability.

---

## 📈 Evaluation Metrics & Results

| Metric       | Score  |
|--------------|--------|
| ✅ Accuracy   | **98.2%** |
| 🎯 Precision  | **98.4%** |
| 📥 Recall     | **98.1%** |
| 🧠 F1 Score   | **98.2%** |

> The model demonstrates high performance in detecting spam messages with excellent generalization on unseen data.

---

## 🖥️ App Demo

Users can input any email content into a clean and interactive **Streamlit UI**, and the system will instantly classify it as:

- ✅ **Not Spam (Ham)**
- 🚨 **Spam**

```python
streamlit run app.py
