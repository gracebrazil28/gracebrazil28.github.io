import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Convert 'Compactness' to numeric, replacing non-numeric values with NaN
combined_df['Compactness'] = pd.to_numeric(combined_df['Compactness'], errors='coerce')

# Check for any remaining non-numeric values
non_numeric_counts = combined_df[['Correctness', 'Completeness', 'Confidence', 'Comprehensibility', 'Compactness']].isnull().sum()
print("Count of NaN values in each column after conversion:")
print(non_numeric_counts)

# Calculate the correlation matrix for the scoring categories
scoring_columns = ['Correctness', 'Completeness', 'Confidence', 'Comprehensibility', 'Compactness']
correlation_matrix = combined_df[scoring_columns].corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
plt.title('Correlation Matrix of Scoring Categories')
plt.tight_layout()
plt.show()

print("\
Correlation matrix:")
print(correlation_matrix)

# Calculate mean scores for each category
mean_scores = combined_df[scoring_columns].mean().sort_values(ascending=False)
print("\
Mean scores for each category:")
print(mean_scores)

print("\
Analysis complete.")
