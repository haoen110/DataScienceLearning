from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, flash, request, redirect, url_for, logging, session
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__)
# Config MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Howie1996925@127.0.0.1/sdsc5003'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
db = SQLAlchemy(app)
connection = db.engine.raw_connection()
cur = connection.cursor()


class RegisterForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [validators.DataRequired(),
                                          validators.EqualTo('confirm', message='Passwords do not match.')])
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
        result = cur.fetchone()
        if result is not None:
            flash('Username Existed.', 'danger')
            return render_template('register.html', form=form)
        db.engine.execute("INSERT INTO users(username, email, password) VALUES(%s, %s, %s);",
                          (username, email, password))
        flash('Registered Successfully. Please login.', 'success')
        return redirect(url_for('login'))
    # else:
    #     flash('Passwords do not match.', 'danger')
    return render_template('register.html', form=form)


@app.route('/', methods=['GET', 'POST'])
def login():
    session['logged_in'] = False
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']
        cur.execute("SELECT * FROM users WHERE username = %s;", username)
        result = cur.fetchone()
        print(result)
        if result is not None:
            # Get stored has
            password = result[3]
            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                session['logged_in'] = True
                session['username'] = username
                return redirect(url_for('index'))
            else:
                flash('Wrong Password.', 'danger')
        else:
            flash('Wrong Username.', 'danger')
    return render_template('login.html')


@app.route('/forgot-password.html')
def forgot_password():
    return render_template('forgot-password.html')


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session['logged_in']:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please Login!', 'danger')
            return redirect(url_for('login'))
    return wrap


@app.route('/index.html')
@is_logged_in
def index():
    return render_template('index.html')


# Article Form Class
class ArticleForm(Form):
    title = StringField('Title', [validators.Length(min=1)])
    body = TextAreaField('Body', [validators.Length(min=1)])


@app.route('/table1.html', methods=['GET', 'POST'])
@is_logged_in
def table1():
    cur = db.engine.raw_connection().cursor()
    cur.execute("SELECT * FROM articles;")
    articles = cur.fetchall()
    return render_template('table1.html', articles=articles)

@app.route('/add_article', methods=['POST'])
@is_logged_in
def add_article():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data
        db.engine.execute("INSERT INTO articles(title, body, transactor) VALUES (%s, %s, %s)",
                    (title, body, session['username']))
        flash('Insert Successfully!', 'success')
        return redirect(url_for('table1'))
    return render_template('table1.html', form=form)

@app.route('/table1.html/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def delete_article(id):
    if request.method == 'POST':
        db.engine.execute("DELETE FROM articles WHERE id = %s", [id])
        flash('Delete Successfully!', 'success')
        return redirect(url_for('table1'))


# @app.route('/charts.html')
# @is_logged_in
# def charts():
#     return render_template('charts.html')

# @app.route('/tables.html')
# @is_logged_in
# def tables():
#     return render_template('tables.html')


if __name__ == "__main__":
    app.secret_key = "123"
    app.run(debug=True)
    print("Server is running...")
    # db.create_all()
    # db.engine.execute("insert into user(username, email, password, if_admin) values('haoen110', 'haoen110@163.com', '123456', 1);")
    # result = db.engine.execute('select * from user;')
    # for row in result:
    # print(row)
