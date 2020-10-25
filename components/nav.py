import dash_bootstrap_components as dbc
import dash_html_components as html 

nav = dbc.Nav(
    [
        #dbc.NavItem(dbc.NavLink("Locations", active=True, href="/locations", style={'color': "white"})),
        #dbc.NavItem(dbc.NavLink("Counts", href="/counts", style={'color': "white"})),
        dbc.NavItem(dbc.NavLink("About", href="/about", style={'color': "white"})),
        # dbc.NavItem(dbc.NavLink("Another link", href="#")),
        # dbc.NavItem(dbc.NavLink("Disabled", disabled=True, href="#")),
        # dbc.DropdownMenu(
        #     [dbc.DropdownMenuItem("Item 1"), dbc.DropdownMenuItem("Item 2")],
        #     label="Dropdown",
        #     nav=True,
        # ),
    ]
)

navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    #dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("Home", className="ml-2")),
                    nav
                ],
                align="center",
                no_gutters=True,
            ),
            href="/#",
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
    ],
    color="dark",
    dark=True,
)