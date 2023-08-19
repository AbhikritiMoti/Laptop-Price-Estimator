import streamlit as st
import pandas as pd
import io

data = pd.read_csv('laptop_data.csv')
st.markdown("# Data Playground")

st.sidebar.markdown("# Dataset Utilized for the Analysis")
st.sidebar.markdown('<a style="font-size: 22px; color: #FF5733;" href="https://www.kaggle.com/code/danielbethell/laptop-prices-prediction/data" target="_blank">Explore the dataset on Kaggle</a>', unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.title("Source Code")
st.sidebar.image("git.png")
st.sidebar.write("[Click here](https://github.com/abhikritimoti/-Laptop_Price_Prediction.git) to get the source code.")
st.sidebar.markdown("""### <br>
## :copyright: Abhikriti Moti <br> Email: <a href="abhikriti.12007073@lpu.in">abhikriti.12007073@lpu.in </a>""", unsafe_allow_html=True)

st.markdown("---")

st. set_page_config(layout="wide")

# Interactive Widgets
st.markdown("## Filtered Data Using Interactive Widgets")
num_rows = st.slider("Select the number of rows to display:", 1, len(data), len(data))
selected_columns = st.multiselect("Select columns to display:", data.columns)
display_data = data[selected_columns][:num_rows]
st.dataframe(display_data)

st.markdown("---")

# Data Filtering and Sorting
st.markdown("## Data Filtering and Sorting")
default_option1 = "Company"
selected_column_for_filter = st.selectbox("Select a column for filtering:", data.columns, index=data.columns.get_loc(default_option1))
filter_value = st.selectbox(f"Filter {selected_column_for_filter} by:", data[selected_column_for_filter].unique())
filtered_data = data[data[selected_column_for_filter] == filter_value]

default_option2 = "Inches"
selected_column_for_sort = st.selectbox("Select a column for sorting:", data.columns, index=data.columns.get_loc(default_option2))
sort_order = st.radio("Sort Order:", ("Ascending", "Descending"))
if sort_order == "Ascending":
    filtered_data = filtered_data.sort_values(by=selected_column_for_sort, ascending=True)
else:
    filtered_data = filtered_data.sort_values(by=selected_column_for_sort, ascending=False)


st.dataframe(filtered_data)

# Download Button
if st.button("Download Filtered Data"):
    output = io.BytesIO()
    csv_file = filtered_data.to_csv(output, index=False)
    output.seek(0)
    st.download_button("Download CSV", data=output, file_name='filtered_data.csv')

# Adding a download button for the filtered data in Excel format
if st.button("Download Filtered Data (Excel)"):
    output = io.BytesIO()
    excel_file = filtered_data.to_excel(output, index=False, sheet_name='filtered_data')
    output.seek(0)
    st.download_button("Download Excel", data=output, file_name='filtered_data.xls')




