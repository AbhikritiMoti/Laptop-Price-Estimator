import streamlit as st
# import pickle
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
import plotly.express as px

pipe = pd.read_pickle('pipe.pkl')
df = pd.read_pickle('df.pkl')


def main_page():
    st.text("© 2023 My App. All rights reserved.")

def DataPlayground():
    st.markdown("")

def DataVisualization():
    st.markdown("hi")
    


st. set_page_config(layout="wide")
# Load data
hm = pd.read_csv('clean.csv')
numerical_columns = hm.select_dtypes(include=[np.number])
# Create a Plotly heatmap
fig = px.imshow(numerical_columns.corr())
fig.update_layout(
    width=400,
    height=400,
    xaxis_tickangle=270,
)
st.sidebar.markdown(
                    "<h3 style='font-size: 21px; margin: 0;'> Correlation between Specifications</h3>"
                    "</div>", unsafe_allow_html=True)
st.sidebar.plotly_chart(fig)

st.image("image.jpg")
st.title("Laptop Price Prediction :chart_with_upwards_trend:")
st.markdown("""### 
#### This model predicts Laptop Price Based on User Input Specification""")
#

st.sidebar.title("Source Code")
st.sidebar.image("git.png")
st.sidebar.write("[Click here](https://github.com/abhikritimoti/-Laptop_Price_Prediction.git) to get the source code.")
st.sidebar.markdown("""### <br>
## :copyright: Abhikriti Moti <br> Email: <a href="abhikriti.12007073@lpu.in">abhikriti.12007073@lpu.in </a>""", unsafe_allow_html=True)


company = st.selectbox('Brand',df['Company'].unique())

type = st.selectbox('Type',df['TypeName'].unique())

ram = st.selectbox('RAM (in GB)',[2,4,6,8,12,16,24,32,64])

weight = st.number_input('Weight of the Laptop', step=0.20, value=.69)

touchscreen = st.selectbox('Touchscreen',['No','Yes'])

ips = st.selectbox('IPS',['No','Yes'])

screen_size = st.number_input('Screen Size', step=0.20, value=.69)

resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

cpu = st.selectbox('CPU',df['Cpu brand'].unique())

hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

gpu = st.selectbox('GPU',df['Gpu brand'].unique())

os = st.selectbox('OS',df['os'].unique())

if st.button('Predict Price'):
    # query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])

    query = query.reshape(1,12)
    st.markdown('<span style="color: #b23434; font-size: 30px; ">Predicted Price for Specified Specifications :</span>', unsafe_allow_html=True)
    # Assuming 'pipe' and 'query' are defined earlier
    prediction = int(np.exp(pipe.predict(query)[0]))

    # Creating a box around the text using Markdown
    boxed_text = f'<div style="border: 0.5px solid #b23434;border-radius: 10px; padding: 10px;font-weight: bold; font-size: 50px;"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;₹ {prediction}</div>'

    st.markdown(boxed_text, unsafe_allow_html=True)


