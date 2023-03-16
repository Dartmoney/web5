from flask import Flask
from data import db_session
from data.user import User
from data.jobs import Job
from datetime import datetime
from flask import render_template

db_session.global_init("db/blogs.db")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
@app.route("/index")
def index():
    db_sess = db_session.create_session()
    job = db_sess.query(Job)
    return render_template("proud.html", job=job)


def main():
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
