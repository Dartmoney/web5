import sqlalchemy
from data.user import User
from data import db_session
from flask import Flask

from flask import Flask

# bd = input()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/blogs.db")
db_sess = db_session.create_session()


class Us(User):
    def __repr__(self):
        return f"{self.id}"


for user in db_sess.query(Us).filter(Us.address.like("%module_1%"), Us.speciality.not_like("%engineer%"),
                                     Us.position.not_like("%engineer%")):
    print(user)
