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
#### - Fashion Nova – lost revenue due to poor monitoring of social media backlash and negative feedback.
#### - VIBE-LENZZ enables organizations to proactively track sentiment trends and make informed decisions, potentially saving millions in lost revenue and reputation.

## HOW THE MODEL WORKS :
#### - Upload CSV or PDF files containing customer comments. 
#### - Clean and preprocess textual data automatically.
#### - TF-IDF vectorization to capture important words.
#### - SVM model for accurate sentiment prediction.
#### - Display pie chart for overall sentiment distribution.
#### - Display bar chart of top words per sentiment.
#### - Provide actionable recommendations for positive and negative feedback.
#### - User-friendly UI with emojis and interactive charts for better UX.

## DATA REQUIREMENTS
#### - CSV must contain a column named Text.
#### - PDF files can contain multiple pages of feedback; text is automatically extracted.
