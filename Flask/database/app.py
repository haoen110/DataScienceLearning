from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, flash, request, redirect, url_for, logging, session
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt


app = Flask(__name__)
# Config MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Howie1996925@127.0.0.1/sdsc5003'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
db = SQLAlchemy(app)
connection = db.engine.raw_connection()
cur = connection.cursor()


@app.route('/')
def to_log():
    return render_template('login.html')


@app.route('/index.html')
def index():
    flash('Successfully Logged In', 'success')
    return render_template('index.html')

@app.route('/forgot-password.html')
def forgot_password():
    return render_template('forgot-password.html')

@app.route('/tables.html')
def tables():
    return render_template('tables.html')

@app.route('/charts.html')
def charts():
    return render_template('charts.html')

# 数据库模型继承
# class Users(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(16), unique=True)
#     email = db.Column(db.String(120), unique=True)
#     password = db.Column(db.String(6))
#     if_admin = db.Column(db.Integer, default=0)
#
#     def __init__(self, id, username, email, password, if_admin):
#         self.id = id
#         self.username = username
#         self.email = email
#         self.password = password
#         self.if_admin = if_admin


class RegisterForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords do not match')])
    confirm = PasswordField('Confirm password')


@app.route('/register.html', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))
        # Execute MySQL
        cur.execute("SELECT * FROM users WHERE username = %s;", username)
        result = cur.fetchone()[1]
        if username == result:
            flash('Username Existed.', 'danger')
            return render_template('register.html', form=form)
        db.engine.execute("INSERT INTO users(username, email, password) VALUES(%s, %s, %s);", (username, email, password))
        flash('Registered Successfully. Please login.', 'success')
        return redirect(url_for('login'))
    flash('Passwords do not match.', 'danger')
    return render_template('register.html', form=form)


@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']
        cur.execute("SELECT * FROM users WHERE username = %s;", username)
        result = cur.fetchone()
        if result:
            # Get stored has
            password = result[3]
            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                flash('Successfully Logged In', 'success')
                return redirect(url_for('index'))
            else:
                flash('Wrong Password.', 'danger')
        else:
            flash('Wrong Username.', 'danger')
    return render_template('login.html')


if __name__ == "__main__":
    app.secret_key="123"
    app.run(debug=True)
    print("Server is running...")
    # db.create_all()
    # db.engine.execute("insert into user(username, email, password, if_admin) values('haoen110', 'haoen110@163.com', '123456', 1);")
    # result = db.engine.execute('select * from user;')
    # for row in result:
    #     print(row)