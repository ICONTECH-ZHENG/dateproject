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
           print(outputDay)
    
        elif outputDay == 1:
             outputDay="Tuesday"
             print(outputDay)
        
        elif outputDay == 2:
             outputDay="Wednesday"
             print(outputDay)
        
        elif outputDay == 3:
             outputDay="Thursday"
             print(outputDay)
    
        elif outputDay == 4:
             outputDay="Friday"
             print(outputDay)
        
        elif outputDay == 5:
             outputDay="Saturday"
             print(outputDay)
        
        else:
            outputDay="Sunday"
            print(outputDay)
    else:
        inputDate = " "
    return render_template("index.html",
                           inputDate = inputDate,
                           outputDay = outputDay,
                           pageTitle="Day of The Week Calculator")

