import streamlit as st
from openai import OpenAI

st.balloons()
st.title("CEDH ChatbootApp")
st.write(
   "Este es un chat destinado a la población del estado de Chihuahua, con el objetivo de brindar asesoramiento de los derechos humanos."
)
openai_api_key = st.secrets["api_key"] 
# Create an OpenAI client.
client = OpenAI(api_key=openai_api_key)

prompt = st.chat_input("Hola, pregúntame algo...")
if prompt==None:
   st.stop()

with st.chat_message("user"):
   st.markdown(prompt)

# Generate a response using the OpenAI API.

stream = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "system", "content": "Eres una asistente virtual encargada de brindar asesoramiento a la población del estado de Chihuahua relacionada a los Derechos Humanos; todo lo que respondas dentro de este chat que sea basado en documentación oficial y principalmente de la página https://cedhchihuahua.org.mx."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=0,
    )
respuesta = stream.choices[0].message.content
with st.chat_message("assistant"):
   st.write(respuesta)
