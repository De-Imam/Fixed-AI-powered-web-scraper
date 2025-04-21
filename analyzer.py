from textblob import TextBlob

def analyze_sentiment(text):
    if not text.strip():
        return "No content"
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return f"Sentiment polarity: {polarity:.2f} ({'Positive' if polarity > 0 else 'Negative' if polarity < 0 else 'Neutral'})"