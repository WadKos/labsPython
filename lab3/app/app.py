from flask import Flask, render_template, session, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Для доступа к этой странице необходимо пройти процедуру аутентификации.'
login_manager.login_message_category = 'warning'

class User(UserMixin):
    def __init__(self, id, login):
        self.id = id
        self.login = login
        

@app.route('/')
def index():
    return render_template('index.html')

def get_users():
    users = [
        {
            "id": "1",
            "login": "user",
            "password": "qwerty",
        }
    ]
    return users

def authentificate_user(login, password):
    for user in get_users():
        if user["login"] == login and user["password"] == password:
            auth_user = User(user["id"], user["login"])
            return auth_user
    return None

@login_manager.user_loader
def load_user(user_id):
    for i in range(len(get_users())):
        if get_users()[i]["id"] == user_id:
            user = User(user_id, get_users()[i]["login"])
            return user
    return None

@app.route('/visits')
def visits():
    if 'visit_counter' in session:
        session['visit_counter'] += 1
    else:
        session['visit_counter'] = 1
    return render_template('visits.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
        user_login = request.form["loginInput"]
        user_password = request.form["passwordInput"]
        remember_me = request.form.get('remember_me') == 'on'

        auth_user = authentificate_user(user_login, user_password)
        if auth_user:
            login_user(auth_user, remember=remember_me)
            flash("Вы успешно авторизованы", "success")
            next_ = request.args.get('next')
            return redirect(next_ or url_for("index"))
            
        flash("Введены неверные логин и/или пароль", "danger") 


    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route('/secret_page')
@login_required
def secret_page():
    return render_template('secret_page.html')