import streamlit
import streamlit as st
import plotly.express as px
from backend import get_data

st.set_page_config(layout="wide")
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider(min_value=1,max_value=5,label="Forecast Days",help="Select the number of days")
options = st.selectbox("Select data to view",options=["Temperature","Sky"])
st.subheader("{} for the next {} days in {}".format(options,days,place))

if place:
    # Get the temperature/sky data
    filtered_data = get_data(place,days)

    # Create Temperature plot
    if options == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates,y=temperatures, labels={"x":"Date","y":"Temperatures"})
        st.plotly_chart(figure)

    if options == "Sky":
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        images = {"Clear":"images/clear.png","Clouds":"images/cloud.png","Rain":"images/rain.png","Snow":"images/snow.png"}
        sky_image = [images[condition] for condition in sky_conditions]
        st.image(sky_image, width=115)