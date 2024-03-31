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

    captain = User(surname='Scott', name='Ridley', age=21, position='captain', speciality='research engineer',
                   address='module_1', email='scott_chief@mars.org')
    db_sess.add(captain)

    cabin_boy = User(surname='Ohlopkov', name='Nikita', age=16, position='cleaner', speciality='general education',
                     address='module_2', email='Ohlopkov228@gmail.com')
    db_sess.add(cabin_boy)

    pilot = User(surname='Kurlov', name='Artem', age=17, position='pilot', speciality='high education',
                 address='module_2', email='secret_mail@mail.ru')
    db_sess.add(pilot)

    passenger = User(surname='Zharnikov', name='Fedor', age=17, position='passenger', speciality='idiot',
                     address='module_3', email='iamFedya@gmail.com')
    db_sess.add(passenger)

    db_sess.commit()


if __name__ == '__main__':
    main()
