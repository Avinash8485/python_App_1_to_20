import streamlit as s
import plotly.express as ps
from backend import get_data


s.title("Weather Forecast For the Next Days")
place = s.text_input("Place: ")
days = s.slider("Forecast Days",min_value=1,max_value=5,help="select the number of forecasted days ")
view = s.selectbox("Select data to view",("temperature","Sky"))

s.subheader(f"{view} for the next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place,days)


        if view == "Temperature":
            temperature = [entry["main"]["temp"]/10 for entry in filtered_data] 
            dates =[entry["dt_txt"] for entry in filtered_data]
            figure =ps.line(x=dates,y=temperature,labels={"X":"Date","Y":"Temprature(C)"})
            s.plotly_chart(figure)

        if view == "Sky":
            images = {"Clear":"images/clear.png","Clouds":"images/cloud.png",
                    "Rain":"images/rain.png","Snow":"images/snow.png"}
            sky = [entry["weather"][0]["main"] for entry in filtered_data]
            images_path = [images[conditions] for conditions in sky]
            s.image(images_path,width=115)

    except KeyError:
        s.write("That placce is does not exist")
