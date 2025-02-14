import pandas as pd

# File paths
input_file = r"final_matched_articles.csv"  # Input CSV file from the previous step
gender_file = r"all_universities_academics_with_gender.xlsx"  # Gender file
output_file = r"final_matched_articles_with_gender.csv"  # Output CSV file with gender column

def add_gender_column(input_file, gender_file, output_file):
    try:
        print("Loading matched articles data...")
        articles_data = pd.read_csv(input_file, encoding='utf-8', low_memory=False)

        print("Loading gender data...")
        gender_data = pd.read_excel(gender_file, engine="openpyxl", sheet_name=0)
        gender_data['Academic Name'] = gender_data['Academic Name'].str.lower().str.strip()
        gender_data['Gender'] = gender_data['Gender'].str.strip()

        print("Merging gender information into articles data...")
        # Normalize academic names in articles data for matching
        articles_data['Academic Name'] = articles_data['Academic Name'].str.lower().str.strip()

        # Merge gender data into articles data
        merged_data = pd.merge(
            articles_data,
            gender_data[['Academic Name', 'Gender']],
            on='Academic Name',
            how='left'  # Left join to keep all rows from articles_data
        )

        print(f"Saving the output file to: {output_file}")
        merged_data.to_csv(output_file, index=False, encoding='utf-8-sig')

        print("Output file saved successfully.")

    except Exception as e:
        print(f"Error: {e}")

# Run the function
add_gender_column(input_file, gender_file, output_file)
