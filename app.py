import dash
import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc
from components import nav, jumbotron, cards, graphs, about
from components.graphs import register_graph_callbacks
import dash_dangerously_set_inner_html

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)



app = dash.Dash(external_stylesheets=[dbc.themes.LUX])

register_graph_callbacks(app)

app.config.suppress_callback_exceptions = True

server = app.server

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div([
    nav.navbar,
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])




index_page = html.Div(style={'backgroundColor': colors['background']}, children=[
    jumbotron.jumbotron, 
    html.Div([cards.count_card, cards.total_count_card], style={"display": "flex", 'margin': '0 auto'}),
    
])

location_layout = html.Div([
    jumbotron.jumbotron,
    html.H1("Where are islamophobic tweets coming from?", className="location-title", style={'text-align': 'center', "padding-top": "25px", "padding-bottom": "25px"}),
    graphs.tabs,
    # graphs.location_graph,
    # html.Div( [graphs.tweet_count, graphs.user_count], className="card text-white bg-danger mb-3", style={"display": "flex", "text-align": "center", "align-items": "center", 'margin': '0 auto'}),
    # graphs.world_time,
    # graphs.us_graph
],  style={'width': '100vh', 'height': '300px', 'margin': '0 auto'})

# count_layout = html.Div([
#     html.Div([cards.count_card, cards.total_count_card], style={"display": "flex"}),
# ])
about_layout2 = html.Div([
  about.jumbo
])

about_layout = html.Div([
    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
       
<div id= "sources" style="overflow: hidden; padding-top:100px">

<div class="card text-white bg-dark mb-3" >
  <div class="card-body">
    <h4 class="card-title">What is this website?</h4>
    <p class="card-text"> This website seeks to display location-based analysis on Tweets that present islamophobic call-to-action or hate speech. Users may interact with the map to identify how many islamophobic tweets were posted within the last week at any location. Upon clicking on a location, the user may see a time series on number of tweets per day over the last week, and view what news headlines were most popular on a given day. Here the user may analyze rhetoric used in different headlines and news articles and how that may influence hate speech on social media. </p>
    <br> 
    <h4 class="card-title">What does this dataset contain?</h4>
    <p class="card-text">This dataset contains all tweets from 10/16/2020 to 10/24/2020 containing the keywords "ban islam". The goal of this project is to eventually be able to dynamically fetch data from current tweets and trends. The dataset used as well as the steps taken to scrape and parse the tweets can be found <a class="card-text", href="https://github.com/taniaarya/islamophobia-dashboard", style={'text-color': 'white'}>here</a></p>
    
    <br>
    <h4 class="card-title">Resources Used</h4>
    <div>
      <a class="card-text", href="https://developer.twitter.com/en/docs/twitter-api", style={'color': 'white'}>Twitter API</a>
      <a class="card-text", href="https://newsapi.org/", style={'text-color': 'white'}>News API</a>
    </div>
    
  </div>
</div>
<div class="card bg-secondary mb-3" >
  <div class="card-header">How did we get the data?</div>
  <div class="card-body">
    <h4 class="card-title">Secondary card title</h4>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
  </div>
</div>



</div> 
    '''),
])

# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    print(pathname)
    # if pathname == '/locations':
    #     return location_layout
    # elif pathname == '/counts':
    #     return count_layout
    if pathname == '/about': 
        return about_layout2
    else:
        return location_layout



if __name__ == '__main__':
    app.run_server(debug=True)