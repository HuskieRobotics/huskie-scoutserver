#Hey Gavin
#first install python 3 on ur computer
#then install pip3
#then run sudo pip install flask
#now you can run this file by using: python3 serverFlask.py
#to access the website use 127.0.0.1:5000 and follow the instructions


from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """This is the home page\n\t Please add a /form to the url to get to the scouting form"""

@app.route('/form')
def enterData():
    return render_template("webform.html")


if __name__ == "__main__":
    app.run()