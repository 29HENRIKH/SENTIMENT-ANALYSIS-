## SENTIMENT-ANALYSIS-
### VIBE-LENZZ 🌀 analyzes customer feedback, classifies comments as Positive or Negative, highlights top words, and gives actionable insights, helping organizations make data-driven decisions and improve products, services, and engagement

## PROBLEM STATEMENT :
#### In todays society we mostly tend to look at the comments , reviews and things of that nature before purchasing a product or getting a service from a company . The company may suffer if there are a lot more negative comments compared to positive comments and thats where VIBE LENZZ comes in . Companies can use the model to know the amount of positive or negative comments , hence directing the company to take action . This in turn helps the company make data driven decisions , make improvements in the product / service the company offers . 

## OVERVIEW :
#### - VIBE-LENZZ is a Python-based Streamlit web application designed to help companies, NGOs, and government organizations analyze customer feedback at scale. The app leverages machine learning models (SVM & Naive Bayes) to classify text into Positive and Negative sentiments.
#### - By analyzing comments from CSV or PDF uploads, VIBE-LENZZ provides:
  #### - Top words driving each sentiment.
  #### - Recommendations for improving products, services, and customer engagement.
  #### - Interactive visualizations including pie charts and bar charts for clear insights.

## MOTIVATION :
#### - Many companies face losses due to unmonitored customer sentiment. Two examples:
#### - The Last of Us Part II – faced “review bombing” which led to misinformed pricing and marketing strategies.
#### - Fashion Nova – lost revenue due to poor monitoring of social media backlash , hiding negative reviews from the public and negative feedback.
#### - VIBE-LENZZ enables organizations to proactively track sentiment trends and make informed decisions, potentially saving millions in lost revenue and reputation.

## HOW THE MODEL WORKS :
### - Upload CSV or PDF files containing customer comments.
#### - Your app supports multiple input formats, allowing users to bring in raw customer feedback from surveys, exports, or internal reporting tools.
### - Clean and preprocess textual data automatically.
#### - The system handles text normalization, removal of noise (URLs, emojis, numbers), tokenization, and stopword removal, ensuring high-quality input for the model.
### - TF-IDF vectorization to capture important words.
#### - TF-IDF transforms text into numerical features by giving higher weight to impactful words. This helps the model focus on terms that strongly influence sentiment.
### - SVM model for accurate sentiment prediction.
#### - A Support Vector Machine classifier is used because it performs exceptionally well on high-dimensional text data. It provides strong generalization and robust decision boundaries.
### - Display pie chart for overall sentiment distribution.
#### - The UI visualizes how many comments fall into each sentiment category, helping users quickly understand the polarity of customer feedback.
### - Display bar chart of top words per sentiment.
#### - The application extracts and displays the most frequent or influential words for each class, giving insight into what customers talk about the most.
### - Provide actionable recommendations for positive and negative feedback.
#### - Based on predicted sentiment, the system summarizes strengths, pain points, and opportunities for improvement—turning raw comments into strategic insights.
### - User-friendly UI with emojis and interactive charts for better UX.
#### - The application features a visually engaging design with emojis, collapsible sections, real-time feedback display, and interactive charts powered by Streamlit.
### - Export results into PDF reports.
#### - Users can download sentiment analysis insights, visualizations, and comment summaries as a clean, formatted PDF for presentations or documentation.
### - End-to-end pipeline ready for deployment.
#### - The entire workflow—from data ingestion to prediction and visualization—is containerizable and suitable for deployment on cloud platforms (Railway, GCP, AWS, Streamlit Cloud, etc.).

## DATA REQUIREMENTS
#### - CSV must contain a column named Text.
#### - PDF files can contain multiple pages of feedback; text is automatically extracted.
