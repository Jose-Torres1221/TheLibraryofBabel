'''
This program is for the CasaInternational "Library of Babel" Project.
Running this program will perform the following:
    Load in CSV and excel files provided with the repository
    Combine the dataframes into CombinedDF
    Pre-Process the data in CombinedDF
    Save the final Dataframe
'''
# load in dataframes

# importing libraries
import pandas as pd

# read in
jose_df = pd.read_csv('jose_English.csv')
rio_df = pd.read_csv('ryotaro_English.csv')
rio_df = rio_df.drop('Unnamed: 0', axis = 1)    
jose_df = jose_df.drop('Unnamed: 0', axis = 1)
# checking dataframes
rio_df.head()

# checking dataframes
jose_df.head()

# combine dataframes

combined_df = pd.concat([jose_df,rio_df], ignore_index = True)

# preprocess data

# importing libraries
import re

# function to remove escape sequences
def removeEscapeSequences(text):
  # use regex to find escape sequences (e.g., \n, \t, \u)
  return re.sub(r'\\.', '', repr(text)) # using repr to access the escape sequences

# create the function
def preprocessColumns(df):
  """
  Convert all string columns in a dataframe to lowercase.

  input:
  dataframe

  returns:
  dataframe with lowercase columns
  """

  # iterating through columns
  for col in df.columns:
    df[col] = df[col].str.lower() # lowercase
    df[col] = df[col].apply(removeEscapeSequences) # removing escape sequances
  return df

# running function on data
combined_df = preprocessColumns(combined_df)

combined_df.to_csv('CombinedDF.csv', index = False)