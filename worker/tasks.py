# coding: utf-8
import pandas as pd
from sqlalchemy import create_engine
from postgres_utils import replace_table, find_df, get_db

db = get_db()


def run_integration():

	print('task started')

	# data sources
	US_STATES_URL = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv'
	US_AG_URL = 'https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv'

	df_st = pd.read_csv(US_STATES_URL)
	df_ag = pd.read_csv(US_AG_URL)

	replace_table(df_st, 'df_st', db)
	replace_table(df_ag, 'df_ag', db)

	print('success')

	return True
