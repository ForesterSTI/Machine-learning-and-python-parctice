# importing libraries 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plot

#importing data 
raw_data = pd.read_csv("Day 3 work on assignment/Data/raw_data.csv")
#print(raw_data)
meta_data = pd.read_csv("Day 3 work on assignment/Data/metadata.csv")
#print(meta_data.head)

Urban_Area_only = raw_data['Property_Area'] == "Urban"
Rural_Area_only = raw_data['Property_Area'] == "Rural"
Semiurban_Area_only = raw_data['Property_Area'] == "Semiurban"
Urban = raw_data[Urban_Area_only] 
Rural= raw_data[Rural_Area_only] 
Semiurban = raw_data[Semiurban_Area_only] 
#print(Urban)

#isolate and count data in Property area column
Property_area_totU = Urban['Loan_Status'].value_counts()
Property_area_totR= Rural['Loan_Status'].value_counts()
Property_area_totSU = Semiurban['Loan_Status'].value_counts()
Missing_values_in_Property_area = meta_data.loc[meta_data['Column Name'] == 'Property_Area','missing Values'].values[0]
#Calculate totals 
Urban_Totals = Property_area_totU['Y']+Property_area_totU['N']
Rural_Totals = Property_area_totR['Y']+Property_area_totR['N']
Semiurban_Totals = Property_area_totSU['Y']+Property_area_totSU['N']
#Calculate percentages
Urban_Percentage = (Property_area_totU['Y']/Urban_Totals)*100
Rural_Percentage = (Property_area_totR['Y']/Rural_Totals)*100
Semiurban_Percentage = (Property_area_totSU['Y']/Semiurban_Totals)*100
#Creating and plotting pie chart
plot.figure(0,figsize=(4,4))
plot.pie(Property_area_totU, labels= Property_area_totU, colors=('r',"g"))
plot.title("loan Approvals of Applicants living in an urban area")
plot.legend(labels=[f"Total number of approvals: {Property_area_totU['Y']}\n\
                   Total number of declines: {Property_area_totU['N']}\n\
                   Overall Total: {Urban_Totals}\n\
                    Percentage of approvals: {Urban_Percentage:.2f}"
                   
                ]
                    , loc='upper right', facecolor=None)
plot.figure(1,figsize=(4,4))
plot.pie(Property_area_totR, labels= Property_area_totR, colors=('b',"#ffcc00"))
plot.title("loan Approvals of Applicants living in an rural area")
plot.legend(labels=[f"Total number of approval: {Property_area_totR['Y']}\n\
                   Total number of declines: {Property_area_totR['N']}\n\
                    Overall Total: {Rural_Totals}\n\
                    Percentage of approvals: {Rural_Percentage:.2f}"
                   
                ]
                    , loc='upper right', facecolor=None)
plot.figure(2,figsize=(4,4))
plot.pie(Property_area_totSU, labels= Property_area_totSU, colors=('#5eb32e','#ddbad5'))
plot.title("loan Approvals of Applicants living in an semiurban area")
plot.legend(labels=[f"Total number of approvals: {Property_area_totSU['Y']}\n\
                    Total number of declines: {Property_area_totSU['N']}\n\
                    Overall Total: {Semiurban_Totals}\n\
                    Percentage of approvals: {Semiurban_Percentage:.2f} "
                   
                ]
                    , loc='upper right', facecolor=None)


plot.show()

