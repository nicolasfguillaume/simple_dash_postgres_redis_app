# coding: utf-8

# https://testdriven.io/asynchronous-tasks-with-flask-and-redis-queue

# https://realpython.com/flask-by-example-implementing-a-redis-task-queue/
# we listened for a queue called default and established a connection to 
# the Redis server on localhost:6379

import os
import redis
from rq import Worker, Queue, Connection

REDIS_PORT = '6389'

listen = ['default']

redis_url = 'redis://localhost:{}/0'.format(REDIS_PORT)   # temp -- app.config['REDIS_URL']

conn = redis.from_url(redis_url)

if __name__ == '__main__':

    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()