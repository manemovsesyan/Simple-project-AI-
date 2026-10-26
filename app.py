from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive (Դրական)"
    elif polarity < 0:
        return "Negative (Բացասական)"
    else:
        return "Neutral (Չեզոք)"

if __name__ == "__main__":
    sample_text = "I love learning about AI and Docker! It is amazing."
    result = analyze_sentiment(sample_text)
    print(f"Text: '{sample_text}'")
    print(f"Sentiment: {result}")
