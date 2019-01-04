# coding: utf-8
import pandas as pd
from sqlalchemy import create_engine

def get_db():
	# https://www.tutorialspoint.com/postgresql/postgresql_python.htm
	return create_engine('postgresql://postgres:example@localhost:5400/postgres')


def replace_table(df, table_name, db):
	df.to_sql(table_name, db, if_exists='replace')


def find_df(table_name, db):
	return pd.read_sql_query('select * from {}'.format(table_name), db)


def remove_table(df, table_name, db):
	pd.DataFrame().to_sql(table_name, db, if_exists='replace')