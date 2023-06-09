from flask import Flask
from data import db_session
from data.user import User
from data.jobs import Job
from datetime import datetime
from flask import render_template
from flask import redirect
from forms.user import RegisterForm

db_session.global_init("db/blogs.db")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
@app.route("/index")
def index():
    db_sess = db_session.create_session()
    job = db_sess.query(Job)
    return render_template("proud.html", job=job)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            surname=form.surname.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


def main():
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
