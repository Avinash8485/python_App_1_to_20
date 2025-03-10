from flask import Flask,render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt",skiprows=17)
stations = stations[["STAID","STANAME                                 "]]

@app.route("/")#decorater when user hits that url then the below methos starts executing
def home():
    return render_template("home.html",data = stations.to_html())

@app.route("/api/v1/<station>/<date>")
#<> - to infrom that the user can enter any number ot string , we can take that variable and we can use it in paramter
def about(station,date):
    station_zfill = str(station).zfill(6)
    filename ="data_small/TG_STAID"+station_zfill+".txt"
    df = pd.read_csv(filename,skiprows=20,parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"]==date]['   TG'].squeeze()/10
    return {"Station":station,
            "date":date,
            "temprature":temperature}

@app.route("/api/v1/<station>")
#<> - to infrom that the user can enter any number ot string , we can take that variable and we can use it in paramter
def station_data(station):
    station_zfill = str(station).zfill(6)
    filename ="data_small/TG_STAID"+station_zfill+".txt"
    df = pd.read_csv(filename,skiprows=20,parse_dates=["    DATE"])
    result = df.to_dict(orient="records") 
    return result

@app.route("/api/v1/year/<station>/<year>")
#<> - to infrom that the user can enter any number ot string , we can take that variable and we can use it in paramter
def station_data_yearly(station,year):
    station_zfill = str(station).zfill(6)
    filename ="data_small/TG_STAID"+station_zfill+".txt"
    df = pd.read_csv(filename,skiprows=20)
    df["    DATE"]=df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result



app.run(debug=True)# to see the erroes in console