import sys
from functools import wraps

from main import app
from extensions import db

from sqlalchemy import create_engine

"""Import all models here to allow the migration"""
from models import User


"""Decorator that create app context"""
def with_app_context(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        with app.app_context():
            f(*args, **kwargs)
    return decorated


""" drop and create all database tables """
@with_app_context
def migrate():
    db.drop_all()
    db.create_all()


""" print a list with all tables in database """
@with_app_context
def show_tables():
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    tables: list = engine.table_names()

    print("-------------TABLES-------------")

    for table in tables:
        print(table)

    print("--------------------------------")


""" Create a simple CLI for database operations
    Use -m or --migrate to migrate the database
    -t or --tables to show all the tables"""
if __name__ == "__main__":

    if '--migrate' in sys.argv or '-m' in sys.argv:
        migrate()

    if '--tables' in sys.argv or '-t' in sys.argv:
        show_tables()