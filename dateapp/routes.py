from . import app
import datetime
from flask import request
from flask import render_template
from dateapp import app


@app.route('/', methods=['GET'])
def index():
    input_date = None
    input_dat= None
    if request.args:
        input_date =request.args.get('datetime')
    if input_dat:
        day = str(input_date)
        month, day, year = (int(x) for x in day.split('/'))
        output_day = datetime.date(year, month, day).weekday()
        if output_day == 0:
            output_day="Monday"
        elif output_day == 1:
            output_day="Tuesday"
        elif output_day == 2:
            output_day="Wednesday"
        elif output_day == 3:
            output_day="Thursday"
        elif output_day == 4:
            output_day="Friday"
        elif output_day == 5:
            output_day="Saturday"
        else:
            output_day="Sunday"
        
     else:
        input_day = "Please submit the date above."
     return render_template("index.html",)
                            input_date = input_date,
                            output_day = output_day,
                            page_title="Day of The Week Calculator")
            
