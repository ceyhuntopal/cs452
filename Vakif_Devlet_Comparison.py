import pandas as pd
import matplotlib.pyplot as plt
import unicodedata
import re

# File paths
universities_file_path = r"Turkiye_Universiteleri_Sehirleriyle.xlsx"
articles_file_path = r"final_matched_articles_with_gender.csv"
output_file_path = r"vakif_vs_devlet_performance.csv"

def normalize_to_english(name):
    """
    Convert Turkish characters to English and normalize string.
    """
    if pd.isna(name):
        return ""
    name = unicodedata.normalize("NFKD", name)
    name = re.sub(r"ı", "i", name)
    return re.sub(r"[^a-zA-Z0-9\s]", "", name).lower()

# Load data
print("Loading universities data...")
universities_data = pd.read_excel(universities_file_path, sheet_name=0, engine='openpyxl')
print("Universities Data Columns:", universities_data.columns)

print("Loading articles data...")
articles_data = pd.read_csv(articles_file_path, low_memory=False, encoding='utf-8')

# Normalize university names
print("Normalizing university names...")
universities_data['Normalized University'] = universities_data['Üniversite Adı'].apply(normalize_to_english)
articles_data['Normalized University'] = articles_data['University'].apply(normalize_to_english)

# Merge datasets on normalized university names
print("Merging datasets...")
merged_data = pd.merge(
    articles_data,
    universities_data[['Normalized University', 'Türü']],  # Include only necessary columns
    left_on='Normalized University',
    right_on='Normalized University',
    how='inner'
)

# Calculate performance metrics
print("Calculating performance metrics...")
# Add weights for performance calculation
w1, w2, w3 = 1, 2, 1
merged_data['Performance Score'] = (w1 * merged_data['Article Title'].apply(lambda x: 1 if not pd.isna(x) else 0) +
                                    w2 * merged_data['Cited Reference Count'].fillna(0) +
                                    w3 * (merged_data['Cited Reference Count'].fillna(0) /
                                          merged_data['Article Title'].apply(lambda x: 1 if not pd.isna(x) else 1)))

# Group data by Publication Year and University Type ('Türü')
print("Grouping and aggregating data...")
yearly_performance = merged_data.groupby(['Publication Year', 'Türü']).agg({
    'Performance Score': 'mean'
}).reset_index()

# Filter data for years after 2002
yearly_performance = yearly_performance[yearly_performance['Publication Year'] > 2003]

# Pivot data for plotting
pivoted_data = yearly_performance.pivot(index='Publication Year', columns='Türü', values='Performance Score')

# Plot results
print("Plotting results...")
plt.figure(figsize=(12, 8))
plt.plot(pivoted_data.index, pivoted_data['Devlet'], label='Devlet Universities', marker='o')
plt.plot(pivoted_data.index, pivoted_data['Vakıf'], label='Vakıf Universities', marker='o')

plt.xlabel('Publication Year')
plt.ylabel('Average Performance Score')
plt.title('Yearly Performance of Devlet vs Vakıf Universities (Post-2002)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the plot
plot_path = r"vakif_vs_devlet_performance_plot.png"
plt.savefig(plot_path)
print(f"Plot saved to {plot_path}")
plt.show()

# Save the results to a CSV file
print("Saving performance data to CSV...")
pivoted_data.to_csv(output_file_path, index=True, encoding='utf-8-sig')
print(f"Performance data saved to {output_file_path}")
