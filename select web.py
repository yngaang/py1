from bottle import route, run, template, request, get, post, Bottle, redirect
import sqlbible

app = Bottle()


@app.route('/start_menu')
def start():
    return sqlbible.start_menu()


@app.post('/start_menu')
def redirected():
    c = request.forms.get("choose")
    if int(c) == 1:
        return redirect("select_all")
    elif int(c) == 2:
        return redirect("filtr")


@app.route('/select_all')
def choose():
    return sqlbible.select_all()


@app.post('/select_all')
def back():
    a = request.forms.get('back')
    if a == "Back":
        return sqlbible.start_menu()


@app.get('/filtr')
def filtr_show():
    return sqlbible.filtr()


@app.post('/filtr')
def choose3():
    if request.forms.get('back') == "Back":
        return sqlbible.start_menu()
    else:
        choose_id = request.forms.get("choose_id")
        choose_fname = request.forms.get("choose_fname")
        choose_lname = request.forms.get("choose_lname")
        choose_phone = request.forms.get("choose_phone")
        choose_address = request.forms.get("choose_adr")
        return sqlbible.filtr_name(choose_id, choose_fname, choose_lname, choose_phone, choose_address)


app.run(host='localhost', port=8080, debug=True)
