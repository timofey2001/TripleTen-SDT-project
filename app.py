import streamlit as st
import matplotlib.pyplot as plt 
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

all_columns = [col for col in cars.columns if col not in ['date_posted', 'model']]
num_rows = (len(all_columns) + 1) // 2
plt.figure(figsize=(15, num_rows * 5))
for i, col in enumerate(all_columns, 1):
    ax = plt.subplot(num_rows, 2, i)
    if cars[col].dtype in ['int64', 'float64']:
        sns.histplot(cars[col].dropna(), kde=False, bins=30, ax=ax)
        ax.set_ylabel('Number of Vehicles')
    else:
        sns.countplot(x=col, data=cars, ax=ax)
    ax.set_title(f'Distribution of {col}')
    if col in cars.select_dtypes(include=['object', 'bool']).columns:
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        ax.set_ylabel('Number of Vehicles')
plt.tight_layout()

st.markdown("The vehicles csv contains basic info on over 50 thousand cars, including paint color, sell price, milage, model year, and make/model info. To help visualize the data, I have included a few charts for some of the quantitative columns.")



plt.figure(figsize=(10, 5))
plt.hist(cars['price'], bins=40, color='skyblue', edgecolor='black')
plt.title('Vehicle Price Distribution')
plt.xlabel('Price')
plt.ylabel('Number of Vehicles')
st.pyplot(plt)

car_models = cars["model"].unique().tolist()
selected_car_model = st.selectbox("Choose a car model:", car_models)
filtered_df = cars[cars["model"] == selected_car_model]
price_distribution = filtered_df["price"].value_counts()
plt.bar(price_distribution.index, price_distribution.values)
plt.xlabel("Car price ($)")
plt.ylabel("Number of cars")
plt.title("Price distribution for " + selected_car_model)
plt.show()
st.pyplot(plt)


st.markdown("Using the data in this chart we can see that the majority of vehicles sell for less than 20 thousand dollars.")

if st.checkbox('Show Price Distribution by Vehicle Condition'):
    plt.figure(figsize=(10, 6))
    ax = sns.boxplot(x='condition', y='price', data=cars)
    ax.set_title('Price Distribution by Vehicle Condition')
    ax.set_xlabel('Condition')
    ax.set_ylabel('Price')
    ax.set_ylim(0, 120000)
    st.pyplot(plt)
    st.title('Conclusion')
    st.markdown("Our examination of the vehicle sales data yielded profound insights into the used car market's dynamics, highlighting the role of multiple factors in shaping car prices. We discovered a significant impact of a car's condition on its market value, with well-maintained cars fetching higher prices. This is especially true for newer vehicles, which tend to be pricier, and for 'salvage' vehicles, which are often more affordable. A notable observation was the preponderance of outliers, mainly cars in 'good' or 'like new' condition. This suggests a higher incidence of rare or high-end brands within these categories. Moreover, there was a distinct connection between a car's mileage and its selling price. Cars with lower mileage typically command higher prices, underscoring the importance of mileage in determining a car's worth. These insights are extremely valuable for participants in the car industry, aiding in strategic planning and enabling buyers to make more educated decisions. Nonetheless, there is still room for further investigation. Future research could include forecasting car prices and examining specific car segments in greater detail, potentially offering a more intricate understanding of the used car market.")
