import pandas as pd
import streamlit as st
from joblib import load

# Cargar el modelo
pipeline_cargado = load('modelo0.71.pkl')

# Función de predicción
def predict_sentiment(text, location, hashtag1, hashtag2, hashtag3, country):
    input_data = pd.DataFrame({
        'tokens_lematizados_sin_stopwords_str': [text],
        'ubicación': [location],
        'hashtag1': [hashtag1],
        'hashtag2': [hashtag2],
        'hashtag3': [hashtag3],
        'país_de_origen': [country]
    })
    prediction = pipeline_cargado.predict(input_data)[0]
    if prediction == 0:
        prediction = 'A favor de la guerra'
    elif prediction == 1:
        prediction = 'Postura Neutral'
    else:
        prediction = 'En contra de guerra'
    return prediction

# Título y descripción de la aplicación
st.title("Análisis de Sentimientos")
st.write("Introduce el texto y otras variables para predecir el sentimiento.")

# Crear los campos de entrada
text = st.text_area("Texto")
location = st.text_input("Ubicación")
hashtag1 = st.text_input("Hashtag 1")
hashtag2 = st.text_input("Hashtag 2")
hashtag3 = st.text_input("Hashtag 3")
country = st.text_input("País de origen")

# Botón para realizar la predicción
if st.button("Predecir Sentimiento"):
    if text and location and hashtag1 and hashtag2 and hashtag3 and country:
        try:
            # Realizar la predicción
            sentiment = predict_sentiment(text, location, hashtag1, hashtag2, hashtag3, country)
            st.write(f"Sentimiento: {sentiment}")
        except Exception as e:
            st.error(f"Ocurrió un error al realizar la predicción: {e}")
    else:
        st.error("Por favor, completa todos los campos.")
