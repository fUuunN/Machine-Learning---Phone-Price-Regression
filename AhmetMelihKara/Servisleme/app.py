import streamlit as st
import joblib

# Eğitilmiş modelimi yükledim
model = joblib.load('best_model.sav')

st.title('Telefon Puanı - Model Tahmini Uygulaması')

# Kullanıcıdan giriş değerlerini aldım
Depolama = st.number_input('Depolama (1024 Gb - 8 Gb) ')
RAM = st.number_input('RAM (12 Gb - 1 Gb)')
EkranBoyutu = st.number_input('Ekran Boyutu (6.70 İnç - 5.0 İnç)')
BataryaKapasitesi = st.number_input('Batarya Kapasitesi (5000 mA - 2000 mA)')
KameraPixel = st.number_input('Kamera Pixeli (200 mp - 10 mp)')
EkranGovde = st.number_input('Ekran Gövde Oranı (Genllikle 80 - 89 arası)')
CPUFrekans = st.number_input('İşlemci Frekansı (2 Ghz - 3.5 Ghz)')
Genislik = st.number_input('Genislik Çözünürlüğü - Pixel Sayısı')
Uzunluk = st.number_input('Uzunluk Çözünürlüğü - Pixel Sayısı')
BesG = st.checkbox('5G')
SuyaDayanıklılık = st.checkbox('Suya Dayanıklılık')
HizliSarj = st.checkbox('Hızlı Şarj')

#Veri setimde 5G gibi özlellikleri olan telefonlar encode edilirken 0 değerini almış. Bende böyle bir çözüm buldum.
BesG = 1 if not BesG else 0
SuyaDayanıklılık = 1 if not SuyaDayanıklılık else 0
HizliSarj = 1 if not HizliSarj else 0

if st.button('Tahmin Yap'):
    user_input = [
        Depolama, RAM, EkranBoyutu, BataryaKapasitesi, KameraPixel, EkranGovde,
        CPUFrekans, Genislik, Uzunluk,
        BesG, SuyaDayanıklılık, HizliSarj,
    ]

    prediction = model.predict([user_input])

    st.write('Tahmin Sonucu:', prediction[0])
