#install linraries 
#pandas for data manupulation
import pandas as pd
# from pandas_profiling import profilereport

#Data Visualisation 
import matplotlib as plt
import plotly.express as plx

#Date manipulatiion 
from datetime import datetime,date, timedelta

#Cluster algorythm 
from sklearn.cluster import KMeans

#for Cat feature 
from category_encoders import OneHotEncoder

#Handling mising valuse 
from sklearn.impute import SimpleImputer

#for scaling features,
from sklearn.preprocessing import StandardScaler

#Model Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.decomposition import PCA

#Evaluation metric
from sklearn.metrics import silhouette_score

#warnigs override
import warnings
warnings.simplefilter('ignore', category= warnings, lineno=0, append=False)

#import data 
row_df = pd.read_csv("./Data/marketing_campaign.csv")
print(row_df.head())

#unserstanf data
print(row_df.info())
# view null colums 
print(row_df.isnull().sum())

#fill data 
row_df.loc[
        row_df['Income'].isnull() == True,
        'Income'
    ] = row_df['Income'].mean()

#W/imputer 


#Check missing value 
print(row_df.isnull().sum())

print(row_df.Z_CostContact.unique())

#make DT_Customers into date 
pd.to_datetime(row_df['Dt_Customer'], format="%d-%m-%Y")

#Categorical features 

Cat_features = ['Education', 'Marital_Status']
for i  in Cat_features:
    print(f'Feature {i}: \n in {row_df[i].unique()}')

row_df.describe(include='number')
print(
row_df.assign(
    Dt_Customer = lambda x: pd.to_datetime(x['Dt_Customer'], format= "%d-%m-%Y"
    )).assign(
        Cust_Age = lambda x: (x['Dt_Customer'].min() - x['Dt_Customer'])/timedelta(days=1))
            )

print(row_df.loc[:, row_df.columns.str.contains('Mnt')] .agg(['sum'], axis=1 ))

def prepare_data(data):

    data = (
        data
        # Remove NA values
        .dropna()
        
        # Convert Dt_Customer datatype to Date
        .assign(
            Dt_Customer = lambda x: pd.to_datetime(x['Dt_Customer'], format="%d-%m-%Y")
            )
        
        # Feature: Customer Age - max customer date
        .assign(
            Cust_Age = lambda x: (x['Dt_Customer'].min() - x['Dt_Customer'])/timedelta(days=1)
            )
        
        # Spent = Sum(Mnt...)
        .assign(
            Spent = lambda x: x.loc[:,x.columns.str.contains('Mnt')].agg(
                ['sum'], #function to use
                axis=1 # tell pandas to aggregate each row
                )
            )
        
        # Remove unnecessary features
        .drop(
            columns = ['ID', 'Z_CostContact', 'Z_Revenue', 'Response', 'Dt_Customer']
            )
        )
    
    # Transform Cat features
    prepared_df = OneHotEncoder(use_cat_names=True).fit_transform(data)
    
    # Output: cleaned dataframe
    return prepared_df

X= prepare_data(row_df)
print(X.head())