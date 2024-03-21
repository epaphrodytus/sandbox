import sqlite3

import click 
from flask import current_app, g

# click stand for Command Line Interface Creation Kit
# documentation link in the README.md file

# from the tutorial:
# g is a special object that is unique for each request
# and is used to store data that might be accessed by multiple functions
# during the request.
# current_app is another special object that points to 
# the Flask application handling the request.

def get_db():
    # this if statement essentially says
    # if there is an existing db connection
    # return it.
    # Otherwise try to connect and return
    # that instead. 
    if 'db' not in g:
        g.db = sqlite3.connect(
            database=current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row # this tells the connection to return rows that behave like dicts
    
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables"""
    init_db()
    click.echo('Initialized the database')

def init_app(app):
    """
    Functions need to be 'registered' with the application instance,
    otherwise they won't be used.
    """
    app.teardown_appcontext(close_db) # tells Flask to call that function every time when cleaning up after returning the response
    app.cli.add_command(init_db_command) # this adds a new command that can be called with the flask command 
