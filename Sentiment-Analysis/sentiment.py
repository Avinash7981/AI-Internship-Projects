import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = {
    "text": [
        "I love this product",
        "This is amazing",
        "Very happy with service",
        "Worst experience ever",
        "I hate this",
        "Very bad product"
    ],
    "sentiment": [
        "positive",
        "positive",
        "positive",
        "negative",
        "negative",
        "negative"
    ]
}

df = pd.DataFrame(data)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text"])

model = MultinomialNB()
model.fit(X, df["sentiment"])

test = ["I hate this product"]
test_vector = vectorizer.transform(test)

prediction = model.predict(test_vector)

print("Sentiment:", prediction[0])