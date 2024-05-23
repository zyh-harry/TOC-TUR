import pandas as pd

toc_file = "TOC_combined_with_discharge.csv"
tur_file = "TUR_combined_with_discharge.csv"

#Reading data
toc_df = pd.read_csv(toc_file)
tur_df = pd.read_csv(tur_file)

#EDA function
def perform_eda(df):
    eda_results = {}
    
    #Summary statistics
    numeric_df = df.select_dtypes(include=['number'])
    eda_results['summary_statistics'] = numeric_df.describe().transpose()
    
    #Any null values detected
    missing_values = df.isnull().sum().to_frame(name='missing_values')

    #% of null values for each column
    missing_values['missing_percentage'] = (missing_values['missing_values'] / len(df)) * 100
    eda_results['missing_values'] = missing_values
    
    #Correlation matrix
    eda_results['correlation_matrix'] = numeric_df.corr()
    
    return eda_results

#EDA on TOC
toc_eda = perform_eda(toc_df)

#EDA on TUR
tur_eda = perform_eda(tur_df)

#EDA results saved separately
toc_eda['summary_statistics'].to_csv('TOC_summary_statistics.csv')
toc_eda['missing_values'].to_csv('TOC_missing_values.csv')
toc_eda['correlation_matrix'].to_csv('TOC_correlation_matrix.csv')

tur_eda['summary_statistics'].to_csv('TUR_summary_statistics.csv')
tur_eda['missing_values'].to_csv('TUR_missing_values.csv')
tur_eda['correlation_matrix'].to_csv('TUR_correlation_matrix.csv')

#To separate sum stats, missing values and correlation matrix for better data visualization, blank columns are used
def create_blank_df(rows):
    return pd.DataFrame({'': [''] * rows})

#Combine all EDA results into one single dataframe with blank columns separating datasets in the final CSV
def combine_eda_results(eda_results):
    blank_df1 = create_blank_df(len(eda_results['summary_statistics']))
    blank_df2 = create_blank_df(len(eda_results['missing_values']))
    
    combined_df = pd.concat([eda_results['summary_statistics'], blank_df1, 
    eda_results['missing_values'], blank_df2, 
    eda_results['correlation_matrix']], axis=1)
    return combined_df

toc_eda_combined = combine_eda_results(toc_eda)
toc_eda_combined.to_csv('TOC_eda.csv', index=False)

tur_eda_combined = combine_eda_results(tur_eda)
tur_eda_combined.to_csv('TUR_eda.csv', index=False)


