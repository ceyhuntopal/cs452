import pandas as pd
import matplotlib.pyplot as plt

# Load the university performance data
file_path = r"university_average_performance.csv"
data = pd.read_csv(file_path)

# Calculate per-academic article averages and performance scores
data['Articles per Academic'] = data['Total Articles'] / data['Number of Academics']

# Scatter plot
plt.figure(figsize=(12, 8))
plt.scatter(data['Articles per Academic'], data['Performance Score'], color='blue', alpha=0.7, edgecolor='k')

# Label the axes and title
plt.xlabel('Articles per Academic', fontsize=12)
plt.ylabel('Average Performance Score', fontsize=12)
plt.title('Academic Performance vs Articles per Academic', fontsize=14)

# Improve layout
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Show the plot
plt.show()
