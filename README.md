# simple_dash_postgres_redis_app
Simple dash postgres redis app

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
