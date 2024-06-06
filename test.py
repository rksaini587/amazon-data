import streamlit as st
import pandas as pd

# Title of the Streamlit app
st.title('Amazon Analytics')

# Button to show data
show_button = st.button('Show data')

# Load the data from CSV
df = pd.read_csv('amazon business.csv')
df['year'] = pd.to_datetime(df['Order Date']).dt.year

# Display data if button is clicked
if show_button:
    st.dataframe(df)

# Function to calculate top N categories by profit
def top(category, n):
    df = pd.read_csv('amazon business.csv')
    result = df.groupby(category).agg(
        highest_profit=('Profit', 'sum')
    ).sort_values('highest_profit', ascending=False).head(n)
    return result

# Header for top N category profit section
st.header('Top N Category Profit')

# Input for category and top N
cat = st.text_input('Enter the category you want?')
topn = int(st.number_input('Top N', min_value=1, step=1))

# Button to calculate top N categories
calculate = st.button('Calculate')

# Calculate and display the bar chart if button is clicked
if calculate:
    if cat and topn > 0:
        var = top(cat, topn)
        st.dataframe(var)
        st.bar_chart(var['highest_profit'])
    else:
        st.write("Please enter a valid category and number.")

# Header for yearly profit section
st.header('Yearly profit')

# Function to calculate yearly profit
def yearly(year):
    df = pd.read_csv('amazon business.csv')
    df['year'] = pd.to_datetime(df['Order Date']).dt.year
    return df.loc[df['year'] == year]['Profit'].sum()

# Input for year
year = int(st.number_input('Enter Year', min_value=2000, step=1))

# Button to calculate yearly profit
calculate_yearly = st.button('Calculate yearly profit')

# Calculate and display the yearly profit if button is clicked
if calculate_yearly:
    profit = yearly(year)
    st.write(f"The total profit for the year {year} is {profit}")
