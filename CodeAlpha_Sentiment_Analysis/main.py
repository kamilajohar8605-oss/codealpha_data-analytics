from textblob import TextBlob

print("=== Sentiment Analysis ===")

review = input("Enter a review: ")

analysis = TextBlob(review)
polarity = analysis.sentiment.polarity

if polarity > 0:
    sentiment = "Positive"
elif polarity < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print("\nReview:", review)
print("Polarity Score:", polarity)
print("Sentiment:", sentiment)