from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import ids
import scipy.stats as distr
import numpy as np
from math import ceil

def getdistr(name):
    try:
        return getattr(distr, name)
    except AttributeError:
        raise ValueError(f"Unknown distribution: {name}")

def create_hist_plot(data: pd.DataFrame, data_label: str, distr: str, distr_params: list[float]) -> go.Figure:
    hist_fig = make_subplots(1, 1) 
    plot_data = data[data_label]

    hist_fig.add_trace(
        go.Histogram(x=plot_data, histnorm='probability density', showlegend=False), 
        1, 1
        )
    x_min = ceil(plot_data.min())-1.5
    x_max = ceil(plot_data.max())
    numbers = np.linspace(x_min, x_max, 10**3)
    hist_fig.add_trace(
        go.Scatter(
            x=numbers, y=getdistr(distr).pdf(numbers, *distr_params), 
            line={'color':'red', 'width':3},
            showlegend=False), 
            1, 1
        )
    hist_fig.update_layout(height=600, width=1000)

    return hist_fig

def hist_render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.HISTOGRAM, 'children'),
        [
            Input(ids.MI_SLIDER, 'value'), 
            Input(ids.SIGMA_SLIDER, 'value'),
            Input(ids.DATA_DROPDOWN, 'value'),
            Input(ids.DISTR_DROPDOWN, 'value'),
        ], 
    )
    def _(mi: float, sigma: float, data_label: str, distr: str) -> html.Div: 
        hist_div = dbc.Row(
            children=[
                dbc.Col( 
                    dcc.Graph( 
                        figure=create_hist_plot(
                            data=data, 
                            data_label=data_label, 
                            distr=distr, 
                            distr_params=[mi, sigma]
                            )
                        ),
                    width={'size':6}  # width did the trick
                    )
            ],
            justify='center', # in combination with 'width' param - centers a plot
        )

        return hist_div
    
    return html.Div(id=ids.HISTOGRAM)

