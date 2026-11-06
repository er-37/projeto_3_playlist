import streamlit as st
import json

with open("playlist.json", "r", encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

st.sidebar.title("Exû Playlist")
st.sidebar.image("logo.png")

estilo = st.sidebar.selectbox("Escolha um estilo musical:", dados['estilos'].keys())
artista = st.sidebar.selectbox("Escolha um artista:", dados['estilos'][estilo]['Artistas'].keys())

st.title(artista)

video, sobre = st.tabs(["video", "Sobre"])

with video:
    st.video(dados['estilos'][estilo]['Artistas'][artista]['video'])

with sobre:
    nome_arquivo = dados['estilos'][estilo]['Artistas'][artista]['sobre']

    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()

    st.markdown(texto)
    

