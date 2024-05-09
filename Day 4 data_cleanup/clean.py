#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
from skimpy import clean_columns
import seaborn as sns

#load raw data
raw = pd.read_csv("Day 3 work on assignment/Data/raw_data.csv")
meta = pd.read_csv("Day 3 work on assignment/Data/metadata.csv")
#isolate Coapplicant income table and Loan_Status
Appincome = raw[['CoapplicantIncome']]
Out_lair= Appincome.describe(x*0.1 for x in range(614))
sns.boxenplot(x=Appincome)
