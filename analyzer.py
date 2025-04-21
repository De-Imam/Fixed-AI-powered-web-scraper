from transformers import pipeline

# Load the pre-trained sentiment-analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

# Analyze sentiment using Hugging Face
def analyze_sentiment(text):
    result = sentiment_analyzer(text)
    return result[0]['label']  # 'POSITIVE' or 'NEGATIVE'
