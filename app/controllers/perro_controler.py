from flask import Blueprint, render_template, request
from flask_login import login_required

from models.todo import Todo
from config.db import db

todo_blueprint = Blueprint("Todo", __name__, url_prefix="/todo")

@todo_blueprint.route("/", methods=["GET"])
@login_required
def get_todos():
    todos = []
    if request.args:
        done = request.args.get("done")
        todos = Todo.query.filter(Todo.done == done).all()
    else:
        todos = Todo.query.all()
    return render_template("todos_index.html", todos = todos)