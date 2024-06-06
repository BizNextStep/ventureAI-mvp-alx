import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
df = pd.read_csv('business_ideas.csv')

# Preprocess the text data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['description'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, df['category'], test_size=0.2, random_state=42)

# Train a Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Use the trained model to make recommendations
def recommend_ideas(idea_description):
    # Convert the idea description to a TF-IDF vector
    idea_vector = vectorizer.transform([idea_description])

    # Calculate the similarity between the idea and each business idea
    similarities = cosine_similarity(idea_vector, X)

    # Get the top 5 most similar business ideas
    top_5_indices = similarities.argsort()[-5:][::-1]

    # Return the top 5 business ideas
    return [df.iloc[i]['name'] for i in top_5_indices]

# Example usage
idea_description = "A new e-commerce platform for sustainable products"
recommended_ideas = recommend_ideas(idea_description)
print("Recommended ideas:", recommended_ideas)

