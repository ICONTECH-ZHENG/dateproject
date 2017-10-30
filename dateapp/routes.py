from . import app
import datetime
from flask import request
from flask import render_template
from dateapp import app



@app.route('/', methods=['Get'])
def index():
    inputDate = None
    outputDay = None
    if request.args:
        inputDate = request.args.get('datetime')
    if inputDate:
        day = str(inputDate)
        month, day, year = (int(x) for x in day.split('/'))
        outputDay = datetime.date(year, month, day).weekday()
        if outputDay == 0:
            outputDay="Monday"
        elif outputDay == 1:
            outputDay="Tuesday"
        elif outputDay == 2:
            outputDay="Wednesday"
        elif outputDay == 3:
            outputDay="Thursday"
        elif outputDay == 4:
            outputDay="Friday"
        elif outputDay == 5:
            outputDay="Saturday"
        else:
            outputDay="Sunday"

    else:
        inputDate = "Please Submit A Date!"
    return render_template("index.html",
                           inputDate = inputDate,
                           outputDay = outputDay,
                           pageTitle="Day of The Week Calculator")

