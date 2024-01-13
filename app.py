import streamlit as st
import plotly.express as pt
import seaborn as sns 
import altair as alt
import pandas as pd

path = 'https://raw.githubusercontent.com/timofey2001/TripleTen-SDT-project/main/vehicles_us.csv'
cars = pd.read_csv(path)

st.header('Analysis of Vehicle Sales Data')

st.markdown('In this notebook we will perform a basic analysis of vehicle sales data. The dataset contains records of cars sold, with various attributes such as price, model year, condition, and more. Our goal is to uncover insights into the factors that influence car prices using pandas, altair, streamlit, pyplot, and seaborn to visualize the distribution of key variables to identify patterns and outliers.')

cars['is_4wd'].fillna(0, inplace=True)
cars['is_4wd'] = cars['is_4wd'].astype(bool)

cars['paint_color'].fillna('Unknown', inplace=True)

average_cylinders = cars.groupby(['model_year', 'model'])['cylinders'].transform('mean')
cars['cylinders'].fillna(average_cylinders, inplace=True)

fig = pt.histogram(cars, x="price", title="Vehicle Price Distribution", labels={'price':'Vehicle Price', 'count':'Cars'}, nbins=200, range_x=[0,60000])
fig.update_layout(yaxis_title="Number of Cars")
st.plotly_chart(fig)

car_models = cars["model"].unique().tolist()
selected_car_model = st.selectbox("Choose a car model:", car_models)
filtered_df = cars[cars["model"] == selected_car_model]

fig1 = pt.histogram(filtered_df, x="price", nbins=30, title=f"Price Distribution for {selected_car_model}")
fig1.update_xaxes(title_text='Car price ($)')
fig1.update_yaxes(title_text='Number of cars')
st.plotly_chart(fig1)

if st.checkbox('Show Vehicles priced above $50,000'):
    filtered_cars = cars[(cars['price'] > 50000) & (cars['price'] < 400000)]
    filtered_cars = filtered_cars[filtered_cars['transmission'] == 'automatic']
    fig2 = pt.scatter(filtered_cars, x='days_listed', y='price', title='Price vs Days Listed', color='type')
else:
    fig2 = pt.scatter(cars, x='odometer', y='price', title='Price vs Odometer', color='type')
    fig2.update_xaxes(title_text='Odometer (Mileage)')
    fig2.update_yaxes(title_text='Price')

st.plotly_chart(fig2)

st.markdown("Using the data in this chart we can see that the majority of vehicles sell for less than 20 thousand dollars.")

st.title('Conclusion')
st.markdown("Our examination of the vehicle sales data yielded profound insights into the used car market's dynamics, highlighting the role of multiple factors in shaping car prices. We discovered a significant impact of a car's condition on its market value, with well-maintained cars fetching higher prices. This is especially true for newer vehicles, which tend to be pricier, and for 'salvage' vehicles, which are often more affordable. A notable observation was the preponderance of outliers, mainly cars in 'good' or 'like new' condition. This suggests a higher incidence of rare or high-end brands within these categories. Moreover, there was a distinct connection between a car's mileage and its selling price. Cars with lower mileage typically command higher prices, underscoring the importance of mileage in determining a car's worth. These insights are extremely valuable for participants in the car industry, aiding in strategic planning and enabling buyers to make more educated decisions. Nonetheless, there is still room for further investigation. Future research could include forecasting car prices and examining specific car segments in greater detail, potentially offering a more intricate understanding of the used car market.")
    
