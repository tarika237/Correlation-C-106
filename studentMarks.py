import plotly.express as px
import csv 

with open("Student Marks vs Days Present.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x="Marks in Percentage", y="Days Present")
    fig.show()