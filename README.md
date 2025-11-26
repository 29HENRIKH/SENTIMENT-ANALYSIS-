<div align="center">

# 🌀 VIBE-LENZZ

**Customer Sentiment Analysis at Scale**

_"Turn raw customer feedback into actionable business insights."_

</div>

---

## 📖 Overview

**VIBE-LENZZ** is a machine learning-powered application designed to analyze customer sentiments from textual feedback. It empowers organizations to classify comments, identify pain points, and make data-driven decisions to improve products and services.

---

## 📉 Problem Statement

In the digital economy, a company’s financial health—spanning profits, sales, and market share—is tightly linked to its online reputation. Public perception acts as a primary filter for potential customers.

Reliance on this feedback loop creates a critical vulnerability: if negative sentiment outweighs positive, companies risk significant revenue loss, rapid customer churn, and long-term brand damage.

**VIBE-LENZZ addresses this by analyzing feedback at scale, moving beyond observation to actionable insights.**

---

## 🚀 Motivation: The Cost of Ignoring Sentiment

Real-world examples highlight the financial risks of failing to analyze customer feedback effectively.

### 🎮 Case Study 1: *The Last of Us Part II* (Naughty Dog)

<img src="assets/TLOUP2.png" alt="The Last of Us Part 2 Banner" width="100%">

| Challenge | Failure | Impact |
|-----------|---------|--------|
| Review Bombing driven by ideological polarization | No nuanced tracking; failed to separate valid criticism from trolling | Long-term sales potential damaged due to uncontrolled negative narrative |

**✨ VIBE-LENZZ Solution:** Real-time dashboards would have immediately identified specific grievance themes for a strategic PR response.

---

### 👗 Case Study 2: Fashion Nova

<img src="assets/fn2.webp" alt="Fashion Nova Banner" width="100%">

| Challenge | Failure | Impact |
|-----------|---------|--------|
| $4.2 million FTC fine for suppressing negative reviews | Hid comments under 4 stars, ignoring sizing/quality issues | Loss of consumer trust and massive financial penalties |

**✨ VIBE-LENZZ Solution:** Automated analysis would have highlighted product flaws for immediate improvement rather than hiding them.

---

## ⚙️ How It Works

1. **📥 Input:** Upload CSV (with a `Text` column) or PDF files containing raw comments.  
2. **🧹 Preprocessing:** Automatic cleaning of noise (URLs, emojis, stopwords) and text normalization.  
3. **🧮 Vectorization:** TF-IDF transforms text to weigh impactful words and capture sentiment drivers.  
4. **🤖 Prediction:** An SVM model classifies sentiment (Positive/Negative/Neutral).  
5. **📊 Visualization:** Generates charts and a downloadable PDF report.  
6. **🗣️ Linguistic Insights:** Extracts key drivers behind customer opinions by analyzing word frequency patterns.  

---

## 📊 Linguistic Insights: Top Words by Sentiment

<div align="center">
<img src="assets/topwords.png" alt="Top Words by Sentiment Analysis" width="800">
<p><em>(Most frequent terms driving Positive vs. Negative sentiment)</em></p>
</div>

**Key Findings:**

- 🟢 **Positive Drivers:** Words like *"Love"*, *"Best"*, *"Great"* correlate with user satisfaction and brand loyalty.  
- 🔴 **Negative Drivers:** Words like *"Crash"*, *"Slow"*, *"Refund"* highlight technical or service issues leading to churn.  
- 🔵 **Neutral Signals:** Words like *"Update"*, *"Release"* indicate informational queries rather than emotional feedback.  

**💡 Business Value:** Companies can identify the exact root causes of user dissatisfaction and take targeted action.

---

## 📊 Model Performance & Error Analysis

### 1. Model Comparison

We benchmarked **Naive Bayes**, **Logistic Regression**, and **Linear SVM** using **confusion matrices**.

| Model | Performance |
|-------|------------|
| Naive Bayes | Misclassified 'Neutral' as 'Negative' |
| Logistic Regression | Moderate performance |
| Linear SVM | Most balanced accuracy; correctly identified 2,877 Neutral cases |

<div align="center">
<img src="assets/NBAL.png" width="250">
<img src="assets/SVMAL.png" width="250">
<img src="assets/LRAL.png" width="250">
</div>

**🏆 Why Linear SVM Won:**  
- Neutral comments are the hardest class; SVM provided the most accurate classification.

---

### 2. Deep Dive: The "Neutrality" Challenge

Despite strong performance, the model occasionally confuses Neutral comments with Positive or Negative ones.

**Vocabulary Overlap Problem:**  
- Neutral comments often share high-frequency nouns and verbs with polarized comments but lack defining adjectives.  
- Examples: *"game"*, *"time"*, *"just"* appear across all sentiments.

<div align="center">
<img src="assets/sharedsnts.png" alt="Vocabulary Overlap Graph" width="700">
</div>

**Implication:**  
- Words like *"I played the game"* (Neutral) vs *"This game is broken"* (Negative) look similar to the model based purely on frequency.  
- **Future solution:** Implement **contextual embeddings (BERT)** to capture subtle differences.

---

## 📂 Data Requirements

- **CSV Files:** Must contain a column named `Text`.  
- **PDF Files:** Multiple pages supported; text will be automatically extracted.

---

## 🔧 Installation & Usage

**Clone the repository:**

```bash
git clone https://github.com/your-username/vibe-lenzz.git
cd vibe-lenzz

