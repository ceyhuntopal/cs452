# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import re

# File paths
file_path = r"final_matched_articles_with_details.csv"
output_csv = r"faculty_yearly_publications.csv"

# Function to extract faculty information from the Details column
def extract_faculty(details):
    try:
        details = details.lower()
        details = (details.replace("\u00fc", "u").replace("\u00f6", "o").replace("\u00e7", "c")
                          .replace("\u015f", "s").replace("\u0131", "i").replace("\u011f", "g"))
        match = re.search(r'/([^/]+)/', details)  # Extract the text between first and second "/"
        if match:
            return match.group(1).strip()
        return "Unknown Faculty"
    except Exception as e:
        return "Unknown Faculty"

# Load data
try:
    print("Loading data...")
    data = pd.read_csv(file_path, encoding='utf-8', low_memory=False)
    print(f"Data loaded successfully. Number of rows: {len(data)}")
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Extract faculty information
print("Extracting faculty information...")
data['Faculty'] = data['Details'].apply(extract_faculty)

# Group data by year and faculty
print("Grouping data by year and faculty...")
grouped = data.groupby(['Publication Year', 'Faculty']).size().reset_index(name='Publication Count')

# Save results to a CSV file
print(f"Saving results to {output_csv}...")
grouped.to_csv(output_csv, index=False, encoding='utf-8-sig')

# Visualize the data
print("Creating visualization...")
plt.figure(figsize=(14, 8))
for faculty in grouped['Faculty'].unique():
    faculty_data = grouped[grouped['Faculty'] == faculty]
    plt.plot(faculty_data['Publication Year'], faculty_data['Publication Count'], label=faculty)

plt.xlabel('Year')
plt.ylabel('Publication Count')
plt.title('Yearly Publication Count by Faculty')
plt.legend(title="Faculty", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

print("Visualization completed.")
