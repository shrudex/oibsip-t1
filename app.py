import streamlit as st
import pickle 
import pandas as pd

#reading the encoder, model and scaler object files
encoder = pickle.load(open("encoder.pkl", 'rb'))
model = pickle.load(open("model.pkl", 'rb'))
scaler = pickle.load(open("scaler.pkl", 'rb'))

#setting the title and text
st.title("🌼Iris Flower Classification")
st.write("*Made with ❤️‍🔥 by Shrudex👨🏻‍💻*")

#taking the input from user
newSL = st.number_input("Enter sepal length (cm):", min_value=0.0)
newSW = st.number_input("Enter sepal width (cm):", min_value=0.0)
newPL = st.number_input("Enter petal length (cm):", min_value=0.0)
newPW = st.number_input("Enter petal width (cm):", min_value=0.0)

#button to trigger the classification
if st.button("Classify"):
    newValue = pd.DataFrame([[newSL, newSW, newPL, newPW]])
    newValue = scaler.transform(newValue)
    prediction = model.predict(newValue)
    finalAns = encoder.inverse_transform(prediction)
    st.markdown(f"Prediction result: **{finalAns[0]}**")


