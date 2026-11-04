import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('Data.csv')

#Cleaning

df['City'] = df['City'].str.strip()
df['City'] = df['City'].str.title()
df.columns = df.columns.str.strip()
print(df)

#Drop-down menu

select_city= st.selectbox("Pleas Select the city:" , df['City'].unique())

#Amounts Filter

max_amount = df['Sales_Amount'].max()
min_amount = df['Sales_Amount'].min()
filter_amount= st.slider("Select the maxmum number:" , min_amount , max_amount , max_amount )

#Hydrid filter

Final_filter= df[(df['City'] == select_city) & (df['Sales_Amount'] <=filter_amount)]

#Castomer Chart
#اینجا چون  در متغیر نمودار ستون شهر و قسمت رو داریم بهتره ستون دیگری رو برای رنگی رنگی بزاریم
plt.title("Chart")
fig , ax = plt.subplots(figsize = (10,7))
Chart = sns.scatterplot(x= 'order_id' , y= 'Sales_Amount' , hue='Order_Date', ax=ax , data= Final_filter)
st.pyplot(fig)

#Showing
st.subheader("All filter + Chart")
st.dataframe(Final_filter)
