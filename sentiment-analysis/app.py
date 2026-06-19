from textblob import TextBlob
def sentiment_analysis(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment, polarity
def main():
    text = input("Enter a sentence: ")
    sentiment, polarity = sentiment_analysis(text)
    print(f"Sentiment: {sentiment}, Polarity: {polarity}")
    text_2 = input("Analyze another text? (y/n): ")
    while text_2 == "y":
        text = input("Enter a sentence: ")
        sentiment, polarity = sentiment_analysis(text)
        print(f"Sentiment: {sentiment}, Polarity: {polarity}")
        text_2 = input("Analyze another text? (y/n): ")


if __name__ == "__main__":
    main()