from dash import Dash, html, dcc
import ids

def sliders_render(app: Dash) -> html.Div:
    sliders_div = html.Div(
        className='sliders',
        children=[
            html.H4('Location parameter μ'),
            dcc.Slider(
                -10, 10, 0.1, id=ids.MI_SLIDER, value=0,
                marks=None,
                tooltip={"placement": "bottom", "always_visible": True, "template": "Loc {value}"}
                ),
            html.H4('Scale parameter σ'),
            dcc.Slider(
                -10, 10, 0.1, id=ids.SIGMA_SLIDER, value=1,
                marks=None,
                tooltip={"placement": "bottom", "always_visible": True, "template": "Scale {value}"}),
            ],
    )
    return sliders_div