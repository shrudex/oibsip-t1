import streamlit as st
import pickle 

encoder = pickle.load(open("encoder.pkl", 'rb'))
model = pickle.load(open("model.pkl", 'rb'))
scaler = pickle.load(open("scaler.pkl", 'rb'))