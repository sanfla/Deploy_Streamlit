import streamlit as st

st.title("ChatBot")
st.write("Hello World")
st.text("Selamat datang di aplikasi ChatBot")

nama = st.text_input("Masukan Nama", key='input1') #key untuk ID unik 
nim = st.text_input("Masukan NIM", key='input2')

if nama:
    st.text("Nama: " + nama)
    if len(nim) != 10:
        st.text("Nim yang anda masukan salah banget")
    else:
        st.text("Nim: " + nim)

iniKotak = st.selectbox('Pilih Matkul', ['B Indo', 'Alpro', 'Strukdat'])
st.write("Matkul yang anda pilih adalah " + iniKotak)

Umur = st.slider("umur: ", 5, 60, 15) #diambil yang minimum dan maksimum, 15 untuk titik awal
st.write(Umur)

Gender = st.radio('Gender', ['Pria', 'Wanita'])
if Gender == "Pria":
    st.write("Selamat Datang Mas " + nama)
else:
    st.write("Selamat Datang Bu " + nama)

list_hobi = st.text_area("Hobi", 'Main bola, Main Game')
list_hobi = [x.strip() for x in list_hobi.split(',')]
st.write(list_hobi)

st.image('https://i.pinimg.com/736x/83/88/e8/8388e8555f54776a2e0ece3856e9270a.jpg', width = 90 ,caption="Meme")

st.markdown('[ini link ke google](https://www.google.com/)')

import pandas as pd
data = {'Pekerjaan':['Programmer', 'Dokter', 'Pengacara'],
        'Tier':["E", "SS", 'A']
        }

df = pd.DataFrame(data)
st.dataframe(df, use_container_width = True)

st.title("Buka Data")
file = st.file_uploader('Pilih file jpg', type=['jpg', 'csv', 'png'])
if file is not None:
    st.write(file.type)
    if file.type == "image/jpeg" or file.type == "image/png":
        st.image(file)
    else:
        data = pd.read_csv(file)

        st.dataframe(data)

st.title("Kalkulator")
angka1 = st.number_input("Masukan angka 1 ", value = 0)
angka2 = st.number_input("Masukan angka 2 ", value = 0)

operasi = st.radio('Pilih Operasi', ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"])

if st.button('Hitung'):
    if operasi == "Penjumlahan":
        hasil = angka1 + angka2
    elif operasi == "Pengurangan":
        hasil = angka1 - angka2
    elif operasi == "Perkalian":
        hasil = angka1 * angka2
    elif operasi == "Pembagian":
        hasil = angka1 / angka2

    st.success(f'Hasil {operasi} : {hasil}')

st.sidebar.header('Fitur Kiri')
if st.sidebar.checkbox('Biodata'):
    st.sidebar.write(f'Nama : {nama}')