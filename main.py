import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# import the model
# pipe = pickle.load(open('pipe.pkl','rb'))
# df = pickle.load(open('df.pkl','rb'))
pipe = pd.read_pickle('pipe.pkl')
df = pd.read_pickle('df.pkl')


# st.sidebar.subheader("Correlation b/w Laptop configurations")
# hm = pd.read_csv('clean.csv')
# fig = plt.figure(figsize=(5, 3)) #facecolor= "#262730"
# sns.heatmap(hm.corr())
# sns.set_style("white")
# st.sidebar.pyplot(fig)

st.image("image.jpg")
st.title("Laptop Price Prediction :chart_with_upwards_trend:")
st.markdown("""### 
#### This model predicts laptop price according to the user input configuration """)
#

st.sidebar.title("Source Code")
st.sidebar.image("git.png")
st.sidebar.write("[Click here](https://github.com/abhikritimoti/-Laptop_Price_Prediction.git) to get the source code.")
st.sidebar.markdown("""### <br>
## :copyright: Abhikriti Moti <br> Email: <a href="abhikriti.12007073@lpu.in">abhikriti.12007073@lpu.in </a>""", unsafe_allow_html=True)


company = st.selectbox('Brand',df['Company'].unique())

type = st.selectbox('Type',df['TypeName'].unique())

ram = st.selectbox('RAM (in GB)',[2,4,6,8,12,16,24,32,64])

weight = st.number_input('Weight of the Laptop')

touchscreen = st.selectbox('Touchscreen',['No','Yes'])

ips = st.selectbox('IPS',['No','Yes'])

screen_size = st.number_input('Screen Size')

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
    st.markdown("## The predicted price of this configuration is ")
    st.markdown("# ₹ " + str(int(np.exp(pipe.predict(query)[0]))))

st.markdown(""" ## <br> """, True)
st.markdown("""---""")
st.markdown(""" ## Dataset Used :mag_right: <br> 
####  [kaggle link](https://www.kaggle.com/code/danielbethell/laptop-prices-prediction/data) """, True)
data = pd.read_csv('laptop_data.csv')
st.dataframe(data)
