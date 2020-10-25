import dash
import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import country_converter as coco
import pandas as pd
from urllib.request import urlopen
import json
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import datetime as dt
import requests

df_all = pd.read_csv("https://raw.githubusercontent.com/taniaarya/islamophobia-dashboard/main/hate_speech2.csv")

df_count = df_all.dropna(subset=['country'])
cc = coco.CountryConverter()
iso2_code = list(df_count['country'].to_numpy())
df_count['country'] = cc.convert(names=iso2_code, to='ISO3')
data = df_count.groupby('country').country.count()
df3 = pd.DataFrame({'country': data.index, 'count': data})

world_fig = px.choropleth(
    df3, 
    locations='country',
    hover_name="country", 
    color="count", 
    color_continuous_scale = ["Pink", "IndianRed", "DarkRed"],
    range_color = (0,500), 
    )

#world_fig.update_layout(font_color='white', width=1000, height=600)

df_us = df_count[df_count.country == "USA"]
data = df_count.groupby('fips').country.count()
df4 = pd.DataFrame({'fips': data.index, 'count': data})
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
geojson=counties
us_fig = px.choropleth(df4, geojson=counties, locations="fips", color="count",
                           color_continuous_scale=["Pink", "IndianRed", "DarkRed"],
                           range_color=(0, 12),
                           scope="usa",
                          )



location_graph = dcc.Graph(
                        id='world-graph',
                        figure= world_fig
                    )

us_graph = dcc.Graph(
                        id='us-graph',
                        figure= us_fig
                    )

tweet_count = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H1(children="-", id="tweet-total"),
                html.H4("hate tweets detected")                        
            ]
        ),
    ],
)
user_count = dbc.Card( 
    dbc.CardBody(
        [
                html.H1(children="-", id="user-total"),
                html.H4("different users")
        ]
    ),
   
)

us_tweet_count = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H1(children="-", id="us-tweet-total"),
                html.H4("hate tweets detected")                        
            ]
        ),
    ],
)
us_user_count = dbc.Card( 
    dbc.CardBody(
        [
                html.H1(children="-", id="us-user-total"),
                html.H4("different users")
        ]
    ),
   
)

headlines = dbc.Card( 
    dbc.CardBody(
        [
            html.Div(id="world-headlines") 
        ]
    )
   
)

us_headlines = dbc.Card( 
    dbc.CardBody(
        [
            html.Div(id="us-headlines") 
        ]
    )
   
)

world_time = dcc.Graph(
                        id='world-timeseries'
                    )

us_time = dcc.Graph(
                        id='us-timeseries'
                    )


tabs = html.Div([
    dcc.Tabs(id='tabs', value='world', children=[
                dcc.Tab(label='World', value='world'),
                dcc.Tab(label='US', value='us'),
    ],
    colors={
        "border": "#343a3f",
        "primary": "red",
        #"background": "#343a3f"
    }),
    html.Div(id='tabs-content')
])


# total count
        # timeseries
        # top 3?
        # most recent
        # 




def register_graph_callbacks(app):

    @app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
    def render_content(tab):
        if tab == 'world':
            return html.Div([
                location_graph,
                html.Div([tweet_count], className= "card text-white bg-dark mb-3", style={"width": "50%",
  "margin": "0 auto", "float": "left", "text-align": "center", "padding-left": "50px"}),
                html.Div([user_count], className= "card text-white bg-dark mb-3", style={ "width": "50%",
  "margin": "0 auto", "overflow": "hidden", "text-align": "center", "padding-left": "25px", "padding-right": "50px"}),
                world_time,
                headlines
                #html.Div(id="world-headlines")
            ], style = {"overflow":"hidden"}) 
        elif tab == 'us':
            return html.Div([
                us_graph,
                html.Div([us_tweet_count], className= "card text-white bg-dark mb-3", style={"width": "50%",
  "margin": "0 auto", "float": "left", "text-align": "center", "padding-left": "50px"}),
                html.Div([us_user_count], className= "card text-white bg-dark mb-3", style={ "width": "50%",
  "margin": "0 auto", "overflow": "hidden", "text-align": "center", "padding-left": "25px", "padding-right": "50px"}),
                us_time,
                us_headlines
                #html.Div(id="world-headlines")
            ], style = {"overflow":"hidden"}) 

    @app.callback(
        Output(component_id='tweet-total', component_property='children'),
        [Input(component_id='world-graph', component_property='clickData')])
    def get_tweet_data(clickData):
        if clickData is None:
            raise PreventUpdate
        country = clickData["points"][0]["location"]
        df = df_count[df_count.country == country]
        num = df.shape[0]
        return str(num) 

    @app.callback(
        Output(component_id='user-total', component_property='children'),
        [Input(component_id='world-graph', component_property='clickData')])
    def get_user_data(clickData):
        if clickData is None:
            raise PreventUpdate
        country = clickData["points"][0]["location"]
        df = df_count[df_count.country == country]
        num = len(df.screen_name.unique())
        return str(num) 


    @app.callback(
        Output(component_id='us-tweet-total', component_property='children'),
        [Input(component_id='us-graph', component_property='clickData')])
    def get_us_tweet_data(clickData):
        if clickData is None:
            raise PreventUpdate
        fips = clickData["points"][0]["location"]
        df = df_count[df_count.fips == fips]
        num = df.shape[0]
        return str(num) 

    @app.callback(
        Output(component_id='us-user-total', component_property='children'),
        [Input(component_id='us-graph', component_property='clickData')])
    def get_us_user_data(clickData):
        if clickData is None:
            raise PreventUpdate
        fips = clickData["points"][0]["location"]
        df = df_count[df_count.fips == fips]
        num = len(df.screen_name.unique())
        return str(num)

    @app.callback(
        Output(component_id='world-timeseries', component_property='figure'),
        [Input(component_id='world-graph', component_property='clickData')])
    def get_timeseries(clickData):

        if clickData is None:
            raise PreventUpdate

        country = clickData["points"][0]["location"]
        df = df_count[df_count.country == country]
        df["create_dt"] = pd.to_datetime(df['create_dt'])
        df.sort_values(by=["create_dt"], ascending=False)
        df_temp =  df['create_dt'].dt.floor('d').value_counts().rename_axis('date').reset_index(name='count')
        df_temp = df_temp.sort_values(by=["date"])
        fig = px.line(df_temp, x="date", y="count")

        return fig
        
    @app.callback(
        Output(component_id='us-timeseries', component_property='figure'),
        [Input(component_id='us-graph', component_property='clickData')])
    def get_timeseries(clickData):

        if clickData is None:
            raise PreventUpdate

        fips = clickData["points"][0]["location"]
        df = df_count[df_count.fips == fips]
        df["create_dt"] = pd.to_datetime(df['create_dt'])
        df.sort_values(by=["create_dt"], ascending=False)
        df_temp =  df['create_dt'].dt.floor('d').value_counts().rename_axis('date').reset_index(name='count')
        df_temp = df_temp.sort_values(by=["date"])
        fig = px.line(df_temp, x="date", y="count")
        
        return fig

    @app.callback(
        Output(component_id='world-headlines', component_property='children'),
        [Input(component_id='world-timeseries', component_property='clickData')])
    def get_timeseries(clickData):

        if clickData is None:
            raise PreventUpdate

        date = clickData["points"][0]["x"]

        headers = {'Authorization': 'b7de039e294740bb84d8dff8c2bbf97d'}
        everything_news_url = 'https://newsapi.org/v2/everything'
 
        # Add parameters to request URL based on what type of headlines news you want
        
        # All the payloads in this section
        headlines_payload = {}
        everything_payload = {'q': 'muslim', 'language': 'en', 'sortBy': 'popularity','from': date, 'to': date}
        sources_payload = {'category': 'general', 'language': 'en'}
        
        # Fire a request based on the requirement, just change the url and the params field
        
        # Request to fetch the top headlines
        # response = requests.get(url=top_headlines_url, headers=headers, params=headlines_payload)
        
        # Request to fetch every news article
        response = requests.get(url=everything_news_url, headers=headers, params=everything_payload)
        return html.Div([
            html.H2(f"Top Headlines for {date} with 'Muslim'"),
            html.Div([html.Div([html.A(req['title'], href=req['url'])]) for req in response.json()['articles']])
            
        ])

    
    @app.callback(
        Output(component_id='us-headlines', component_property='children'),
        [Input(component_id='us-timeseries', component_property='clickData')])
    def get_timeseries(clickData):

        if clickData is None:
            raise PreventUpdate

        date = clickData["points"][0]["x"]

        headers = {'Authorization': 'b7de039e294740bb84d8dff8c2bbf97d'}
        everything_news_url = 'https://newsapi.org/v2/everything'
 
        # Add parameters to request URL based on what type of headlines news you want
        
        # All the payloads in this section
        headlines_payload = {'country': 'us'}
        everything_payload = {'q': 'muslim', 'language': 'en', 'sortBy': 'popularity','from': date, 'to': date}
        sources_payload = {'category': 'general', 'language': 'en', 'country': 'us'}
        
        # Fire a request based on the requirement, just change the url and the params field
        
        # Request to fetch the top headlines
        # response = requests.get(url=top_headlines_url, headers=headers, params=headlines_payload)
        
        # Request to fetch every news article
        response = requests.get(url=everything_news_url, headers=headers, params=everything_payload)
        return html.Div([
            html.H2(f"Top Headlines for {date} with 'Muslim'"),
            html.Div([html.Div([html.A(req['title'], href=req['url'])]) for req in response.json()['articles']])
            
        ])
        
        # pretty_json_output = json.dumps(response.json(), indent=4)
        #print(pretty_json_output)
        
        #return pretty_json_output
        