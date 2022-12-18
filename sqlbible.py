import sqlite3
from bottle import request, route, run


def select_all():
    conn = sqlite3.connect('phones.db')

    select = conn.cursor()

    select.execute("SELECT * FROM users;")
    res = select.fetchall()
    data = ""
    for row in res:
        data = data + "ID: " + str(row[0]) + \
               "<br>First Name: " + str(row[1]) + \
               "<br>Last Name: " + str(row[2]) + \
               "<br>Address: " + str(row[3]) + \
               "<br>Phone Number: " + str(row[4]) + \
               "<br>============================<br>"
    select.close()
    return "<form action='/select_all' method = 'post'>" \
           "<input  type = 'submit' name = 'back' value = 'Back'></form>" + data


def start_menu():
    data = "1 - Показать всю базу данных" \
           "<br> 2 - Фильтрация"
    return data + '''<br><br>
        <form action="/start_menu" method="post">
            Выбор: <input name="choose" type="text" />
            <input value="Ok" type="submit" />
        </form>
        '''


def filtr():
        return '''<br>
        <form action="/filtr" method="post">
            ID:         <br><input name="choose_id" type="text" /><br>
            <br>First name: <br><input name="choose_fname" type="text" /><br>
            <br>Last name:  <br><input name="choose_lname" type="text" /><br>
            <br>Address:    <br><input name="choose_adr" type="text" /><br>
            <br>Phone:      <br><input name="choose_phone" type="text" /><br>
            <br><input value="Ok" type="submit"> <input type = "submit" name = "back" value = "Back">
        </form>
        '''


def filtr_name(id, fname, lname, phone, adr):
    conn = sqlite3.connect('phones.db')
    select = conn.cursor()
    select.execute("SELECT * FROM users where userid like '" + id + "%' and firstname like '" + fname + "%'"
                    "and lastname like '" + lname + "%'"
                    "and address like '" + adr + "%'"
                    "and phone like '" + phone + "%';")
    res = select.fetchall()
    data = ""
    for row in res:
        data = data + "ID: " + str(row[0]) + \
               "<br>First Name: " + str(row[1]) + \
               "<br>Last Name: " + str(row[2]) + \
               "<br>Address: " + str(row[3]) + \
               "<br>Phone Number: " + str(row[4]) + \
               "<br>============================<br>"
    select.close()
    if len(data) == 0:
        return filtr() + '<br>No results'
    else:
        return filtr() + data
