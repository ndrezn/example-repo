from dash import Dash, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv"
)

app = Dash()

server = app.server

app.layout = [
    dcc.Markdown("""
        # Welcome to Plotly Dash!
                 
        With Dash Open Source, you can create data apps on your laptop in pure Python, 
        no JavaScript required.

        Get familiar with Dash by building a [sample app](https://dash.plotly.com/tutorial) 
        with open source. Scale up with [Dash Enterprise](https://plotly.com/dash/) when 
        your Dash app is ready for department or company-wide consumption. Or, launch your 
        initiative with Dash Enterprise from the start to unlock developer productivity 
        gains and hands-on acceleration from Plotly's team.
                 
        Try out this Dash app by changing the dropdown value, or get started with Dash on
        HuggingFace by using this app [as a template](http://huggingface.co/new-space?template=plotly/dash-app-template).
    """),
    dcc.Dropdown(df.country.unique(), "Canada", id="dropdown-selection"),
    dcc.Graph(id="graph-content"),
]


@callback(Output("graph-content", "figure"), Input("dropdown-selection", "value"))
def update_graph(value):
    dff = df[df.country == value]
    return px.line(dff, x="year", y="pop")


if __name__ == "__main__":
    app.run(debug=True)
