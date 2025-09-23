import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Sayfa yapılandırması
st.set_page_config(page_title="Airbus Uçak Fiyat Tahmini", page_icon="✈️", layout="wide")

# Modeli yükle
model = joblib.load('airbus_model.pkl')

# Başlık ve açıklama
st.title("Airbus Uçak Fiyat Tahmini")
st.write("Uçak özelliklerini girerek tahmini fiyatı öğrenin.")

# Kullanıcıdan girişler
model_type = st.selectbox("Model Tipi", ["A320", "A330", "A350", "A380"]) 
year = st.number_input("Üretim Yılı", min_value=2000, max_value=2025, value=2020)
capacity = st.number_input("Kapasite", min_value=50, max_value=850, value=200)
engines = st.number_input("Motor Sayısı", min_value=1, max_value=4, value=2)

# Özellikleri birleştir
input_data = np.array([model_type, year, capacity, engines]).reshape(1, -1)

# Tahmin yap
if st.button("Fiyatı Tahmin Et"):
    prediction = model.predict(input_data)
    st.write(f"Tahmini Fiyat: ${prediction[0]:,.2f}")
 
