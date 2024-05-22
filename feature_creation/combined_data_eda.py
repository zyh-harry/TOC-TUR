import pandas as pd

#Combined data files
toc_file = "TOC_combined_with_discharge.csv"
tur_file = "TUR_combined_with_discharge.csv"

#Reading data
toc_df = pd.read_csv(toc_file)
tur_df = pd.read_csv(tur_file)

#EDA Function
def perform_eda(df):
    eda_results = {}
    
    #Statistics
    numeric_df = df.select_dtypes(include=['number'])
    eda_results['summary_statistics'] = numeric_df.describe().transpose()
    
    #Any null values
    missing_values = df.isnull().sum().to_frame(name='missing_values')

    #Calculates the % of missing values for each column, len(df) is the number of rows of the dataframe
    missing_values['missing_percentage'] = (missing_values['missing_values'] / len(df)) * 100  
    
    eda_results['missing_values'] = missing_values
    
    #Data correlation (matrix)
    eda_results['correlation_matrix'] = numeric_df.corr()
    
    return eda_results

#EDA on TOC
toc_eda = perform_eda(toc_df)

#EDA on TUR
tur_eda = perform_eda(tur_df)

#EDA results
toc_eda['summary_statistics'].to_csv("TOC_summary_statistics.csv")
toc_eda['missing_values'].to_csv("TOC_missing_values.csv")
toc_eda['correlation_matrix'].to_csv("TOC_correlation_matrix.csv")

tur_eda['summary_statistics'].to_csv("TUR_summary_statistics.csv")
tur_eda['missing_values'].to_csv("TUR_missing_values.csv")
tur_eda['correlation_matrix'].to_csv("TUR_correlation_matrix.csv")

#EDA results in one CSV
toc_eda_combined = pd.concat([toc_eda['summary_statistics'], toc_eda['missing_values'], toc_eda['correlation_matrix']], axis=1)
toc_eda_combined.to_csv("TOC_eda.csv")

tur_eda_combined = pd.concat([tur_eda['summary_statistics'], tur_eda['missing_values'], tur_eda['correlation_matrix']], axis=1)
tur_eda_combined.to_csv("TUR_eda.csv")

