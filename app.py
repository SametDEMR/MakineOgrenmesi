import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Başlık
st.title("Cam Fiyat Tahmin Uygulaması")

# Eğitimli modeli yükleme
model_filename = 'eniyi_cam_model.joblib'
try:
    model = joblib.load(model_filename)
    st.success("Model başarıyla yüklendi.")
except FileNotFoundError:
    st.error(f"Model dosyası bulunamadı: {model_filename}")
    st.stop()

# Kullanıcı girdileri
st.sidebar.header("Cam Özelliklerini Girin")

def user_input_features():
    cam_markasi = st.sidebar.selectbox("Cam Markası", ['Marka A', 'Marka B', 'Marka C'])
    inceltilme_miktari = st.sidebar.slider("İnceltilme Miktarı (mm)", 1.0, 5.0, 2.5)
    ek_ozellikler = st.sidebar.selectbox("Ek Özellikler", ['Yok', 'UV Filtre', 'Anti-Refle'])
    cam_kasko_suresi = st.sidebar.slider("Cam Kasko Süresi (yıl)", 1, 5, 2)
    cerceve_markasi = st.sidebar.selectbox("Çerçeve Markası", ['Marka X', 'Marka Y', 'Marka Z'])
    cerceve_tipi = st.sidebar.selectbox("Çerçeve Tipi", ['Metal', 'Plastik', 'Titanyum'])
    
    data = {
        'Cam Markası': cam_markasi,
        'İnceltilme Miktarı (mm)': inceltilme_miktari,
        'Ek Özellikler': ek_ozellikler,
        'Cam Kasko Süresi (yıl)': cam_kasko_suresi,
        'Çerçeve Markası': cerceve_markasi,
        'Çerçeve Tipi': cerceve_tipi
    }
    return pd.DataFrame([data])

input_df = user_input_features()

# Kullanıcı girdilerini gösterme
st.subheader("Girdi Özellikleri")
st.write(input_df)

# Tahmin yapma
if st.button("Tahmini Hesapla"):
    try:
        prediction = model.predict(input_df)
        st.success(f"Tahmini Fiyat: {prediction[0]:,.2f} TL")
    except Exception as e:
        st.error(f"Tahmin sırasında bir hata oluştu: {e}")