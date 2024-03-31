from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    # app.run()
    db_sess = db_session.create_session()

    captain = db_sess.query(User).filter(User.position == 'captain').first()
    job = Jobs(job='deployment of residential modules 1 and 2', work_size=15, collaborators='2, 3', is_finished=False)
    captain.jobs.append(job)

    db_sess.commit()


if __name__ == '__main__':
    main()
