import pandas as pd

# Load the Orthogroups.tsv file
file_path = 'Orthogroups.tsv'
df = pd.read_csv(file_path, sep="\t")

# Filter rows where column '111' is not empty
filtered_df = df[df['111'].notna()]

# Save the filtered dataframe to a new file (optional)
filtered_df.to_csv('Filtered_Orthogroups.tsv', sep="\t", index=False)

# Display the first few rows of the filtered dataframe
print(filtered_df.head())
