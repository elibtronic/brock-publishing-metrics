import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Brock University Journal Dynamics")
st.write(""" :books: Providence: OpenAlex, by academic year (July 1 - july 30), ROR in record as Brock University""")

upa_df = pd.read_csv("uap_report.csv")
fig = px.bar(upa_df, x="Year", y =["Closed Publications", "Open Access Publications"],barmode="stack")
st.plotly_chart(fig)


st.download_button(
	label = "Download Data",
	data = upa_df.to_csv().encode("utf-8"),
	file_name = "uap_report",
	mime = "text/csv",
	icon = ":material/download:"
	)