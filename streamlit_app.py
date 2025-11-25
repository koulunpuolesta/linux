import streamlit as st
import mysql.connector
import pandas as pd

st.markdown("<meta http-equiv='refresh' content='900'>", unsafe_allow_html=True)


conn = mysql.connector.connect(host='localhost', user='paakaytt', password='LempPass123!', database='weather_db')
df = pd.read_sql('SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 50',conn)
conn.close()

st.title('Säädata Helsingistä')
st.dataframe(df)

st.line_chart(df.set_index("timestamp")[["temperature"]])
