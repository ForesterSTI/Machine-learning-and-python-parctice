#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
#load raw data
raw = pd.read_csv("Day 3 work on assignment/Data/raw_data.csv")
meta = pd.read_csv("Day 3 work on assignment/Data/metadata.csv")
#isolate Coapplicant income table and Loan_Status
Appincome = raw[['CoapplicantIncome','Loan_Status']]
incom_positive = Appincome["CoapplicantIncome"]>0
print(Appincome[incom_positive])

Appincome = raw[['CoapplicantIncome','Loan_Status']]
incom_zero = Appincome["CoapplicantIncome"]==0
yes = Appincome[incom_positive]
no = Appincome[incom_zero]
#count values and calulate totals 
yes_total = yes['Loan_Status'].value_counts()
No_total= no['Loan_Status'].value_counts()
All_CoappIcY = yes_total['Y'] + yes_total['N']
All_CoappIcN = No_total['Y'] + No_total['N']
#calculating peercentages for approved loan applicatins for applicans with and without CoapplicantIncome
approved_with_CoAppInc = (yes_total['Y']/All_CoappIcY)*100
approved_without_CoAppInc = (No_total['Y']/All_CoappIcN)*100
#Create Pie charts and plot data
pl.figure(figsize=(3,3))
pl.pie(yes_total, labels= yes_total, colors=('#3361FF',"#FF33C4"))
pl.title("loan Approvals of Applicants living in an urban area")
pl.legend(labels=[f"\t\ napplicants approved with Co-applicant income: {yes_total['Y']}\n\
                applicants Declined with Co-applicant income: {yes_total['N']}\n\
                Total data entries: {All_CoappIcY}\n\
                Percatage of approved loans with Co-applicabt income: {approved_with_CoAppInc:.2f}%"
                
                ]
                    , loc='best', facecolor=None
                    )
pl.figure(figsize=(3,3))
pl.pie(No_total, labels= No_total, colors=('g',"r"))
pl.title("loan Approvals of Applicants living in an urban area")
pl.legend(labels=[f"\t\
                applicants approved without Co-applicant income: {No_total['Y']}\n\
                applicants Declined without Co-applicant income: {No_total['N']}\n\
                Total data entries: {All_CoappIcN}\n\
                Percatage of approved loans without Co-applicabt income: {approved_without_CoAppInc:.2f}%"
                   
                   ]           
                    , loc='best', facecolor=None
                    )
pl.show()