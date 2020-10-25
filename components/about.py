import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_dangerously_set_inner_html

jumbo = dbc.Jumbotron(
    [
        html.H1("About", className="display-3"),
        html.Hr(className="my-2"),
        html.P(
            "What is this website?",
            className="lead",
        ),
        html.P(
            "This website seeks to display location-based analysis on Tweets that present islamophobic call-to-action or hate speech. Users may interact with the map to identify how many islamophobic tweets were posted within the last week at any location. Upon clicking on a location, the user may see a time series on number of tweets per day over the last week, and view what news headlines were most popular on a given day. Here the user may analyze rhetoric used in different headlines and news articles and how that may influence hate speech on social media. "
        ),

        html.Hr(className="my-2"),

        html.P(
            "What does this dataset contain?",
            className="lead",
        ),
        html.P(
            "This dataset contains all tweets from 10/16/2020 to 10/24/2020 containing the keywords 'ban islam'. The goal of this project is to eventually be able to dynamically fetch data from current tweets and trends. The dataset used as well as the steps taken to scrape and parse the tweets can be found at:"
        ),
        html.A(
            "https://github.com/taniaarya/islamophobia-dashboard",
            href="https://github.com/taniaarya/islamophobia-dashboard"
        ),

        html.Hr(className="my-2"),

        html.P(
            "Resources Used",
            className="lead",
        ),
        html.A(
            "Dash",
            href="https://plotly.com/dash/"
        ),
        html.P(
            "",
            className="lead",
        ),
        html.A(
            "Plotly",
            href="https://plotly.com/"
        ),
        html.P(
            "",
            className="lead",
        ),
        html.A(
            "Twitter API",
            href="https://developer.twitter.com/en/docs/twitter-api" 
        ),
        html.P(
            "",
            className="lead",
        ),
        html.A(
            "News API",
            href="https://newsapi.org/"
        ),
        html.P(
            "",
            className="lead",
        ),
        html.A(
            "Reverse Geocoder",
            href="https://github.com/thampiman/reverse-geocoder"
        ),
        


        #html.P(dbc.Button("Learn more", color="primary"), className="lead"),
    ]
)
 

# what is the purpose?
# how did we get the data?