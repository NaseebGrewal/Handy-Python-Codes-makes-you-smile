import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Step 1: Load and preprocess the data
data = pd.read_csv('emails.csv')  # Replace with your CSV file
data.dropna(inplace=True)  # Remove rows with missing values
X = data['body']

# Step 2: Feature extraction
vectorizer = TfidfVectorizer()
X_features = vectorizer.fit_transform(X)

# Step 3: Apply clustering algorithm
k = 3  # Number of clusters to create
clustering_model = KMeans(n_clusters=k, random_state=42)
clustering_model.fit(X_features)

# Step 4: Predict clusters for new emails
new_emails = pd.read_csv('new_emails.csv')  # Replace with the CSV file containing new emails
new_emails_features = vectorizer.transform(new_emails['body'])
new_emails['predicted_cluster'] = clustering_model.predict(new_emails_features)

# Step 5: Assign categories to clusters
# Based on your knowledge of the emails, manually assign categories to the predicted clusters
category_mapping = {
    0: 'Finance',
    1: 'Tracking',
    2: 'General'
}
new_emails['predicted_category'] = new_emails['predicted_cluster'].map(category_mapping)

# Step 6: Save the results to a new CSV file
new_emails.to_csv('categorized_emails.csv', index=False)
