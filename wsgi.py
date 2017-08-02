from app import application
'''uncomment below for flask-admin stuff
from app import db
from flask_login import LoginManager
from app.auth.models import User

login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = 'login'

# Create user loader function
@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)
'''

if __name__ == "__main__":
    application.run()