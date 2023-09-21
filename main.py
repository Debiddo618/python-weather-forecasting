import streamlit
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider(min_value=1,max_value=5,label="Forecast Days",help="Select the number of days")
options = st.selectbox("Select data to view",options=["Temperature","Sky"])
st.subheader("{} for the next {} days in {}".format(options,days,place))

def get_data(days):
    dates = ["2022-25-10","2022-22-10","2022-21-10","2022-20-10"]
    temperatures=[0,3,2,4]
    temperatures=[days*i for i in temperatures]
    return dates,temperatures
d,t = get_data(days)
figure = px.scatter(x=d,y=t, labels={"x":"Date","y":"Temperatures"})
st.plotly_chart(figure)