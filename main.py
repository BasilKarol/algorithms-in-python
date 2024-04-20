from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP
from layout import create_layout
import pandas as pd

DATA_PATH = "Distributions dashboard/lab2.csv"

def main() -> None:
    data = pd.read_csv(DATA_PATH)

    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Distributions"
    app.layout = create_layout(app, data)
    app.run()

if __name__=="__main__":
    main()



