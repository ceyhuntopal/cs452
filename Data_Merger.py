import os, sys
import pandas as pd

# Define paths & data type
data_folder = "data" # Enter data folder name
data_dir = os.path.join(os.getcwd(), data_folder)
data_type = ".xls"

# Define columns to drop from the data frame
columns_to_drop = ['Book Authors', 'Book Editors', 'Book Group Authors', 'Book Author Full Names', 'Book Series Subtitle', 'Conference Host', 
                   'Abstract', 'Reprint Addresses', 'Researcher Ids', 'ORCIDs', 'Funding Orgs', 'Funding Text', 'Cited References', 
                   '180 Day Usage Count', 'Since 2013 Usage Count', 'Publisher Address', 'Journal Abbreviation', 'Journal ISO Abbreviation',
                   'Supplement', 'Special Issue', 'Part Number', 'Meeting Abstract', 'Start Page', 'End Page', 'Article Number', 'DOI Link',
                   'Early Access Date', 'WoS Categories', 'Web of Science Index', 'IDS Number', 'Pubmed Id', 'Open Access Designations',
                   'Highly Cited Status', 'Hot Paper Status', 'Date of Export', 'UT (Unique WOS ID)', 'Web of Science Record']

# Convert excel data to pandas data frame
def convert(dir, type):
    df = []
    for file in os.listdir(dir):
        if file.endswith(type):
            df.append(pd.read_excel(os.path.join(dir, file)))
    return df

# Modify data frames
def modify(df, dcols, filler):
    tmp = df.drop(dcols, axis=1)
    tmp = tmp.fillna(filler)
    return tmp

dfs = convert(data_dir, data_type)
for i in range(0, len(dfs)):
    dfs[i] = modify(dfs[i], columns_to_drop, "-")

merged_df = pd.concat(dfs, axis=0, ignore_index=True)
merged_df.index += 1
merged_df.to_excel("merged_data.xlsx")
# merged_df.to_pickle("merged_data.pkl")
