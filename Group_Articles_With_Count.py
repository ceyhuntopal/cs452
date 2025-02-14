import pandas as pd
import os

# Define file paths
input_file_path = r"merged_results.csv"
output_file_path = r"academics_with_articles.csv"

def combine_articles_by_academic():
    """ Combine all articles for each academic into the same row with article count """
    print("Loading the merged dataset...")
    # Load the combined dataset
    df = pd.read_csv(input_file_path, encoding='utf-8-sig', low_memory=False)

    print(f"Dataset loaded. Total rows: {len(df)}")
    print("Processing data to combine articles for each academic...")

    # Group by 'Academic Name' and 'University' and aggregate articles into lists
    grouped_df = df.groupby(['Academic Name', 'University']).agg({
        'Article Title': lambda x: '; '.join(x.dropna().unique()),   # Combine unique article titles
        'Journal': lambda x: '; '.join(x.dropna().unique()),        # Combine unique journals
        'Publication Year': lambda x: '; '.join(x.dropna().astype(str).unique()),  # Combine unique years
        'Citation Count': lambda x: '; '.join(x.dropna().astype(str).unique()),   # Combine citation counts
        'Article Title': 'count'  # Count the number of articles
    }).rename(columns={'Article Title': 'Article Count'}).reset_index()

    print("Data processing complete.")
    print(f"Total academics after grouping: {len(grouped_df)}")

    # Save the result to a new CSV file
    grouped_df.to_csv(output_file_path, index=False, encoding='utf-8-sig')
    print(f"Combined data saved to: {output_file_path}")

if __name__ == "__main__":
    combine_articles_by_academic()


import pandas as pd

# Read the Excel file
df = pd.read_excel("academics_with_articles.xlsx", engine='openpyxl')

# Save as CSV
df.to_csv("academics_with_articles.csv", index=False, encoding='utf-8-sig')
