```python
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Sample data: Feed ID, Past Usefulness Score, Risk Contribution Score
data = {
    'Feed_ID': [1, 2, 3, 4, 5],
    'Past_Usefulness': [8.0, 6.5, 9.0, 7.0, 5.5],
    'Risk_Contribution': [2.0, 3.5, 1.5, 4.0, 3.0]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Normalize the scores to a common scale
scaler = MinMaxScaler()
df[['Past_Usefulness', 'Risk_Contribution']] = scaler.fit_transform(df[['Past_Usefulness', 'Risk_Contribution']])

# Calculate a combined score with a higher weight on usefulness
df['Score'] = 0.7 * df['Past_Usefulness'] - 0.3 * df['Risk_Contribution']

# Sort feeds by the new score
df.sort_values(by='Score', ascending=False, inplace=True)

# Output the DataFrame with the new scores
print(df)
```