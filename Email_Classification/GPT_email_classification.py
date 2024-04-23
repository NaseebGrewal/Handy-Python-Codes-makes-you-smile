import pandas as pd
import openai

# Set up OpenAI API
openai.api_key = "YOUR_API_KEY"  # Replace with your OpenAI API key

# Load and preprocess the data
data = pd.read_csv("emails.csv")  # Replace with your CSV file
data.dropna(inplace=True)  # Remove rows with missing values
X = data["body"]

# Analyze email content and generate category suggestions
category_suggestions = []
for email in X:
    # Generate response using ChatGPT
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=email,
        max_tokens=100,
        stop=None,  # Remove stop conditions to allow for full responses
    )
    suggestion = response.choices[0].text.strip()
    category_suggestions.append(suggestion)

# Add category suggestions to the DataFrame
data["category_suggestion"] = category_suggestions

# Save the results to a new CSV file
data.to_csv("categorized_emails.csv", index=False)
