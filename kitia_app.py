import streamlit as st

st.set_page_config(page_title='KitIA', page_icon='🔧', layout='wide')
st.title('🔧 KitIA - Diagnóstico de circuitos')
st.subheader('Para docentes rurales sin conectividad')
st.markdown('---')

ERRORES = {
  'LED en polaridad inversa': {
    'situacion': 'Conectaste el LED pero NO enciende',
    'explicacion': 'El LED tiene polaridad invertida: ánodo (pata larga) debe ir al positivo',
    'accion': 'Invierte el LED: pata larga hacia resistencia, pata corta hacia GND',
    'tiempo': '15 segundos'
  },
  'Resistencia muy baja': {
    'situacion': 'Parpadea, se calienta o hay riesgo de dañar el pin Arduino',
    'explicacion': 'Pasa más de 20 mA por el pin digital',
    'accion': 'Cambia por resistencia de 330 Ω',
    'tiempo': '20 segundos'
  },
  'Falta GND común': {
    'situacion': 'Sensor no lee o da valores erráticos',
    'explicacion': 'Arduino y sensor deben compartir tierra común',
    'accion': 'Conecta GND del sensor al GND del Arduino',
    'tiempo': '10 segundos'
  }
}

opcion = st.selectbox('Selecciona un caso', list(ERRORES.keys()))
e = ERRORES[opcion]
st.success(opcion)
st.markdown(f'**¿Qué pasa?** {e["situacion"]}')
st.markdown(f'**¿Por qué?** {e["explicacion"]}')
st.markdown(f'**¿Qué hacer?** {e["accion"]}')
st.markdown(f'**Tiempo estimado:** {e["tiempo"]}')

st.markdown('---')
st.caption('KitIA | NAUFest 2026 | Herbert Steven Galeano Flores - Guatemala')