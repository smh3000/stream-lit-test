import matplotlib as mpl
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

username=st.text_input("username", value='enter the username')


f1=st.file_uploader("Upload a File", type=None, accept_multiple_files=False, key=None)
df = pd.read_csv(f1)
st.write(df.head())
st.write("List of all the columns")
st.write(df.columns)
columns=df.columns
c1=st.radio("select first column(x axis)", columns,key="1stcolumn")
c2=st.radio("select second column(y axis)", columns,key="2ndcolumn")
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.scatter(
        df[c1],
        df[c2],
    )

ax.set_xlabel(c1)
ax.set_ylabel(c2)

st.write(fig)

h=st.radio("select hue column", columns,key="hue")

sns.scatterplot(x=c1, y=c2, data=df,hue=h)
st.pyplot()
