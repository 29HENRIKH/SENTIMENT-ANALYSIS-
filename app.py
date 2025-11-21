# ------------------------------
# UPDATED STREAMLIT APP WITH Neutral & Irrelevant SUPPORT + FILTERING
# ------------------------------
import streamlit as st
import pandas as pd
import joblib
import re
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
from PyPDF2 import PdfReader

# ------------------------------
# Load model & vectorizer (supports 4 classes)
# ------------------------------
svm_model = joblib.load("models/linear_svm_sentiment_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# ------------------------------
# Text cleaning
# ------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# ------------------------------
# UI
# ------------------------------
st.set_page_config(page_title="VIBE-LENZZ 🌀", page_icon="🌀")
st.title("VIBE-LENZZ 🌀")
st.subheader("Sentiment Analysis for Customer Insights 🌟")

uploaded_file = st.file_uploader("📂 Upload CSV (Text column) or PDF", type=["csv", "pdf"])

if uploaded_file:
    df = pd.DataFrame()

    if uploaded_file.type == "application/pdf":
        reader = PdfReader(uploaded_file)
        texts = []
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                texts.append(page_text)
        df = pd.DataFrame({'Text': texts})
        st.info(f"📝 {len(df)} pages extracted.")

    elif uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        if 'Text' not in df.columns:
            st.error("❌ CSV must contain a 'Text' column.")
        else:
            st.info(f"📝 {len(df)} comments loaded.")

    if not df.empty:
        df['clean_text'] = df['Text'].apply(clean_text)
        X_vect = vectorizer.transform(df['clean_text'])
        df['Sentiment'] = svm_model.predict(X_vect)

        st.subheader("🎛️ Filter Sentiments")
        sentiments_available = df['Sentiment'].unique().tolist()
        selected_sentiments = st.multiselect(
            "Select sentiment(s) to display:",
            options=sentiments_available,
            default=sentiments_available
        )

        filtered_df = df[df['Sentiment'].isin(selected_sentiments)]

        st.subheader("📊 Sentiment Distribution (%)")
        sentiment_counts = filtered_df['Sentiment'].value_counts(normalize=True) * 100

        fig1, ax1 = plt.subplots(figsize=(4,4))
        ax1.pie(sentiment_counts.values, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)

        st.subheader("🔑 Most Common Words Per Sentiment")
        cv = CountVectorizer(stop_words='english', max_features=50)
        X_counts = cv.fit_transform(filtered_df['clean_text'])
        words_df = pd.DataFrame(X_counts.toarray(), columns=cv.get_feature_names_out())
        words_df['Sentiment'] = filtered_df['Sentiment']

        top_words_dict = {}

        for sentiment in selected_sentiments:
            temp = words_df[words_df['Sentiment'] == sentiment]
            top_words = temp.drop(columns=['Sentiment']).sum().sort_values(ascending=False).head(10)
            top_words_dict[sentiment] = top_words
            st.write(f"### Top words in {sentiment} comments:")
            st.bar_chart(top_words)

        st.subheader("📊 Overview: Top Words for General Sentiment")
        if len(selected_sentiments) > 0:
            main_sentiment = filtered_df['Sentiment'].value_counts().idxmax()
            fig2, ax2 = plt.subplots(figsize=(4,4))
            top_words_dict[main_sentiment].plot(kind='bar', ax=ax2)
            ax2.set_title(f"Top Words in {main_sentiment} Comments")
            plt.xticks(rotation=45, ha='right')
            st.pyplot(fig2)

        st.subheader("💡 Recommendations")
        if 'Negative' in selected_sentiments:
            st.write("- Address complaints, improve product reliability.")
        if 'Positive' in selected_sentiments:
            st.write("- Reinforce strategies generating satisfaction.")
        if 'Neutral' in selected_sentiments:
            st.write("- Convert neutral feedback into actionable insights.")
        if 'Irrelevant' in selected_sentiments:
            st.write("- Clean dataset or create filtering rules for irrelevant content.")