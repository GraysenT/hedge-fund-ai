Below is a Python script that analyzes recent system behavior logs and compares them to the long-term purpose and mission alignment. This script assumes you have a structured log file (e.g., a CSV file) containing system behavior data and a text file outlining the system's purpose and mission. The script uses natural language processing (NLP) to analyze the alignment between the system's recent activities and its defined mission.

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure that NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    # Tokenize text
    tokens = word_tokenize(text.lower())
    # Remove stopwords
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    # Join tokens back to string
    return ' '.join(tokens)

def load_system_logs(log_file_path):
    # Load logs from a CSV file
    return pd.read_csv(log_file_path)

def load_mission_statement(mission_file_path):
    # Load mission statement from a text file
    with open(mission_file_path, 'r') as file:
        mission_statement = file.read()
    return mission_statement

def analyze_alignment(logs, mission_statement):
    # Preprocess logs and mission statement
    logs['processed'] = logs['activity'].apply(preprocess_text)
    processed_mission = preprocess_text(mission_statement)
    
    # Combine all logs into a single document
    combined_logs = ' '.join(logs['processed'].tolist())
    
    # Vectorize the documents using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([combined_logs, processed_mission])
    
    # Calculate cosine similarity
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity[0][0]

def main():
    log_file_path = 'system_logs.csv'  # Path to the system logs file
    mission_file_path = 'mission_statement.txt'  # Path to the mission statement file
    
    # Load data
    logs = load_system_logs(log_file_path)
    mission_statement = load_mission_statement(mission_file_path)
    
    # Analyze alignment
    alignment_score = analyze_alignment(logs, mission_statement)
    print(f"Alignment Score: {alignment_score:.2f}")

if __name__ == "__main__":
    main()
```

### Explanation:
1. **Data Loading**: The script loads system behavior logs from a CSV file and a mission statement from a text file.
2. **Preprocessing**: Text data is preprocessed by tokenizing, converting to lowercase, and removing stopwords.
3. **TF-IDF Vectorization**: Both the combined logs and the mission statement are converted into TF-IDF vectors.
4. **Cosine Similarity**: The script calculates the cosine similarity between the vectorized log data and the mission statement to quantify alignment.

### Requirements:
- Ensure you have the necessary files (`system_logs.csv` and `mission_statement.txt`) and they are formatted correctly.
- The CSV file should have at least one column named 'activity' which contains text descriptions of system activities.
- Python libraries: `pandas`, `nltk`, `sklearn` need to be installed. You can install them using pip (`pip install pandas nltk scikit-learn`).