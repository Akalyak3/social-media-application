# backend/app/__init__.py

from flask import Flask
from .models import db
from .routes.users import users
from .routes.posts import posts

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dashboard_user:yourpassword@localhost/social_media_dashboard'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(posts, url_prefix='/posts')

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
