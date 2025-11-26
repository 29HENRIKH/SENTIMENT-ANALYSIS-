# 🌀 VIBE-LENZZ: Customer Sentiment Analysis at Scale

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-SVM-green)
![Status](https://img.shields.io/badge/Status-Maintained-brightgreen)

> **Turn raw customer feedback into actionable business insights.**

VIBE-LENZZ is a machine learning-powered application designed to analyze customer sentiments from textual feedback. It helps organizations classify comments, identify pain points, and make data-driven decisions to improve products and services.

---

## 📉 Problem Statement

In the digital economy, a company’s financial health—spanning profits, sales, and market share—is inextricably linked to its online reputation. Public perception, driven by user reviews and comments, acts as a primary filter for potential customers before they commit to a purchase.

The reliance on this feedback loop creates a critical vulnerability: if negative sentiment outweighs the positive, the consequences are immediate and severe. Companies face **significant revenue loss**, **rapid customer churn**, and **long-term damage to brand reputation**.

Therefore, manual monitoring is no longer sufficient. **Sentiment analysis is imperative** for understanding the emotional drivers behind consumer behavior. **VIBE-LENZZ** addresses this critical need by analyzing customer feedback at scale. It empowers organizations to move beyond simple observation and take data-driven actions to improve products, retain customers, and protect their bottom line.

---

## 🚀 Motivation & Impact

Many companies suffer significant losses due to unmonitored customer sentiment.

* **Case Study 1: The Last of Us Part II** – Faced "review bombing," leading to misinformed pricing and marketing strategies due to a lack of nuanced sentiment tracking.
* **Case Study 2: Fashion Nova** – Lost revenue and faced backlash by failing to monitor social media sentiment effectively and hiding negative reviews.

VIBE-LENZZ enables organizations to **proactively track sentiment trends**, potentially saving millions in lost revenue and preserving brand integrity.

---

## 🛠️ Overview & Features

**VIBE-LENZZ** is a Python-based Streamlit web application. It leverages **Support Vector Machines (SVM)** and **Naive Bayes** classifiers to process text from CSV or PDF uploads.

### Key Capabilities
* **📊 Sentiment Classification:** Categorizes feedback as Positive, Negative, Neutral, or Irrelevant.
* **🔍 Actionable Insights:** Highlights top influential words and provides strategic recommendations.
* **📈 Interactive Visualizations:** Features dynamic pie charts and bar charts for real-time data exploration.
* **📄 PDF Reporting:** Exports analysis results into clean, formatted PDF reports for stakeholders.

---

## ⚙️ How It Works

![VIBE-LENZZ System Workflow](assets/workflow_diagram.png)
*(Note: Ensure you upload your diagram image to an `assets` folder in your repo)*

1.  **Input:** Users upload **CSV** (with a `Text` column) or **PDF** files containing raw customer comments.
2.  **Preprocessing:** The system automatically cleans data by normalizing text and removing noise (URLs, emojis, numbers, stopwords).
3.  **Vectorization:** **TF-IDF** transforms text into numerical features, weighing impactful words heavily to capture sentiment drivers.
4.  **Prediction:** An **SVM model** classifies the sentiment. SVM is chosen for its exceptional performance on high-dimensional text data and robust decision boundaries.
5.  **Visualization:**
    * **Pie Charts:** Show overall sentiment distribution.
    * **Bar Charts:** Display the top frequent words driving each sentiment.
6.  **Reporting:** The app summarizes strengths/weaknesses and generates a downloadable PDF report.

---

## 📂 Data Requirements

To ensure the model performs correctly, please ensure your data meets the following criteria:

* **CSV Files:** Must contain a column explicitly named **`Text`**.
* **PDF Files:** Can contain multiple pages; the system will automatically extract all text.

---

## 💻 Tech Stack

* **Language:** Python
* **Framework:** Streamlit
* **Machine Learning:** Scikit-learn (SVM, Naive Bayes), TF-IDF Vectorizer
* **Data Processing:** Pandas, NumPy
* **NLP:** NLTK / Spacy
* **Visualization:** Matplotlib / Plotly

---

## 🔧 Installation & Usage

To run this project locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/vibe-lenzz.git](https://github.com/your-username/vibe-lenzz.git)
    cd vibe-lenzz
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

---

**Author:** [Henrick Reagan Sarai]
**Contact:** [LinkedIn ; Reagan Sarai]
