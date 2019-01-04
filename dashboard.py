# coding: utf-8
import pandas as pd

from rq import Queue, Connection
from rq.job import Job

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
import dash.dependencies
from dash.dependencies import Input, Output, State
import plotly

from run_worker import conn

from postgres_utils import replace_table, find_df, get_db, remove_table

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

db = get_db()
df_ag = find_df('df_ag', db)

##########
### UI ###
##########

navbar = dbc.Navbar(
					brand="Demo App",
				    brand_href="#",
				    sticky="top",

				    children=[
				        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
				        dbc.NavItem(dbc.NavLink("Page 2", href="#")),
				        dbc.NavItem(dbc.NavLink("Page 3", href="#")),
				        dbc.NavItem(dbc.NavLink("About", href="#")),
				        # dbc.DropdownMenu(
				        #     nav=True,
				        #     in_navbar=True,
				        #     label="Menu",
				        #     children=[
				        #         dbc.DropdownMenuItem("Entry 1"),
				        #         dbc.DropdownMenuItem("Entry 2"),
				        #         dbc.DropdownMenuItem(divider=True),
				        #         dbc.DropdownMenuItem("Entry 3"),
				        #     ],
				        # ),
				    ],
				)

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [

                    	dbc.Button("Run integration", color="secondary", id='button-run-integration'),
                    	html.Div(id='hidden-div-1', style={'display': 'none'}),
                    	html.Span(" "),
                    	dbc.Button("Drop DB", color="secondary", id='button-drop-db'),
                    	html.Div(id='hidden-div-2', style={'display': 'none'}),

                    	html.P(),

                        html.H3("Tables"),

					    dt.DataTable(
					        id='my-datatable',
					        columns=[{"name": i, "id": i} for i in df_ag.columns],
					        data=df_ag.to_dict("rows"),
					        row_selectable='single',
					        editable=True,
					        filtering=True,
					        sorting=True,
					        selected_rows=[],
					        style_table={'overflowX': 'scroll', 'height': 400, 'width': 1200},
					    ),

					    html.Div(id='selected-indexes'),

					    html.P(),

					    html.H3("Charts"),

					    dcc.Graph(
					        id='datatable-subplots'
					    ),

                    ],
                    md=4,
                ),
            ]
        )
    ],
    className="mt-4",
)


app.layout = html.Div([navbar, body])


##############
### SERVER ###
##############

@app.callback(Output(component_id='hidden-div-1', component_property='hidden'), 
			 [Input(component_id='button-run-integration', component_property='n_clicks')])
def run_integration_on_click(n_clicks):
     if n_clicks!=None:
     	with Connection(conn):
	        q = Queue()
	        from worker.tasks import run_integration
	        task = q.enqueue(run_integration)


@app.callback(Output('hidden-div-2', 'hidden'), 
			 [Input('button-drop-db', 'n_clicks')])
def drop_db_on_click(n_clicks):
     if n_clicks!=None:
     	print('remove_table')
     	# remove_table()


@app.callback(Output('datatable-subplots', 'figure'),
              [Input('my-datatable', 'data'),
               Input('my-datatable', 'selected_rows')])
def update_figure(rows, selected_rows):
    dff = pd.DataFrame(rows)

    fig = plotly.tools.make_subplots(
        rows=3, cols=1,
        subplot_titles=('Beef', 'Pork', 'Poultry'),
        shared_xaxes=True)

    marker = {'color': ['#0074D9']*len(dff)}
    for i in (selected_rows or []):
        marker['color'][i] = '#FF851B'

    fig.append_trace({
        'x': dff['state'],
        'y': dff['beef'],
        'type': 'bar',
        'marker': marker
    }, 1, 1)

    fig.append_trace({
        'x': dff['state'],
        'y': dff['pork'],
        'type': 'bar',
        'marker': marker
    }, 2, 1)

    fig.append_trace({
        'x': dff['state'],
        'y': dff['poultry'],
        'type': 'bar',
        'marker': marker
    }, 3, 1)

    fig['layout']['showlegend'] = False
    fig['layout']['height'] = 1000
    fig['layout']['width'] = 1200
    fig['layout']['margin'] = {'l': 40, 'r': 10, 't': 60, 'b': 200
    }
    return fig
