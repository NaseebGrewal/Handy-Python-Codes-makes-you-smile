import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Step 1: Load and preprocess the data
data = pd.read_csv('emails.csv')  # Replace with your CSV file
data.dropna(inplace=True)  # Remove rows with missing values
X = data['body']
y = data['category']

# Step 2: Feature extraction
vectorizer = TfidfVectorizer()
X_features = vectorizer.fit_transform(X)

# Step 3: Train a classifier
X_train, X_test, y_train, y_test = train_test_split(X_features, y, test_size=0.2, random_state=42)
classifier = SVC()  # Replace with the classifier of your choice
classifier.fit(X_train, y_train)

# Step 4: Evaluate the model
y_pred = classifier.predict(X_test)
print(classification_report(y_test, y_pred))

# Step 5: Predict categories for new emails
new_emails = pd.read_csv('new_emails.csv')  # Replace with the CSV file containing new emails
new_emails_features = vectorizer.transform(new_emails['body'])
new_emails['predicted_category'] = classifier.predict(new_emails_features)

# Step 6: Save the results to a new CSV file
new_emails.to_csv('categorized_emails.csv', index=False)
