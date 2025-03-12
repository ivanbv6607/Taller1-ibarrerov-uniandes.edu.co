from flask import Blueprint, render_template, request
from models.user import User
from config.db import db

todo_blueprint = Blueprint("User", __name__, url_prefix="/user")
