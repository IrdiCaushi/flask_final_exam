from flask import Flask, render_template
from modules.api import auth
from models import UserModel, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def root():
    return render_template('root.html')

app.register_blueprint(auth, url_prefix='/api/v1/auth')
# app.register_blueprint(auth)