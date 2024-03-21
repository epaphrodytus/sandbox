import os 

from flask import Flask

print("__name__:", __name__)

def create_app(test_config=None):
    """
    Create and configure the app 

    All interactions and configurations happen with a global
    instance of the Flask object

    The tutorial calls this Flask object the 
    "application factory"
    """
    # https://flask.palletsprojects.com/en/3.0.x/api/
    app = Flask(__name__, instance_relative_config=True)

    print("app.instance_path:", app.instance_path)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    

    os.makedirs(app.instance_path, exist_ok=True)

    # creates a connection between URL '/hello' and the
    # function it decorates which will return a response
    # in this case, 'Hello, World!'
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    from . import db 
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog 
    app.register_blueprint(blog.bp)
    # this is quite an interesting piece here
    # in blog.bp we did not specify a url_prefix
    # therefore the index view for the blog blueprint
    # will be at /
    # this following effectively says that when a 
    # url_for('index') is called -> which points to /
    # it becomes equivalent to calling url_for('blog.index') -> which also points to /
    app.add_url_rule('/', endpoint='index')
    
    return app