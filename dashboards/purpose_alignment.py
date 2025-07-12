```python
def calculate_alignment(actions, purpose_statement):
    """
    Calculate the alignment of system actions to its stated purpose.

    Args:
    actions (list of str): List of actions taken by the system.
    purpose_statement (str): The stated purpose of the system.

    Returns:
    float: A percentage representing how closely the actions align with the purpose.
    """
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    # Combine the purpose statement with the list of actions
    documents = [purpose_statement] + actions

    # Create a TF-IDF Vectorizer
    tfidf_vectorizer = TfidfVectorizer()

    # Fit and transform the documents
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

    # Calculate cosine similarity between the purpose statement and each action
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])

    # Calculate the average similarity
    average_similarity = cosine_similarities.mean()

    # Convert to percentage
    alignment_percentage = average_similarity * 100

    return alignment_percentage

# Example usage
actions = [
    "The system processes user data to improve user experience.",
    "The system analyzes user preferences.",
    "The system sends promotional emails."
]
purpose_statement = "The system is designed to enhance user experience by analyzing user data."

alignment_score = calculate_alignment(actions, purpose_statement)
print(f"Alignment Score: {alignment_score:.2f}%")
```