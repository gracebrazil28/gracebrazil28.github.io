import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read all sheets from the Excel file
FILEPATH = "TMK_MEA_Reviewed.xlsx"
dataframes = read_all_sheets_from_excel(FILEPATH)

# Display the first few rows of each sheet
for sheet_name, df in dataframes.items():
    print(f"Sheet: {sheet_name}")
    print(df.head())
    print("\
")

# Print the number of rows in each sheet
print("Number of rows in each sheet:")
for sheet_name, df in dataframes.items():
    print(f"{sheet_name}: {len(df)} rows")

print("Data loaded successfully.")

# Visualize the distribution of 'Score Avg' across different sheets
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(15, 10))
fig.suptitle('Distribution of Score Avg Across Different Question Type', fontsize=16)

# Flatten the axes array for easy iteration
axes = axes.flatten()

# Plot each sheet
for i, (sheet_name, df) in enumerate(dataframes.items()):
    sns.histplot(df['Score Avg'], bins=10, kde=True, ax=axes[i])
    axes[i].set_title(sheet_name)
    axes[i].set_xlabel('Score Avg')
    axes[i].set_ylabel('Frequency')

# Remove any unused subplots
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# Create a box plot to visualize the distribution of scores across question types
plt.figure(figsize=(12, 6))
sns.boxplot(x='Question_Type', y='Score Avg', data=combined_df)
plt.title('Distribution of Score Avg Across Question Types')
plt.xlabel('Question Type')
plt.ylabel('Score Avg')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
