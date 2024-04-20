from dash import Dash, dcc, html
import ids
import pandas as pd

AVAILABLE_DISTRS = ['normal', 'exponential', 'gamma', 'beta', 'uniform']
SCIPY_DISTRS = ['norm', 'expon', 'gamma', 'beta', 'uniform']
    
def distr_render(app: Dash) -> html.Div:
    dropdown_div = html.Div(
        className='distr-dropdown',
        children=[
            html.H6('Distributions:'),
            dcc.Dropdown(
                id=ids.DISTR_DROPDOWN,
                options=[
                    {'label':distr_label, 'value':distr_value} 
                    for distr_label, distr_value in zip(AVAILABLE_DISTRS, SCIPY_DISTRS)
                    ],
                value=SCIPY_DISTRS[0],
            )
        ]
    )
    return dropdown_div

def data_render(app: Dash, data: pd.DataFrame) -> html.Div:
    AVAILABLE_DATA = data.columns

    dropdown_div = html.Div(
        className='data-dropdown',
        children=[
            html.H6('Available Data:'),
            dcc.Dropdown(
                id=ids.DATA_DROPDOWN,
                options=[{'label':data_label, 'value':data_label} for data_label in AVAILABLE_DATA],
                value=AVAILABLE_DATA[0],
            )
        ]
    )
    return dropdown_div