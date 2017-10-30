from . import app
import datetime
from flask import request
from flask import render_template
from dateapp import app



@app.route('/', methods=['Get'])
def index():
    inputdate = None
    outputday = None
    if request.args:
        inputdate = request.args.get('datetime')
    if inputdate:
        day = str(inputdate)
        month, day, year = (int(x) for x in day.split('/'))
        outputday = datetime.date(year, month, day).weekday()
        if outputday == 0:
            outputday="Monday"
        elif outputday == 1:
            outputday="Tuesday"
        elif outputday == 2:
            outputday="Wednesday"
        elif outputday == 3:
            outputday="Thursday"
        elif outputday == 4:
            outputday="Friday"
        elif outputday == 5:
            outputday="Saturday"
        else:
            outputday="Sunday"

    else:
        inputdate = "Please submit the date above."
    return render_template("index.html",
                           inputdate = inputdate,
                           outputday = outputday,
                           page_title="Day of The Week Calculator")

