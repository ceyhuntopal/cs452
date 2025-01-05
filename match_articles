import pandas as pd
import os
from multiprocessing import Pool, cpu_count, current_process
import time

# Define file paths
academics_file_path = r"all_universities_academics_ascii.csv"
articles_dir_path = r"ArticleData"  # Directory containing article files
output_dir_path = r"output_files"
output_file_path = r"final_matched_articles.csv"

# Create the output directory if it doesn't exist
os.makedirs(output_dir_path, exist_ok=True)

# Global variable to hold academics_data
academics_data = None

def load_academics_data():
    """ Load and normalize academics data """
    print(f"Loading academics dataset on process {current_process().name}...")
    global academics_data
    academics_data = pd.read_csv(
        academics_file_path,
        low_memory=False,
        encoding="utf-8",
        keep_default_na=False
    )
    academics_data['Academic Name'] = academics_data['Academic Name'].str.lower().str.strip()
    academics_data['University Name'] = academics_data['University Name'].str.strip()
    academics_data.rename(columns={'Academic Name': 'Split Authors'}, inplace=True)
    academics_data.set_index('Split Authors', inplace=True)  # Set index for faster merging

def process_file(file_name):
    """ Process a single file to match articles with academics """
    global academics_data
    file_path = os.path.join(articles_dir_path, file_name)
    output_file = os.path.join(output_dir_path, f"matched_{file_name}.csv")
    file_start_time = time.time()
    print(f"Starting processing: {file_name}")

    try:
        # Determine engine based on file extension
        engine = "openpyxl" if file_name.endswith('.xlsx') else "xlrd"

        # Load articles data
        articles_data = pd.read_excel(
            file_path,
            usecols=[
                "Publication Type", "Authors", "Author Full Names", "Group Authors", "Article Title",
                "Source Title", "Book Series Title", "Language", "Document Type", "Conference Title",
                "Conference Date", "Conference Location", "Conference Sponsor", "Author Keywords",
                "Keywords Plus", "Addresses", "Affiliations", "Email Addresses", "Funding Name Preferred",
                "Cited Reference Count", "Times Cited, WoS Core", "Times Cited, All Databases", "Publisher",
                "Publisher City", "ISSN", "eISSN", "ISBN", "Publication Date", "Publication Year", "Volume",
                "Issue", "DOI", "Book DOI", "Number of Pages", "Research Areas"
            ],
            engine=engine
        )

        # Normalize and split author names
        articles_data['Author Full Names'] = articles_data['Author Full Names'].str.lower().str.strip()
        articles_data['Split Authors'] = articles_data['Author Full Names'].str.split(';')

        # Reformat author names (Doe, John -> John Doe)
        def reformat_name(name):
            if ',' in name:
                parts = name.split(',')
                return f"{parts[1].strip()} {parts[0].strip()}"
            return name.strip()

        articles_data['Split Authors'] = articles_data['Split Authors'].apply(
            lambda authors: [reformat_name(author) for author in authors] if authors else []
        )
        articles_data_exploded = articles_data.explode('Split Authors')
        articles_data_exploded['Split Authors'] = articles_data_exploded['Split Authors'].str.strip()

        # Perform matching using index join for faster performance
        matches = articles_data_exploded.join(academics_data, on='Split Authors', how='inner')

        # Select and rename columns
        matches.rename(columns={
            'Split Authors': 'Academic Name',
            'University Name': 'University',
        }, inplace=True)

        # Save results to a file
        matches.to_csv(output_file, index=False, encoding='utf-8-sig')
        file_end_time = time.time()
        print(f"Finished processing {file_name}: {len(matches)} matches found in {file_end_time - file_start_time:.2f} seconds.")
        return matches

    except Exception as e:
        print(f"Error processing {file_name}: {e}")
        return pd.DataFrame()  # Return empty DataFrame on failure

if __name__ == "__main__":
    start_time = time.time()

    # Get a list of all files in the directory (supporting both .xls and .xlsx)
    file_list = [f for f in os.listdir(articles_dir_path) if f.endswith(('.xls', '.xlsx'))]
    print(f"Found {len(file_list)} files to process.\n")

    # Initialize academics_data for each worker
    print(f"Using {cpu_count()} CPU cores for parallel processing...\n")
    with Pool(processes=cpu_count(), initializer=load_academics_data) as pool:
        # Collect all matches in a list of DataFrames
        results = pool.map(process_file, file_list)

    # Combine all matches into a single DataFrame
    all_matches = pd.concat(results, ignore_index=True)

    # Remove duplicate rows where both "Article Title" and "Academic Name" (Author Name) are the same
    print("Removing duplicate rows based on Article Title and Academic Name...")
    duplicate_mask = all_matches.duplicated(subset=['Article Title', 'Academic Name'], keep=False)
    all_matches = all_matches[~duplicate_mask]  # Keep only rows that are NOT duplicates

    # Save the consolidated results to a single CSV file
    all_matches.to_csv(output_file_path, index=False, encoding='utf-8-sig')
    end_time = time.time()

    print("\nSummary:")
    print(f"All files processed. Total unique matches found: {len(all_matches)}")
    print(f"Results saved to {output_file_path}")
    print(f"Total execution time: {((end_time - start_time) / 60):.2f} minutes.")
