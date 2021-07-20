import sqlite3

from kivy.core.window import Window
from models.__all_models import Popup, User, db_session, Button, Label, BoxLayout, App

Window.size = (480, 720)
db_session.global_init('sqlite.db')
close = None


class Couple(Popup):
    def __init__(self):
        super().__init__()
        self.title = "Введите новое раписание:"

    def build(self):
        pass

    def changeCouples(self):
        conn = sqlite3.connect('sqlite.db')
        c = conn.cursor()
        c.execute('DELETE FROM couples;')
        conn.commit()
        conn.close()

        self.firstdef()
        self.seconddef()
        self.thirdef()
        self.fourthdef()
        self.fifthtdef()
        self.sixthdef()

    def firstdef(self):
        a = (self.text_in_couple1.text).split(sep="\n")[1:]
        days = [i.split('-')[1] for i in a]

        session = db_session.create_session()
        user = User(
            first=days[0],
            second=days[1],
            third=days[2],
            fourth=days[3],
            fifth=days[4],
            sixth=days[5]
        )
        session.add(user)
        session.commit()

    def seconddef(self):
        a = (self.text_in_couple2.text).split(sep="\n")[1:]
        days = [i.split('-')[1] for i in a]

        session = db_session.create_session()
        user = User(
            first=days[0],
            second=days[1],
            third=days[2],
            fourth=days[3],
            fifth=days[4],
            sixth=days[5]
        )
        session.add(user)
        session.commit()

    def thirdef(self):
        a = (self.text_in_couple3.text).split(sep="\n")[1:]
        days = [i.split('-')[1] for i in a]

        session = db_session.create_session()
        user = User(
            first=days[0],
            second=days[1],
            third=days[2],
            fourth=days[3],
            fifth=days[4],
            sixth=days[5]
        )
        session.add(user)
        session.commit()

    def fourthdef(self):
        a = (self.text_in_couple4.text).split(sep="\n")[1:]
        days = [i.split('-')[1] for i in a]

        session = db_session.create_session()
        user = User(
            first=days[0],
            second=days[1],
            third=days[2],
            fourth=days[3],
            fifth=days[4],
            sixth=days[5]
        )
        session.add(user)
        session.commit()

    def fifthtdef(self):
        a = (self.text_in_couple5.text).split(sep="\n")[1:]
        days = [i.split('-')[1] for i in a]

        session = db_session.create_session()
        user = User(
            first=days[0],
            second=days[1],
            third=days[2],
            fourth=days[3],
            fifth=days[4],
            sixth=days[5]
        )
        session.add(user)
        session.commit()

    def sixthdef(self):
        a = (self.text_in_couple6.text).split(sep="\n")[1:]
        days = [i.split('-')[1] for i in a]

        session = db_session.create_session()
        user = User(
            first=days[0],
            second=days[1],
            third=days[2],
            fourth=days[3],
            fifth=days[4],
            sixth=days[5]
        )
        session.add(user)
        session.commit()
