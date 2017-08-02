# Import flask and template operators
from flask import Flask, render_template
from datetime import datetime

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
'''
#flask login / admin stuff
import flask_login as LoginManager
import flask_admin as admin
'''

# Define the WSGI application object
application = Flask(__name__)

# Configurations
application.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(application)


# error handling
@application.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Import a module / component using its blueprint handler variable (mod_auth)
from app.site.controllers import site as site_module

# Register blueprint(s)
application.register_blueprint(site_module)

# Build the database:
# This will create the database using SQLAlchemy
db.create_all()


@application.context_processor
def inject_now():
    return {'now': datetime.utcnow()}
