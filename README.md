<div align="center">

# 🌀 VIBE-LENZZ
### Customer Sentiment Analysis at Scale

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Maintained-00C853?style=for-the-badge)

<br />

> **"Turn raw customer feedback into actionable business insights."**

</div>

---

## 📖 Overview
**VIBE-LENZZ** is a machine learning-powered application designed to analyze customer sentiments from textual feedback. It empowers organizations to classify comments, identify pain points, and make data-driven decisions to improve products and services.

---

## 📉 Problem Statement

In the digital economy, a company’s financial health—spanning profits, sales, and market share—is inextricably linked to its online reputation. Public perception acts as a primary filter for potential customers.

The reliance on this feedback loop creates a critical vulnerability: if negative sentiment outweighs the positive, companies face **significant revenue loss**, **rapid customer churn**, and **long-term damage to brand reputation**.

**VIBE-LENZZ** addresses this by analyzing feedback at scale, moving beyond simple observation to data-driven action.

---

## 🚀 Motivation: The Cost of Ignoring Sentiment

Real-world examples illustrate the severe financial risks of failing to analyze customer feedback effectively.

### 🎮 Case Study 1: The Last of Us Part II (Naughty Dog)
| Challenge | Failure | Impact |
| :--- | :--- | :--- |
| **"Review Bombing"** driven by ideological polarization. | Lacking nuanced tracking, they failed to segment valid criticism from trolling. | **Long-term sales potential** was damaged due to an uncontrolled negative narrative. |
> **✨ The VIBE-LENZZ Solution:** Real-time dashboards would have identified specific grievance themes immediately for a strategic PR response.

### 👗 Case Study 2: Fashion Nova
| Challenge | Failure | Impact |
| :--- | :--- | :--- |
| **$4.2 million FTC fine** for suppressing negative reviews. | Hid comments under 4 stars, blinding them to sizing/quality issues. | **Loss of consumer trust** and massive financial penalties. |
> **✨ The VIBE-LENZZ Solution:** Automated analysis would have highlighted product flaws (e.g., sizing issues) for immediate improvement rather than hiding them.

---

## ⚙️ How It Works

<div align="center">
  <img src="assets/workflow_diagram.png" alt="VIBE-LENZZ Workflow" width="800">
</div>

1.  **📥 Input:** Upload **CSV** (with a `Text` column) or **PDF** files containing raw comments.
2.  **🧹 Preprocessing:** Auto-cleaning of noise (URLs, emojis, stopwords) and normalization.
3.  **🧮 Vectorization:** **TF-IDF** transforms text, weighing impactful words to capture sentiment drivers.
4.  **🤖 Prediction:** An **SVM model** classifies sentiment (Positive/Negative/Neutral).
5.  **📊 Visualization:** The app generates charts and a downloadable PDF report.

---

## 📊 Model Performance & Error Analysis

To ensure reliability, we benchmarked three algorithms: **Naive Bayes**, **Logistic Regression**, and **Linear SVM**.

### 1. Model Comparison
We utilized Confusion Matrices to visualize decision boundaries:

| Naive Bayes | Linear SVM (Selected) | Logistic Regression |
| :---: | :---: | :---: |
| <img src="assets/NBAL.png" width="250"> | <img src="assets/SVMAL.png" width="250"> | <img src="assets/LRAL.png" width="250"> |

**🏆 Why Linear SVM Won:**
* **Naive Bayes** struggled, misclassifying 'Neutral' data as 'Negative'.
* **Linear SVM** provided the most balanced accuracy, correctly identifying **2,877 Neutral cases** (the hardest class).

### 2. Deep Dive: The "Neutrality" Challenge
Despite SVM's strong performance, the model occasionally confuses **Neutral** comments with **Positive** or **Negative** ones.

**The "Vocabulary Overlap" Problem:**
Our error analysis reveals that "Neutral" comments often share high-frequency nouns and verbs with polarized comments but lack defining adjectives.

<div align="center">
  <img src="assets/sharedsnts.png" alt="Vocabulary Overlap Graph" width="700">
</div>

* **Evidence:** As seen above, words like **"game"**, **"time"**, and **"just"** appear massively across **all three sentiments**.
* **The Dilemma:** Because these words lack inherent polarity, the model struggles to distinguish a neutral statement (*"I played the game"*) from a negative one (*"This game is broken"*) based purely on frequency.
* **Conclusion:** Future iterations will implement **Contextual Embeddings (BERT)** to solve this ambiguity.

---

## 📂 Data Requirements

To ensure the model performs correctly, please ensure your data meets the following criteria:
* **CSV Files:** Must contain a column explicitly named **`Text`**.
* **PDF Files:** Can contain multiple pages; the system will automatically extract all text.

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

<div align="center">

### 👤 Author

**Henrick Reagan Sarai**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/reagan-sarai/)

</div>
