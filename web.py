import streamlit as st
import pandas as pd
st.title("Welcome to Aishwary Kumar Pradhan")
st.header("Python")
dataset=pd.read_csv("D:\website\laptop_data.csv")
st.dataframe(dataset)
name=st.text_input("please Enter Your Name : ")
fname=st.text_input("Please Enter Your Father Name : ")
address=st.text_area("Enter Your Text For Address And Some thing ")
classdata=st.selectbox("Enter Your Class For ",(1,2,3,4,5,6,7))
buttom=st.button("Submit Data")
if buttom:
    st.markdown(f"""
                Name: {name}\n
                FatherName:{fname}\n
                address:{address}\n
                class:{classdata}\n
                """)