import pandas as pd 
import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px
import datetime as dt
st.title('_SUPER MARKET SALE DASHBORD_')
st.markdown("""----""")

df=pd.read_csv('supermarket.csv')
df['Date']=pd.to_datetime(df['Date'],errors='coerce')
df['Month'] = df['Date'].dt.month_name()

st.write(df.head(3))


#---Total KPI---
total_sale=df['Total'].sum()
avg_rating=round(df['Rating'].mean(),1)
gross_incame=df['gross income'].sum()

col1, col2,col3=st.columns(3)
with col1:
    st.subheader('Total Sale:')
    st.subheader(f' US $ {total_sale:},')


with col2:
        st.subheader('AVR_RATING:')
        st.subheader(f'{avg_rating}')

with col3:
    st.subheader('Gross income:')
    st.subheader(f'US $ {gross_incame:},')    

#----sideheader----
st.sidebar.header('FILTER HERE')
city=st.sidebar.multiselect('Select the City',
options=df['City'].unique(),
default=df['City'].unique())

st.sidebar.header('FILTER HERE')
gender=st.sidebar.multiselect(' Select the Gender',
options=df['Gender'].unique(),
default=df['Gender'].unique())
st.sidebar.header('FILTER HERE')
month =st.sidebar.multiselect(' Select the Month',
options=df['Month'].unique(),
default=df['Month'].unique())

# ---- now join both unit----
df_selection = df.query(
    "City == @city  & Gender == @gender & Month == @month"
)

#---- Create barchat total sale with city---

st.title(' TOTAL SALE BAR CHART')
st.markdown("##")

st.markdown("---")
col4, col5,col6=st.columns(3)

with col4:
 city=pd.pivot_table(df_selection, index='City', values='Total', aggfunc='sum')
 st.write(city)
with col5:
 gender=pd.pivot_table(df_selection, index='Gender', values='Total', aggfunc='sum')
 st.write(gender)
with col6:
 month=pd.pivot_table(df_selection, index='Month', values='Total', aggfunc='sum')
 st.write(month)

product_sale=pd.pivot_table(df_selection, index='Product line', values='Total', aggfunc='sum').sort_values(by='Total')
    
fig = px.bar(product_sale, x='Total', y=product_sale.index)
st.plotly_chart(fig,use_container_width=True)

#---- pic chart---
st.title("Total Product Sales Pie Chart")
product_sale=pd.pivot_table(df_selection, index='Product line', values='Total', aggfunc='sum').reset_index()

fig1 = px.pie(product_sale, names= 'Product line', values='Total')
st.plotly_chart(fig1,use_container_width=True)

    





  

