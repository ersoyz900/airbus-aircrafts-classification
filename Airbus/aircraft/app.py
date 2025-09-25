import streamlit as st
import pandas as pd
import numpy as np
import PIL.Image
import PIL.ImageDraw
import os
import joblib

# Sayfa yapılandırması
st.set_page_config(page_title="Airbus Uçak Uygulamaları", page_icon="✈️", layout="wide")

# Sol menü ile uygulama seçimi
app_mode = st.sidebar.selectbox("Uygulama Seç", ["✈️ Görselleştirici", "🧮 Fiyat Tahmini"])

# -------------------------------
# Airbus Görselleştirici
# -------------------------------
def aircraft_visualizer():
    st.markdown('<h1 style="text-align:center;">✈️ Airbus Aircraft Dataset Viewer</h1>', unsafe_allow_html=True)
    st.markdown("Random aircraft image with bounding boxes and stats.")

    # Burada df ve img_folder yolunu kendi projene göre ayarla
    # Örnek:
    # df = pd.read_csv("aircraft_annotations.csv")
    # img_folder = "./images"

    # Şimdilik örnek dummy veri ile
    # Eğer df veya img yoksa hata verir, kendi verine göre düzenle
    try:
        image_ids = df['image_id'].unique()
    except Exception:
        st.error("DataFrame veya image folder yüklenemedi. Lütfen kendi verini tanımla.")
        return

    selected_image_id = st.selectbox("Select Image", image_ids)

    img_path = os.path.join(img_folder, selected_image_id)

    if os.path.exists(img_path):
        img = PIL.Image.open(img_path).convert("RGB")
        draw = PIL.ImageDraw.Draw(img)

        anns = df[df['image_id'] == selected_image_id]

        for _, row in anns.iterrows():
            polygon = row['geometry']
            polygon_tuples = [tuple(p) for p in polygon]
            draw.polygon(polygon_tuples, outline="red", width=2)
            draw.text(polygon_tuples[0], row['class'], fill="red")

        st.image(img, caption=f"Image ID: {selected_image_id}", use_column_width=True)

        with st.sidebar:
            st.header("Image Info")
            st.write(f"**Aircraft count:** {len(anns)}")
            avg_width = anns['width'].mean()
            avg_height = anns['height'].mean()
            st.write(f"**Average Width:** {avg_width:.1f} px")
            st.write(f"**Average Height:** {avg_height:.1f} px")
            st.markdown("---")
            st.markdown("### About")
            st.markdown("This app visualizes bounding boxes of aircraft in selected images from the Airbus dataset.")
    else:
        st.error("Selected image file not found. Please check your image folder path and file names.")

# -------------------------------
# Airbus Fiyat Tahmini
# -------------------------------
def aircraft_price_predictor():
    st.title("✈️ Airbus Uçak Fiyat Tahmini")
    st.markdown("Uçak özelliklerini girerek tahmini fiyatı öğrenin.")

    # Model yükle
    try:
        model = joblib.load('airbus_model.pkl')
    except Exception:
        st.error("Model dosyası yüklenemedi. Lütfen model dosyasını kontrol edin.")
        return

    st.header("📋 Uçak Özelliklerini Girin")

    col1, col2 = st.columns(2)
    with col1:
        model_type = st.selectbox("Model Tipi", ["A320", "A330", "A350", "A380"])
        year = st.number_input("Üretim Yılı", min_value=1990, max_value=2025, value=2015, step=1)

    with col2:
        capacity = st.number_input("Yolcu Kapasitesi", min_value=50, max_value=900, value=200, step=10)
        engines = st.selectbox("Motor Sayısı", [2, 4])

    model_map = {"A320": 0, "A330": 1, "A350": 2, "A380": 3}
    model_type_encoded = model_map.get(model_type, -1)

    input_features = np.array([model_type_encoded, year, capacity, engines]).reshape(1, -1)

    if st.button("🧮 Fiyatı Tahmin Et"):
        try:
            prediction = model.predict(input_features)
            st.success(f"Tahmini Fiyat: ${prediction[0]:,.2f}")
        except Exception as e:
            st.error(f"Tahmin sırasında hata oluştu: {e}")

    st.sidebar.title("ℹ️ Bilgilendirme")
    st.sidebar.info("""
    Bu uygulama Airbus uçaklarının temel teknik özelliklerine göre
    yaklaşık fiyat tahmini yapar.

    Model şu faktörleri dikkate alır:
    - Uçak modeli (A320, A330, A350, A380)
    - Üretim yılı
    - Yolcu kapasitesi
    - Motor sayısı
    """)

# -------------------------------
# Ana uygulama akışı
# -------------------------------
if app_mode == "✈️ Görselleştirici":
    aircraft_visualizer()
elif app_mode == "🧮 Fiyat Tahmini":
    aircraft_price_predictor()

