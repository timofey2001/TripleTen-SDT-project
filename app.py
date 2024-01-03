import streamlit as st
import matplotlib.pyplot as plt 
import seaborn as sns 
import altair as alt
import pandas as pd

path = 'https://raw.githubusercontent.com/timofey2001/TripleTen-SDT-project/main/vehicles_us.csv'
cars = pd.read_csv(path)

st.header('Data Analysis on Cars')

all_columns = [col for col in cars.columns if col not in ['date_posted', 'model']]

num_rows = (len(all_columns) + 1) // 2

fig, ax = plt.subplots(figsize=(15, num_rows * 5))
for i, col in enumerate(all_columns, 1):
    ax = plt.subplot(num_rows, 2, i)
    if cars[col].dtype in ['int64', 'float64']:
        sns.histplot(cars[col].dropna(), kde=False, bins=30, ax=ax)
    else:
        sns.countplot(y=col, data=cars, ax=ax)
    ax.set_title(f'Distribution of {col}')
plt.tight_layout()

st.pyplot(fig)