import pandas as pd
import matplotlib.pyplot as plt

# Load data
file_path = r"final_matched_articles_with_gender.csv"
data = pd.read_csv(file_path)

# Group by Academic Name and University to calculate individual metrics
academic_grouped = data.groupby(['Academic Name', 'University']).agg({
    'Article Title': 'count',  # Number of articles
    'Cited Reference Count': 'sum',  # Total citation count
}).reset_index()

# Calculate average citation count
academic_grouped['Average Citation'] = academic_grouped['Cited Reference Count'] / academic_grouped['Article Title']

# Calculate performance score
w1, w2, w3 = 1, 2, 1  # Weights
academic_grouped['Performance Score'] = (w1 * academic_grouped['Article Title'] +
                                         w2 * academic_grouped['Cited Reference Count'] +
                                         w3 * academic_grouped['Average Citation'])

# Group by University to calculate university-level metrics
university_grouped = academic_grouped.groupby('University').agg({
    'Article Title': 'sum',  # Total number of articles
    'Academic Name': 'count',  # Total number of academics
    'Performance Score': 'mean'  # Average performance score
}).reset_index()

# Calculate average articles per academic
university_grouped['Articles per Academic'] = university_grouped['Article Title'] / university_grouped['Academic Name']

# Filter universities with Performance Score > 1200 or Articles per Academic > 18
filtered_university_grouped = university_grouped[
    (university_grouped['Performance Score'] > 1200) | (university_grouped['Articles per Academic'] > 18)
]

# Scatter plot for all universities
plt.figure(figsize=(14, 8))
plt.scatter(university_grouped['Articles per Academic'], university_grouped['Performance Score'], 
            alpha=0.5, edgecolor='k', color='gray', label='All Universities')

# Highlight filtered universities in a different color
plt.scatter(filtered_university_grouped['Articles per Academic'], filtered_university_grouped['Performance Score'], 
            alpha=0.8, edgecolor='k', color='blue', label='Top Performance Universities')

# Annotate only the filtered universities
for i, row in filtered_university_grouped.iterrows():
    plt.text(row['Articles per Academic'], row['Performance Score'], row['University'], fontsize=8, alpha=0.7)

# Add labels, legend, and title
plt.xlabel('Average Articles per Academic')
plt.ylabel('Average Performance Score')
plt.title('Average Performance vs. Articles per Academic by University')
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()

# Save the filtered university-level results
output_path = r"filtered_university_performance_vs_articles.csv"
filtered_university_grouped.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"Filtered results saved to {output_path}")
