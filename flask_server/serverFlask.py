import csv,datetime
from flask import Flask
from flask import render_template,request,redirect,send_file
from operator import itemgetter, attrgetter

app = Flask(__name__)
app.secret_key = 'development key'
password = 'nnhs3061'

@app.route('/')
@app.route('/form', methods = ["POST","GET"])
def enterData():
    if request.method == 'POST':
        if request.form['btn'] == "Submit Form":
            with open('scoutingData.csv','a',newline = '') as csvFile:
                values = [request.form["matchNumber"],request.form["teamNumber"],request.form["points"],request.form["comments"]]
                writer = csv.writer(csvFile,delimiter= ',')
                writer.writerow(values)
                return redirect('/submitted')
    return render_template("dataform.html")

@app.route('/submitted',methods = ["POST","GET"])
def submitted():
    if request.method == 'POST':
        return redirect('/form')
    return render_template("submitted.html")

def getCSVData():
    csvData = []
    with open('scoutingData.csv') as csvFile:
        reader = csv.reader(csvFile,delimiter=",")
        for row in reader:
            csvData.append(row)
    return csvData
def clearCSVData():
    csv_headings = []
    with open('scoutingData.csv') as csvFile:
        reader = csv.reader(csvFile,delimiter=",")
        csv_headings = next(reader)
    open('scoutingData.csv', 'w').close()
    with open('scoutingData.csv', 'a',newline='') as csvFile:
        writer = csv.writer(csvFile,delimiter=',')
        writer.writerow(csv_headings)

@app.route('/clear',methods=["POST","GET"])
def clear():
    if request.method =="POST":
        if request.form['btn'] == "Enter Password":
            if request.form['password'] == password:
                clearCSVData()
        return redirect('/master')
    return render_template("clear.html")

@app.route('/master', methods = ["POST","GET"])
def master():
    if request.method == 'POST':
        if request.form['btn'] == "Clear":
            return redirect('/clear')
        elif request.form['btn'] == "Download CSV":
            now = datetime.datetime.now()
            fileName = "scoutingData"+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+".csv"
            return send_file('scoutingData.csv',mimetype='text/csv',attachment_filename=fileName, as_attachment=True)
        elif request.form['btn'] == "Sort by Team Number":
            sortedData = sorted(getCSVData()[1:], key=itemgetter(1))
            sortedData.insert(0,getCSVData()[0])
            return render_template("master.html",csvData = sortedData )
        elif request.form['btn'] == "Sort by Match Number":
            sortedData = sorted(getCSVData()[1:], key=itemgetter(0))
            sortedData.insert(0,getCSVData()[0])
            return render_template("master.html",csvData = sortedData )
    return render_template("master.html",csvData = getCSVData())

if __name__ == "__main__":
    app.run()
