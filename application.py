# -*- coding: utf-8 -*-

# venv activation "source venv/bin/activate"
# http://cewing.github.io/training.python_web/html/presentations/venv_intro.html

# from flask import Flask

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly

app = dash.Dash(__name__)
application = app.server
# app = dash.Dash()

# plotly.tools.set_credentials_file(username='gclabbe', api_key='r4ooofWmTz72bXx1WwQd')

import pandas as pd
import numpy as np

tempsC = np.arange(50, 100)
tempsF = tempsC * 9/5 + 32
tempsK = tempsC + 273.15
UrelIAA = 2.39 * 10**11 * np.exp(-9773/tempsK)
UrelIBU = 0.15642 * np.exp(0.01856*tempsC)

app.layout = html.Div(children=[
    html.H1(children="Lob's Beer Cals"),

    html.Div(children='''
        Exploring hop utilization discussion from Alchemy Overlord blog
    '''),

    html.Br(),

    html.Div(children='''
        https://alchemyoverlord.wordpress.com/2016/03/06/an-analysis-of-sub-boiling-hop-utilization/
    '''),

    html.Div(children='''
        https://alchemyoverlord.wordpress.com/2017/01/03/a-summary-of-factors-affecting-ibus/#accounting_for_post_boil
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': tempsC, 'y': UrelIAA, 'type': 'lines+markers', 'name': 'IAA'},
                {'x': tempsC, 'y': UrelIBU, 'type': 'lines+markers', 'name': 'IBU'},
            ],
            'layout': {
                'title': 'Utilization Relative to Temperature',
                'xaxis': { 'title': 'degrees C' },
                'yaxis': { 'title': 'relative %' }
            }
        }
    )
])

if __name__ == '__main__':
    application.run(debug=True)