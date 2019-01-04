# coding: utf-8
import pandas as pd

# https://realpython.com/flask-by-example-implementing-a-redis-task-queue/
import redis
from rq import Queue, Connection
from rq.job import Job
from run_worker import conn, REDIS_PORT

import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
import dash.dependencies
from dash.dependencies import Input, Output, State
import plotly

from dashboard import app

# set up a Redis connection and initialized a queue based on that connection
q = Queue(connection=conn)
app.config['REDIS_PORT'] = REDIS_PORT

if __name__ == '__main__':
    app.run_server(debug=True)