import pandas as pd
import streamlit as st

st.sidebar.title("Data Analysis Dashboard : Explore, Analyze, and Visualize Your Dataset")
st.sidebar.video('data-analysis-vid.mp4')
st.sidebar.image('Data_image.jpg')
st.header('Load Your Data in this section')
# Function that loads the dataset
@staticmethod
def load_dataset():
    try:
        global file 
        file = st.file_uploader('Upload your dataset:')
        if file is not None:
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            elif file.name.endswith(('.xlsx', '.xls')):
                df = pd.read_excel(file)
            else:
                st.error('Invalid file format. Please upload a CSV or Excel file.')
            st.dataframe(df)
            return df
        else:
            st.warning('Please upload your dataset.')
    except:
        st.error('Error occurred while loading the dataset or Your dataset is unstructured or has a problem')
       
df = load_dataset()
print(df)

if df is not None:
    st.subheader(f'Shape of the dataset : {df.shape[0]} rows, {df.shape[1]} colums')

    st.subheader('Clear overview of the structure data and content')
    st.dataframe(pd.concat([df.head(), df.tail()]))

    st.subheader('Statistical Analysis')
    st.dataframe(df.describe())

    st.subheader('Analysis of Object types in dataframe')
    st.dataframe(df.dtypes)

    st.markdown('---')


