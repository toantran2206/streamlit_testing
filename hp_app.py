import pandas as pd 
import numpy as np
import streamlit as st

from pandas.io import gbq


#Read excel file
table1 = pd.read_excel('C:\Users\ROT2HC\Documents\GitHub\streamlit_testing\HPDataReportDataCracy(1).xlsx',sheet_name='DL CT')
table1.head()

order = table1[["Mã ĐH","Trạng thái xuất kho","Trạng thái thanh toán","Trạng thái đơn hàng"]]
order.head()

order.rename(columns={'Mã ĐH':'SalesOrderID','Trạng thái xuất kho':'StorageStatus','Trạng thái thanh toán':'PaymentStatus','Trạng thái đơn hàng':'OrderStatus'},inplace=True)
order.head()

