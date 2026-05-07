import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header("Dashboard de Análise de Veículos Usados")
st.write(
    "Este aplicativo foi desenvolvido para explorar dados de anúncios de veículos usados "
    "por meio de visualizações interativas, permitindo identificar padrões, tendências e relações" 
     " entre variáveis como preço, ano do veículo e quilometragem."    
)

st.write(car_data.head())   

hist_button = st.button("📈 💰 Ver distribuição de preços")

if hist_button:
    st.write("📊 Analisando a distribuição dos preços dos veículos...")

    fig = px.histogram(car_data, x="price")

    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button('📈 Ver relação entre ano e preço')

if scatter_button:
    st.write('Analisando relação entre ano do veículo e preço.')

    fig = px.scatter(car_data, x="model_year", y="price")

    st.plotly_chart(fig, use_container_width=True)