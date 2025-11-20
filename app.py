import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Global Security Dashboard",
    page_icon="🌍",
    layout="wide"
)

# ===== Custom background (CSS gradient) ======
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0F2027, #203A43, #2C5364);
    color: white;
}
[data-testid="stSidebar"] {
    background: #1b1b1b;
}
h1, h2, h3, h4 {
    color: #f2f2f2 !important;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Image header
image = Image.open("/Users/administrator/Desktop/датасаинс/header.png")
st.image(image, use_column_width=True)

st.title("🌍 Global Security & Risk Intelligence Dashboard")
st.markdown("""
## Інтерактивна аналітична система  
Оцінка безпеки країн світу на основі:
- військових витрат  
- рівня вбивств  
- governance-індикаторів  
- тероризму  
- конфліктів  
- внутрішнього переміщення населення  

Перейдіть у меню зліва, щоб переглянути модулі.
""")
