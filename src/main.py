import sqlite3

from models.__all_models import User, App, Label, Button, BoxLayout, TextInput, Widget, db_session, User, \
    GridLayout, AnchorLayout, Window
from couple import Couple

Window.size = (480, 720)
db_session.global_init('sqlite.db')


class Container(BoxLayout):
    def __init__(self):
        super().__init__()
        self.pops = Couple()

    def changeCouple(self):
        self.pops.open()

    def changeGrade(self):
        print(2)

    def updates(self):
        firsts = 'Понедельник\n'
        seconds = 'Вторник\n'
        thirds = 'Среда\n'
        fourths = 'Четверг\n'
        fifths = 'Пятница\n'
        sixths = 'Суббота\n'

        conn = sqlite3.connect('sqlite.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM couples;")
        results = cur.fetchmany(6)
        for i in results:
            if i[0] == 1:
                num = 1
                for j in i:
                    if j != 1:
                        firsts += ''.join(str(num) + '- ' + str(j) + '\n')
                        num += 1
            elif i[0] == 2:
                num = 1
                for j in i:
                    if j != 2:
                        seconds += ''.join(str(num) + '- ' + str(j) + '\n')
                        num += 1
            elif i[0] == 3:
                num = 1
                for j in i:
                    if j != 3:
                        thirds += ''.join(str(num) + '- ' + str(j) + '\n')
                        num += 1
            elif i[0] == 4:
                num = 1
                for j in i:
                    if j != 4:
                        fourths += ''.join(str(num) + '- ' + str(j) + '\n')
                        num += 1
            elif i[0] == 5:
                num = 1
                for j in i:
                    if j != 5:
                        fifths += ''.join(str(num) + '- ' + str(j) + '\n')
                        num += 1
            elif i[0] == 6:
                num = 1
                for j in i:
                    if j != 6:
                        sixths += ''.join(str(num) + '- ' + str(j) + '\n')
                        num += 1

        self.couple1.text = firsts
        self.couple2.text = seconds
        self.couple3.text = thirds
        self.couple4.text = fourths
        self.couple5.text = fifths
        self.couple6.text = sixths


class MainApp(App, Widget):
    def build(self):
        return Container()


if __name__ in ('__main__', '__android__'):
    MainApp().run()
