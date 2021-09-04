import pandas as pd 
import numpy as np
import streamlit as st

from pandas.io import gbq


#Read excel file
table1 = pd.read_excel('C:\Users\ROT2HC\Documents\GitHub\streamlit_testing\[HP] 210808-DataCracyShareDataSM.xlsx',sheet_name='DL CT')
table1.head()

