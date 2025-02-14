import pandas as pd
import matplotlib.pyplot as plt

# File paths
articles_file_path = r"final_matched_articles_with_gender.csv"
output_file_path = r"gender_performance_yearly_updated_v2.csv"

# Load data
print("Loading articles data...")
articles_data = pd.read_csv(articles_file_path, low_memory=False, encoding='utf-8')

# Filter for years starting from 2000 and genders Male/Female
print("Filtering data...")
filtered_data = articles_data[(articles_data['Publication Year'] >= 2000) &
                               (articles_data['Gender'].isin(['Male', 'Female']))]

# Calculate performance metrics with non-linear scaling
print("Calculating performance metrics...")
# Avoid division by zero and handle NaN
filtered_data['Cited Reference Count'] = filtered_data['Cited Reference Count'].fillna(0)
filtered_data['Article Count'] = filtered_data['Article Title'].apply(lambda x: 1 if not pd.isna(x) else 0)

# Updated performance metric:
# Square the publication count to emphasize it more strongly
w1, w2, w3 = 1, 0.5, 0.5  # Weights
filtered_data['Performance Score'] = (w1 * (filtered_data['Article Count'] ** 2) +
                                      w2 * filtered_data['Cited Reference Count'] +
                                      w3 * (filtered_data['Cited Reference Count'] /
                                            filtered_data['Article Count']))

# Group data by Publication Year and Gender
print("Grouping and aggregating data...")
yearly_gender_performance = filtered_data.groupby(['Publication Year', 'Gender']).agg({
    'Performance Score': 'mean'
}).reset_index()

# Pivot data for plotting
pivoted_gender_data = yearly_gender_performance.pivot(index='Publication Year', columns='Gender', values='Performance Score')

# Plot results
print("Plotting results...")
plt.figure(figsize=(12, 8))

# Plot Male and Female performance trends
for gender in ['Male', 'Female']:
    if gender in pivoted_gender_data.columns:
        plt.plot(pivoted_gender_data.index, pivoted_gender_data[gender], label=f"{gender} Performance", marker='o')

plt.xlabel('Publication Year')
plt.ylabel('Average Performance Score')
plt.title('Yearly Performance by Gender')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the plot
plot_path = r"gender_performance_yearly_updated_v2_plot.png"
plt.savefig(plot_path)
print(f"Plot saved to {plot_path}")
plt.show()

# Save the results to a CSV file
print("Saving performance data to CSV...")
pivoted_gender_data.to_csv(output_file_path, index=True, encoding='utf-8-sig')
print(f"Performance data saved to {output_file_path}")
