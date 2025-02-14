import pandas as pd
import matplotlib.pyplot as plt

# Define the path to the merged_data file
merged_data_file_path = r"merged_data.xlsx"

# Function to process and visualize the Language column
def plot_language_distribution_bar(file_path):
    try:
        # Load the Excel file
        print("Loading the merged_data file...")
        data = pd.read_excel(file_path, usecols=["Language"], engine="openpyxl")

        # Drop NaN values and count occurrences of each language
        language_counts = data["Language"].dropna().value_counts()

        # Plot a bar chart
        print("Plotting the language distribution bar chart...")
        plt.figure(figsize=(10, 6))
        plt.bar(language_counts.index, language_counts.values, color='skyblue')
        plt.xlabel("Language")
        plt.ylabel("Number of Articles")
        plt.title("Language Distribution in merged_data")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()  # Adjust layout to prevent label clipping
        plt.show()

    except Exception as e:
        print(f"Error processing file: {e}")

# Call the function
plot_language_distribution_bar(merged_data_file_path)
