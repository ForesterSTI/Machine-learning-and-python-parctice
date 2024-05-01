import pandas as pd
import numpy as np
#Import and read data from raw_data.csv
df_csv = pd.read_csv('./Day 2 Data preporation/Data/raw_data.csv')
#Create new data field with my xhosen columns and outcome
selectedColumns = df_csv[['CoapplicantIncome', 'Property_Area', 'Loan_Status']]
'''
Filter selecColumns datafield into seporate fields  reflecting the coutcome 
( field 1 for Loan approval = yes and field 2 for Load approval = No )
'''
filter_Yes=selectedColumns['Loan_Status'] =="Y"
yes_val = selectedColumns[filter_Yes]

filter_No=selectedColumns['Loan_Status'] =="N"
No_val = selectedColumns[filter_No]
#The next 2 blcos of code summerise the data from the 2 data fields 
urban_count= 0
rural_count= 0
semi_rural_count= 0

for x in yes_val['Property_Area']:
    if  x ==('Urban'):
        urban_count+=1
    elif x ==('Rural'):
        rural_count+=1
    elif x ==('Semiurban'):
        semi_rural_count+=1
total= urban_count+rural_count+semi_rural_count
print(f"Loan_Approval: YES \n\
        Urban total: {urban_count} \n\
        rural_count: {rural_count} \n\
        semi_rural_count: {semi_rural_count}\n\
        Total: {total}")


urban_count_N= 0
rural_count_N= 0
semi_rural_count_N= 0

for x in No_val['Property_Area']:
    if  x ==('Urban'):
        urban_count_N+=1
    elif x ==('Rural'):
        rural_count_N+=1
    elif x ==('Semiurban'):
        semi_rural_count_N+=1
total_N= urban_count_N+rural_count_N+semi_rural_count_N
print(f"Loan_Approval: NO\n\
        Urban total: {urban_count_N} \n\
        rural_count: {rural_count_N} \n\
        semi_rural_count: {semi_rural_count_N}\n\
        Total: {total_N}")