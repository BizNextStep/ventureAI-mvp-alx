from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

class IdeaProcessor:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.scaler = StandardScaler()

    def process_idea(self, idea):
        # Preprocess the idea description
        idea_description = idea['description']
        idea_description = self.vectorizer.fit_transform([idea_description])

        # Calculate the similarity between the idea and each business idea
        similarities = cosine_similarity(idea_description, self.vectorizer.fit_transform(df['description']))

        # Get the top 5 most similar business ideas
        top_5_indices = similarities.argsort()[-5:][::-1]

        # Return the top 5 business ideas
        return [df.iloc[i]['name'] for i in top_5_indices]

    def train_model(self, X, y):
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a random forest classifier
        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = model.predict(X_test)
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("Classification Report:")
        print(classification_report(y_test, y_pred))
        print("Confusion Matrix:")
        print(confusion_matrix(y_test, y_pred))

    def predict(self, X):
        # Use the trained model to make predictions
        y_pred = self.model.predict(X)
        return y_pred

# Example usage
idea_processor = IdeaProcessor()
idea_processor.train_model(X, y)
recommended_ideas = idea_processor.process_idea(idea)
print("Recommended ideas:", recommended_ideas)

