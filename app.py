# VIBE-LENZZ Streamlit App
import streamlit as st
import pandas as pd
import joblib
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from PyPDF2 import PdfReader

# ---------------------------
# Load trained model & vectorizer
# ---------------------------
svm_model = joblib.load("models/linear_svm_sentiment_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# ---------------------------
# Text cleaning function
# ---------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# ---------------------------
# Streamlit App UI
# ---------------------------
st.set_page_config(page_title="VIBE-LENZZ 🌀", page_icon="🌀")
st.title("VIBE-LENZZ 🌀")
st.subheader("Your Ultimate Sentiment Analysis Lens for Customer Insights 🌟")
st.write("Analyze reviews, comments, or feedback to discover what customers feel. Upload CSVs or PDFs, and generate insightful visual reports. 📊")

# ---------------------------
# File Upload (CSV or PDF)
# ---------------------------
uploaded_file = st.file_uploader("📂 Upload CSV (Text column) or PDF", type=["csv", "pdf"])

if uploaded_file:
    df = pd.DataFrame()
    if uploaded_file.type == "application/pdf":
        # Extract text from PDF
        reader = PdfReader(uploaded_file)
        texts = []
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                texts.append(page_text)
        df = pd.DataFrame({'Text': texts})
        st.info(f"📝 {len(df)} pages extracted from PDF for analysis.")
    elif uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        if 'Text' not in df.columns:
            st.error("❌ CSV must contain a 'Text' column.")
        else:
            st.info(f"📝 {len(df)} comments loaded from CSV.")

    if not df.empty:
        # Clean & vectorize
        df['clean_text'] = df['Text'].apply(clean_text)
        X_vect = vectorizer.transform(df['clean_text'])
        df['Sentiment'] = svm_model.predict(X_vect)

        # ---------------------------
        # Sentiment Percentages
        # ---------------------------
        sentiment_counts = df['Sentiment'].value_counts(normalize=True) * 100
        st.subheader("📊 Sentiment Distribution (%)")

        # ---------------------------
        # Top words per sentiment
        # ---------------------------
        st.subheader("🔑 Most Common Words Per Sentiment")
        cv = CountVectorizer(stop_words='english', max_features=50)
        X_counts = cv.fit_transform(df['clean_text'])
        words_df = pd.DataFrame(X_counts.toarray(), columns=cv.get_feature_names_out())
        words_df['Sentiment'] = df['Sentiment']

        top_words_dict = {}
        for sentiment in df['Sentiment'].unique():
            # Only sum numeric columns (word counts)
            top_words = words_df[words_df['Sentiment'] == sentiment].drop(columns=['Sentiment']).sum().sort_values(ascending=False).head(10)
            top_words_dict[sentiment] = top_words.rename("No of Appearances")  # rename column
            st.write(f"{'😊' if sentiment=='Positive' else '😞'} Top words in {sentiment} comments:")
            st.bar_chart(top_words_dict[sentiment])

        # ---------------------------
        # Pie chart & Bar chart side by side
        # ---------------------------
        st.subheader("📊 Overview: Sentiment & Top Words")
        col1, col2 = st.columns(2)

        # Pie chart
        with col1:
            fig1, ax1 = plt.subplots(figsize=(4,4))
            colors = ['green' if s.lower() == 'positive' else 'red' for s in sentiment_counts.index]
            emojis = {'Positive': '😊', 'Negative': '😞'}
            labels = [f"{emojis.get(s, '')} {s}" for s in sentiment_counts.index]
            ax1.pie(sentiment_counts.values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
            ax1.axis('equal')
            st.pyplot(fig1)

        # Bar chart of top words for most prevalent sentiment
        with col2:
            main_sentiment = df['Sentiment'].value_counts().idxmax()
            top_words_main = top_words_dict[main_sentiment]
            fig2, ax2 = plt.subplots(figsize=(4,4))
            top_words_main.plot(kind='bar', color='skyblue', ax=ax2)
            ax2.set_title(f"Top Words in {main_sentiment} Comments")
            ax2.set_ylabel("No of Appearances")
            ax2.set_xlabel("Words")
            plt.xticks(rotation=45, ha='right')
            st.pyplot(fig2)

        # ---------------------------
        # Recommendations
        # ---------------------------
        st.subheader("💡 Recommendations")
        recommendations = []

        # Recommendations for Negative comments
        if sentiment_counts.get('Negative', 0) > 0:
            recommendations.append("⚠️ Negative Feedback Suggestions:")
            recommendations.append("- Focus on improving product quality and service reliability.")
            recommendations.append("- Address common complaints highlighted in top words.")
            recommendations.append("- Engage with customers who leave negative feedback to resolve issues.")
            recommendations.append("- Monitor recurring pain points and implement corrective measures.")

        # Recommendations for Positive comments
        if sentiment_counts.get('Positive', 0) > 0:
            recommendations.append("✅ Positive Feedback Suggestions:")
            recommendations.append("- Maintain strategies that are generating satisfaction.")
            recommendations.append("- Leverage positive feedback in marketing and promotions.")
            recommendations.append("- Recognize teams or products that are consistently praised.")
            recommendations.append("- Analyze positive trends to replicate success across other areas.")

        for rec in recommendations:
            st.write(f"- {rec}")