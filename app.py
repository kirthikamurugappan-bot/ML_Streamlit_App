import streamlit as st
import joblib

model = joblib.load("iris_model.pkl")

st.title("Iris Flower Prediction")

sl = st.number_input("Sepal Length", value=5.1)
sw = st.number_input("Sepal Width", value=3.5)
pl = st.number_input("Petal Length", value=1.4)
pw = st.number_input("Petal Width", value=0.2)

if st.button("Predict"):
    prediction = model.predict_one([sl, sw, pl, pw])

    st.success(f"Predicted Flower: {prediction}")