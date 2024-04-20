from dash import Dash, html
from histogtam_components import hist_render
from dropdown_components import distr_render, data_render
from sliders_components import sliders_render
import pandas as pd

def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    main_div = html.Div(
        className='app-div',
        children=[
            html.H1("Laby ze Statystyki: Lista 2", style={'textAlign':'center'}),
            
            html.Hr(),
            html.H2('Dane:'),
            distr_render(app),
            data_render(app, data),

            html.Hr(),
            html.H2('Wykres:', style={'textAlign':'center'}),
            hist_render(app, data),

            sliders_render(app),
            
        ]
    )
    return main_div