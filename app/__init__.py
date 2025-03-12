from flask import Flask
from config.config import Config
from config.db import db
from config.routes import register_routes
from config.auth import login_manager

#def create_app(config):
app = Flask(__name__, template_folder="views")

app.config.from_object(Config)
db.init_app(app)
login_manager.init_app(app)
register_routes(app)

with app.app_context():
        db.create_all()

if __name__ == "__main__":
    app.run(debug=True) 

