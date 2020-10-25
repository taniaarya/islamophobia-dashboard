import dash_bootstrap_components as dbc
import dash_html_components as html 

jumbotron = dbc.Jumbotron(
    [
        html.H1("Tracking Islamophobia", className="display-3"),
        html.P(
            "Analyzing the impact of news headlines on islamophobic sentiments",
            className="lead",
        ),
        html.Hr(className="my-2"),
        html.P(
            "Social media sites have become a stage for islamophobic rhetoric and hate speech, as well as calls to action such as \"Ban Islam.\" Such behavior not only fuels anti-Muslim sentiment, but it also harms the targeted victims and invokes fear in the Muslim community. However, analyzing trends in Islamophobic speech can offer insights into how we may combat Islamophobia together."
        ),
        #html.P(dbc.Button("Learn more", color="primary"), className="lead"),
    ]
)