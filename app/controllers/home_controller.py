from flask import Blueprint, render_template, request
from flask_login import login_user, login_required, logout_user, current_user
from models.user import User
from config.auth import login_manager

@login_manager.user_loader
def load_user(id:int):
    return User.query.get(int(id))

home_blueprint = Blueprint("home", __name__)

@home_blueprint.route("/")
def home():
    return render_template("index.html")

@home_blueprint.route('/login') 
def login():
    return render_template('login.html')

@home_blueprint.route('/auth') 
def auth():
    username = request.args.get("username")
    password = request.args.get("password")
    user = User.query.filter_by(username=username, password=password).first()

    print(user)
    if user:
        login_user(user)
        return render_template('dashboard.html')
    
    return render_template('login.html')

@home_blueprint.route('/auth/profile') 
@login_required
def auth_profile():
    if current_user.es_admin=="1":
        permisos = "Administrador"
    else: permisos ="usuario"   
    
    if current_user.genero=="Masculino":
        usuario = "Bienvenido"
    else: usuario ="Bienvenida"   

    return f'{usuario}: {current_user.username} eres: {permisos}'

@home_blueprint.route('/logout')
def logout():
    logout_user()
    return render_template('login.html')
