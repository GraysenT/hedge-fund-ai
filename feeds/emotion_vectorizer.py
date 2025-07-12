```python
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Sample data
data = {
    'text': ["I love this product", "This is the worst experience ever", "Absolutely fantastic service!", "I'm not happy with this"],
    'emotion': ['positive', 'negative', 'positive', 'negative']
}

df = pd.DataFrame(data)

# Text feature extraction
vectorizer = TfidfVectorizer(max_features=100)
X_text = vectorizer.fit_transform(df['text']).toarray()

# Sentiment analysis
def get_sentiment_scores(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    return [scores['neg'], scores['neu'], scores['pos'], scores['compound']]

sentiment_features = np.array([get_sentiment_scores(text) for text in df['text']])

# Combine text features and sentiment scores
X_combined = np.hstack((X_text, sentiment_features))

# Label encoding
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df['emotion'])

# Dimensionality reduction
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X_combined)

# Resulting emotion-labeled vector space
emotion_vectors = pd.DataFrame(X_reduced, columns=['Component 1', 'Component 2'])
emotion_vectors['Emotion'] = label_encoder.inverse_transform(y)

print(emotion_vectors)
```

This Python script uses TF-IDF for text feature extraction, VADER for sentiment analysis, and PCA for reducing the dimensionality of the combined feature space into a 2D emotion-labeled vector space.