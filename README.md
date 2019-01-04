# Simple Dash Postgres Redis web app

+ Dash framework  
+ PostgreSQL database  
+ Redis  

![Logo](https://github.com/nicolasfguillaume/simple_dash_postgres_redis_app/blob/master/Screen%20Shot%202019-01-04%20at%2017.41.51.png)

Usage:
```
pyenv virtualenv 3.6.3 dash_postgres_3.6.3
pyenv local dash_postgres_3.6.3

pip install -r requirements.txt

docker-compose up -d

# in a terminal, start the worker
python run_worker.py

# in another terminal, start the app
python run_app.py
```

And open a browser at `http://127.0.0.1:8050/`
