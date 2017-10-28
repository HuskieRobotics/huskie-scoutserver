#Hey Gavin
#first install python 3 on ur computer
#then install pip3
#then run sudo pip install flask
#now you can run this file by using: python3 serverFlask.py
#to access the website use 127.0.0.1:5000 and follow the instructions

import csv
from flask import Flask
from flask import render_template,request,redirect
#from formthing import ContactForm

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/')
@app.route('/form', methods = ["POST","GET"])
def enterData():
    if request.method == 'POST':
        with open('scoutingData.csv','a',newline = '') as f:
            writer = csv.writer(f,delimiter= ',')
            writer.writerow([request.form['lastname'],request.form['firstname']])
            return redirect('/other')
    return render_template("webform.html")

@app.route('/other',methods = ["POST","GET"])
def other():
    if request.method == 'POST':
        return redirect('/form')
    return render_template("other.html")
if __name__ == "__main__":
    app.run()
