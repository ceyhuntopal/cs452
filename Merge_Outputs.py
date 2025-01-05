import pandas as pd
import os
import time

# Define the input and output paths
output_dir_path = r"Academics_Data\output_files"
final_output_path = r"Academics_Data\merged_results.csv"

def merge_output_files():
    """ Merge all individual output CSV files into one combined file """
    start_time = time.time()
    
    # List all CSV files in the output directory
    output_files = [f for f in os.listdir(output_dir_path) if f.startswith('matched_') and f.endswith('.csv')]
    
    if not output_files:
        print("No output files found to merge!")
        return

    print(f"Found {len(output_files)} files to merge.\n")

    # Initialize an empty list to hold DataFrames
    dataframes = []

    # Load and append each file
    for idx, file_name in enumerate(output_files, start=1):
        file_path = os.path.join(output_dir_path, file_name)
        print(f"Reading file {idx}/{len(output_files)}: {file_name}")
        
        try:
            df = pd.read_csv(file_path, encoding='utf-8-sig', low_memory=False)
            dataframes.append(df)
        except Exception as e:
            print(f"Error reading file {file_name}: {e}")
    
    # Concatenate all DataFrames into a single DataFrame
    print("\nMerging files...")
    combined_df = pd.concat(dataframes, ignore_index=True)

    # Save the merged DataFrame to a final CSV file
    combined_df.to_csv(final_output_path, index=False, encoding='utf-8-sig')
    end_time = time.time()

    print("\nMerging complete!")
    print(f"Combined file saved to: {final_output_path}")
    print(f"Total rows in merged file: {len(combined_df)}")
    print(f"Total execution time: {((end_time - start_time) / 60):.2f} minutes.")

if __name__ == "__main__":
    merge_output_files()
