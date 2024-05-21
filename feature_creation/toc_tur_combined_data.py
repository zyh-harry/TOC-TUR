import pandas as pd

#All the toc and tur files here
toc_files = [
    'toc_pnwa_concentration_features.csv',
    'toc_pnwa_load_features.csv',
    'toc_wmth_concentration_features.csv',
    'toc_wmth_load_features.csv'
]

tur_files = [
    'tur_pnwa_concentration_features.csv',
    'tur_pnwa_load_features.csv',
    'tur_wmth_concentration_features.csv',
    'tur_wmth_load_features.csv'
]

discharge_files = [
    'discharge_pnwa_features.csv',
    'discharge_wmth_features.csv'
]

#output_directory = "/mnt/data/"  # Update this to the desired output directory

#Read and combine CSV files, grouping by 'timestamp_ccentral', df short for dataframe
def read_and_merge_csv(files):
    merged_df = pd.read_csv(files[0])
    for file in files[1:]:
        df = pd.read_csv(file)
        merged_df = pd.merge(merged_df, df, on='timestamp_ccentral', how='outer')
    return merged_df

#Combine all toc files
toc_combined_df = read_and_merge_csv(toc_files)

#Combine all tur files
tur_combined_df = read_and_merge_csv(tur_files)

#Combine all dischargefiles
discharge_combined_df = read_and_merge_csv(discharge_files)

#Combine the discharge data with toc and tur combined data
toc_merged_df = pd.merge(toc_combined_df, discharge_combined_df, on="timestamp_ccentral", how="left")
tur_merged_df = pd.merge(tur_combined_df, discharge_combined_df, on="timestamp_ccentral", how="left")

# Save the results
toc_merged_df.to_csv('toc_combined_with_discharge.csv', index=False)
tur_merged_df.to_csv('tur_combined_with_discharge.csv', index=False)

