#Hey Gavin
#first install python 3 on ur computer
#then install pip3
#then run sudo pip install flask
#now you can run this file by using: python3 serverFlask.py
#to access the website use 127.0.0.1:5000 and follow the instructions

import csv
from flask import Flask
from flask import render_template,request
#from formthing import ContactForm

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/')
def hello_world():
    return """This is the home page\n\t Please add a /form to the url to get to the scouting form"""

@app.route('/form', methods = ["POST","GET"])
def enterData():
    if request.method == 'POST':
        print("recieved POST")
        with open('scoutingData.csv','w',newline = '') as f:
            writer = csv.writer(f,delimiter= ',')
            print (writer)
            writer.writerow([request.form['lastname'],request.form['firstname']])
        return ("Things happened")
    else:
        return render_template("webform.html")

if __name__ == "__main__":
    app.run()