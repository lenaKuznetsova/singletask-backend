from flask import Flask
from singletask_sql import engine
from singletask_backend.settings import conf

app = Flask("singletask")
app.db = engine.create_engine(conf)
