from dash import Dash, html
from components.histogtam_components import hist_render
from components.dropdown_components import distr_render, data_render
from components.sliders_components import sliders_render
import pandas as pd

def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    main_div = html.Div(
        className='app-div',
        children=[
            html.H1("Statistics Lab:", style={'textAlign':'center'}),
            
            html.Hr(),
            html.H2('Plot Data:'),
            distr_render(app),
            data_render(app, data),

            html.Hr(),
            html.H2('Plot:', style={'textAlign':'center'}),
            hist_render(app, data),

            sliders_render(app),
            
        ]
    )
    return main_div