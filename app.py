import streamlit as st 
import pandas as  pd
import plotly.express as px

def formatIndex(df):
    df['S/No.'] = range(1, len(df) + 1)
    df = df.set_index('S/No.')
    return df

df=pd.read_csv('superstore.csv',encoding='latin1')
st.write(df.head())
product_list=df['Product Name'].unique()
total_sales_product=df[['Product Name','Sales']].groupby('Product Name').agg({'Sales':'sum'}).reset_index().sort_values(by='Sales',ascending=False)
st.dataframe(total_sales_product.head(10))