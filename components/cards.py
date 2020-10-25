import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

count_card = dbc.Card(
    [
        #dbc.CardImg(src="/static/images/placeholder286x180.png"),
        dbc.CardBody(
            [
                html.H4("[INSERT VARIABLE HERE] Islamophobic Tweets Detected", className="count-card-title"),
                # html.P(
                #     "[INSERT VARIABLE HERE] Tweets Detected",
                #     className="count-card-text",
                # ),
                # html.P(
                #     "[INSERT VARIABLE HERE] Tweets Detected",
                #     className="count-card-text",
                # ),
                dbc.Button("See More", color="primary"),
            ]
        ),
    ],
    #style={"width": "28rem"},
)

total_count_card = dbc.Card(
    [
        #dbc.CardImg(src="/static/images/placeholder286x180.png"),
        dbc.CardBody(
            [
                html.H4("[INSERT VARIABLE HERE] Tweets Searched", className="total-count-card-title"),
                dbc.Button("See More", color="primary"),
            ]
        ),
    ],
)