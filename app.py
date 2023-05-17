import streamlit as st
import pandas as pd
from joao_paulo.vivareal import scrappingJoao
from joao_victor.imoveisvivarealjoaovictor import getDataframe
from jeferson.perez import scrape_website

st.title("Web Scraper de Imóveis")

# Cria um botão para executar a função scrape
if st.button("Executar Web Scraper Joao Paulo"):
    df = scrappingJoao()  # Chama a função scrape() do arquivo joao_paulo.py
    st.dataframe(df)  # Exibe o DataFrame resultante na interface do Streamlit
    st.download_button("Download CSV", data=df.to_csv().encode('utf-8'), file_name='imoveis.csv', mime='text/csv')
    
if st.button("Executar Web Scraper Joao Victor"):
    df_jv = getDataframe()  
    st.dataframe(df_jv)  # Exibe o DataFrame resultante na interface do Streamlit
    st.download_button("Download CSV", data=df_jv.to_csv().encode('utf-8'), file_name='df_jv', mime='text/csv')


if st.button("Executar Web Scraper Jeferson"):
    df_jef = scrape_website()
    st.dataframe(df_jef)  # Exibe o DataFrame resultante na interface do Streamlit
    st.download_button("Download CSV", data=df_jef.to_csv().encode('utf-8'), file_name='df_jef', mime='text/csv')

if st.button("Executar todas as funções de Web Scraper"):
    # Chama as três funções e armazena os resultados em variáveis diferentes
    df1 = scrappingJoao()
    df2 = getDataframe()
    df3 = scrape_website()

    # Juntar os três DataFrames em um único DataFrame final
    df_final = pd.concat([df1, df2, df3])

    # Exibe o DataFrame final na interface do Streamlit
    st.dataframe(df_final)

    # Adicione um botão para baixar o DataFrame final em formato CSV
    st.download_button(
        label="Download CSV",
        data=df_final.to_csv().encode("utf-8"),
        file_name="imoveis.csv",
        mime="text/csv",
    )