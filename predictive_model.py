from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def train_model(data):
    # Assuming you have a labeled dataset for training
    X = data['text']
    y = data['label']  # Replace with actual labels
    vectorizer = CountVectorizer()
    X_vectorized = vectorizer.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2)
    model = MultinomialNB()
    model.fit(X_train, y_train)
    return model, vectorizer
