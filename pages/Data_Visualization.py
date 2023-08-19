import streamlit as st
import streamlit.components.v1 as components
st.sidebar.markdown("# Dataset Utilized for the Analysis")
st.sidebar.markdown('<a style="font-size: 22px; color: #FF5733;" href="https://www.kaggle.com/code/danielbethell/laptop-prices-prediction/data" target="_blank">Explore the dataset on Kaggle</a>', unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.title("Source Code")
st.sidebar.image("git.png")
st.sidebar.write("[Click here](https://github.com/abhikritimoti/-Laptop_Price_Prediction.git) to get the source code.")
st.sidebar.markdown("""### <br>
## :copyright: Abhikriti Moti <br> Email: <a href="abhikriti.12007073@lpu.in">abhikriti.12007073@lpu.in </a>""", unsafe_allow_html=True)

# st. set_page_config(layout="wide")

st.header("Analysis")
path_to_html = "LaptopPricePrediction.html"
with open(path_to_html,'r',encoding='utf-8') as f:
    html_data = f.read()
html_height = html_data.count('\n')
st.components.v1.html(html_data, height=html_height * 1.75)