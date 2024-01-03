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

st.markdown("The vehicles csv contains basic info on over 50 thousand cars, including paint color, sell price, milage, model year, and make/model info. To help visualize the data, I have included a few charts for some of the quantitative columns.")

st.pyplot(fig)


plt.figure(figsize=(10, 5))
plt.hist(cars['price'], bins=40, color='skyblue', edgecolor='black')
plt.title('Vehicle Price Distribution')
plt.xlabel('Price')
plt.ylabel('Number of Vehicles')



st.pyplot(plt)

st.markdown("Using the data in this chart we can see that the majority of vehicles sell for less than 20 thousand dollars.")

if st.checkbox('Show Price Distribution by Vehicle Condition'):
    # Code to create the plot
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='condition', y='price', data=cars)
    plt.title('Price Distribution by Vehicle Condition')
    plt.xlabel('Condition')
    plt.ylabel('Price')
    plt.xticks(rotation=45)  # Optional: if the x labels overlap
    st.pyplot(plt)
    st.title('Conclusion')
    st.markdown('Based on the data analysis, The majority of cars sell for less than 50 thousnad dollars. The cars that less for more than 50k are usually in new condition, however cars that are in good condition contain a large number of outliers that sell for over 100k. This could be because they are either classics, or some kind of rare make/model. If someone wanted to sell a car and get the best price, they should ideally have a car in excellent or new condition with less than 50 thousand miles.')