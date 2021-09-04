import pandas as pd 
import numpy as np
import streamlit as st

from pandas.io import gbq

# @st.cache
# def load_image(image_file):
# 	img = Image.open(image_file)
# 	return img 



def main():
    st.title("File Upload Tutorial")

	menu = ["Dataset","DocumentFiles","About"]
	choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Dataset":
		st.subheader("Dataset")
		data_file = st.file_uploader("Upload Data",type=['csv','xlsx'])
		if st.button("Process"):
			if data_file is not None:
				file_details = {"Filename":data_file.name,"FileType":data_file.type,"FileSize":data_file.size}
				st.write(file_details)

				df = pd.read_excel(data_file,sheet_name='DL CT')
				st.dataframe(df)
                order = df[["Mã ĐH","Trạng thái xuất kho","Trạng thái thanh toán","Trạng thái đơn hàng"]]
                # order.head()
                order.rename(columns={'Mã ĐH':'SalesOrderID','Trạng thái xuất kho':'StorageStatus','Trạng thái thanh toán':'PaymentStatus','Trạng thái đơn hàng':'OrderStatus'},inplace=True)
                st.dataframe(order)
# Read excel file

# table1 = pd.read_excel(r'C:\Users\ROT2HC\Documents\GitHub\streamlit_testing\HPDataReportDataCracy(1).xlsx',sheet_name='DL CT')
# table1.head()

# order = table1[["Mã ĐH","Trạng thái xuất kho","Trạng thái thanh toán","Trạng thái đơn hàng"]]
# order.head()

# order.rename(columns={'Mã ĐH':'SalesOrderID','Trạng thái xuất kho':'StorageStatus','Trạng thái thanh toán':'PaymentStatus','Trạng thái đơn hàng':'OrderStatus'},inplace=True)
# order.head()

