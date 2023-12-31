from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/process'  ,methods = ["POST"])
def process():
    page = ""
    form = request.form
    if form["kleur"] == "rood":
        page+= "You picked Red"
    elif form["kleur"] == "blauw":
        page+= "You picked blauw"
    elif form["kleur"] == "groen":
        page+= f"You picked {form['kleur']}"
    return page

@app.route('/index')
def index():
    page = """<!DOCTYPE html>
<html lang = "en">

<head>
    <meta charset="utf-8">
    <meta name = "viewport" content = "width=device-width">
    <title>Linktree</title>   
    <link href="static/css/75.css" rel="stylesheet" type="text/css"/>
</head>

<body>

    <form method="post" action="/process">

                <p>Username: <input type="text" name = "username" required></p>

                <p>Email: <input type="Email" name = "email" required ></p>

                <p>Password: <input type="Password" name = "password" required></p>

                    <input type="hidden" name="userID" value="232">

                <p>Fav Color: <select name="kleur" id="test">  DROPDOWN MENU
                                    <option value="rood">rood</option>
                                    <option value="blauw">blauw</option>
                                    <option value="groen">groen</option>
                             </select></p> 


                <button type="submit">Login</button>

    </form>

</body>"""
    return page

app.run(host = '0.0.0.0', port=81)