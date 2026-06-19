from textblob import TextBlob

positive = []
negative = []
neutral = []


def analyze_sentiment(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            text = line.strip()

            if not text:
                continue

            blob = TextBlob(text)
            polarity = blob.sentiment.polarity

            if polarity > 0:
                positive.append(text)

            elif polarity < 0:
                negative.append(text)

            else:
                neutral.append(text)


# Run function
file_path = r"C:\Users\adnan\AI-ML-Learning-Journey\sentiment-analysis\text.txt"
analyze_sentiment(file_path)

# Print results
print("Positive sentences:")
for sentence in positive:
    print("-", sentence)

print("\nNegative sentences:")
for sentence in negative:
    print("-", sentence)

print("\nNeutral sentences:")
for sentence in neutral:
    print("-", sentence)

# Summary
print("\n===== SUMMARY =====")
print(f"Positive: {len(positive)}")
print(f"Neutral: {len(neutral)}")
print(f"Negative: {len(negative)}")