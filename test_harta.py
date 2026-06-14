import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_geolocation import streamlit_geolocation

st.title("GPS-ul Meu în Timp Real")

# Funcția care cere locația browserului
location = streamlit_geolocation()

if location and location['latitude'] is not None:
    lat = location['latitude']
    lon = location['longitude']
    
    st.write(f"Coordonatele tale sunt: {lat}, {lon}")
    
    # Generăm harta centrată pe locația detectată
    m = folium.Map(location=[lat, lon], zoom_start=16)
    folium.Marker([lat, lon], popup="Aici ești tu!", icon=folium.Icon(color="red")).add_to(m)
    st_folium(m, width=700, height=500)
else:
    st.warning("Te rog să apeși pe butonul de 'Permite locația' din browser pentru a vedea harta.")