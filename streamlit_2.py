import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")

data = {
    "num" : [x for x in range(1,11)],
    "square":[x**2 for x in range(1,11)],
    "twice" : [x*2 for x in range(1,11)]
}

st.sidebar.radio("Navigation",["Home","About Us"])
df = pd.DataFrame(data = data)

col = st.sidebar.selectbox("Select a number" , df.columns)

plt.plot(df["num"],df[col])
st.pyplot()

