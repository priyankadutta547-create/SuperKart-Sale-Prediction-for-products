import streamlit as st
import pandas as pd
import joblib

# Load the trained regression model
def load_model():
    return joblib.load("SuparKart_sale_prediction_v1.0.joblib")

model2 = load_model()

# Streamlit UI for Boston Housing Price Prediction
st.title("Stores' total sales based on product ")
st.write("This app predicts the sales forecast predicting the future sales based on historical data.")
st.write("Move the sliders below to adjust values and get a prediction.")

# Collect user input using sliders
Product_Id = st.selectbox("Unique identifier of each product, each identifier having two letters at the beginning, followed by a number", 'FD6114', 'FD5484', 'NC1071', 'FD3342')
Product_Weight = st.slider("Weight of each product", 0.0, 100.0, 12.0, 1.0)
Product_Sugar_Content = st.selectbox("Sugar content of each product", 'Low Sugar', 'No Sugar', 'Regular', 'Reg')
Product_Allocated_Area = st.slider("Ratio of the allocated display area of product", 0.0, 1.0, 0.55, 0.01)
Product_Type = st.selectbox("Broad category for product", 'Frozen Fruit', 'Canned', 'Health and Hygiene', 'Meat')
Product_MRP = st.slider("Maximum retail price of each product", 0.0, 100.0, 65.0, 1.0)
Store_Id = st.selectbox("Unique identifier of each store", 'OUT001', 'OUT002', 'OUT004', 'OUT005')
Store_Establishment_Year = st.slider("Year in which the store was established", 1987, 1999, 2000, 2008)
Store_Size = st.selectbox("Size of the store, depending on sq. feet", 'High', 'Medium', 'Low')
Store_Location_City_Type = st.selectbox("Type of city in which the store is located", 'Tier 1', 'Tier 2', 'Tier 3')
Store_Type = st.selectbox("Type of store depending on the products that are being sold there,", 'Departmental Store', 'Supermarket Type 1', 'Supermarket Type 2', 'Food Mart')

# Create input DataFrame
input_data = pd.DataFrame([{
    'Product_Id': Product_Id,
    'Product_Weight': Product_Weight,
    'Product_Sugar_Content': Product_Sugar_Content,
    'Product_Allocated_Area': Product_Allocated_Area,
    'Product_Type': Product_Type,
    'Product_MRP': Product_MRP,
    'Store_Id': Store_Id,
    'Store_Establishment_Year': Store_Establishment_Year,
    'Store_Size': Store_Size,
    'Store_Location_City_Type': Store_Location_City_Type,
    'Store_Type': Store_Type,
    'Product_Store_Sales_Total': Product_Store_Sales_Total
}])

# Predict button
if st.button("Predict MEDV"):
    predicted_Sale = model.predict(input_data)[0]
    st.success(f"💰 Estimated Median Value of Home (MEDV): ${predicted_Sale*1000:,.2f}")
