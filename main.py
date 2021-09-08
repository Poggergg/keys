from quart import Quart, redirect, render_template, request
import json
import os
from replit import db
from threading import Thread
from key_gen import assigner
import pyston
w_logs = []
app = Quart('app')

def user(value):
    if value == "KNDoSWe6U":
      return"Iron"
    elif value == "WvpIRvrjw":
      return "Phil"
    elif value == "meUbsGekh":
      return "Verrus"
    elif value == "g9fgLzaxh":
      return "Chiko"
    elif value == "mJkHzJeSu":
      return "Ally"
    elif value == "oBLv6BCPx":
      return "Mike"
    elif value == "sRPfQOKZ1":
      return "Rave"
    elif value == "cAiq4v8Es":
      return "Emily"
    elif value == "yA9WrgNHJ":
      return "Adam"
    elif value == "vk6KmL1bi":
      return "Kun"
    elif value == "avwuaPvEp":
      return "Lime"
    elif value == "a5WUsoDWm":
      return "Sam"
    elif value == "pWKi3MDXr":
      return "Lemon"
    elif value == "iudghQQaF":
      return "Eli"
    elif value == "N0VA":
      return "Nova"
    

key_dict = {'KNDoSWe6U' : "Iron", 'WvpIRvrjw' : "Phil", 'meUbsGekh' : "Verrus",}
#   "Kun": "vk6KmL1bi", 
#   "Lime": "avwuaPvEp", 
#   "Sam": "a5WUsoDWm", 
#   "Lemon": "pWKi3MDXr", 
#   "Eli": "iudghQQaF", 
#   "4162_ADMIN": "7mES3UObM"



@app.route('/home/@<name>')
async def asd(name):

  with open(f"allowedKeys.json", "r") as logs:
    l_logs = json.load(logs)

    key_values = [key for key in l_logs.values()]
    key_name = [key for key in l_logs]

    if name == "7mES3UObM":
      return await render_template('4162_config.json')
      with open("Weblogs.json", "r") as r:
        l_r = json.load(r)
        l_r[f"{user(name)}"] = "Login detected"
      with open("Weblogs.json", "w") as r:
        json.dump(l_r, r)
    if name in key_values:
      print(f"detected key {key_values} {name}")
      return await render_template('the-game.html', name=user(value=name))
  
    else:
      print(f"did not detect key {key_values} {name}")
      return redirect("/")

@app.route('/')
async def ome():
  return db.keys()
  
@app.route('/Data')
async def page():
  return await render_template("data-use.html")



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
      return await render_template("activity.html", name=user(value=text), logs=l_f)

@app.route('/exec')
async def index():
  return await render_template('index.html')

@app.route('/exec', methods=['POST', 'GET'])
async def req():
    if request.method == "POST":
        form = await request.form
        lang = form["lang"].lower().replace(" ", "")
        code = form["code"]

        client = pyston.PystonClient()
        try:

          output = await client.execute(lang, code)
        except:
          return "An error occured."
        return await render_template("index.html", output=output, code=code, lang=lang)

    else:
        return await render_template("index.html")
app.run(host='0.0.0.0',port=8042)