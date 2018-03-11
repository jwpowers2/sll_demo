# on index() see if variable stock_queue exists, if not 
# create stock_list from StockList and run add_stocks, run begin rotator

from flask import Flask, render_template, request, redirect,flash,session 
import re
import atexit
import csv
import time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from collections import deque

app = Flask(__name__)    
app.secret_key = "secret"

STOCKS = [['GOOGL', 'Alphabet', '1100'],
          ['GE', 'General Electric', '14.5'],
          ['AMZN', 'Amazon', '1500'],
          ['TSLA', 'Tesla', '333'],
          ['TXT', 'Textron', '59'],
          ['F', 'Ford', '10'],
          ['BABA', 'Alibaba', '190'],
          ['F5', 'F5 networks', '50']]

d = deque()
input_file = csv.DictReader(open("nasdaq.csv"))
for row in input_file:
    d.appendleft(row)

def rotate_queue():
    d.rotate(1) 

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=rotate_queue,
    trigger=IntervalTrigger(seconds=5),
    id='rotate queue',
    name='rotate last in stock queue to first',
    replace_existing=True)

atexit.register(lambda: scheduler.shutdown())



@app.route('/', methods=['GET'])          

def index():
  if 'status' not in session:
      session['message'] = ""
   
  return render_template('index.html',one=[d[0]['Symbol'],d[0]['Name']],
				      two=[d[1]['Symbol'],d[1]['Name']],          
				      three=[d[2]['Symbol'],d[2]['Name']],          
				      four=[d[3]['Symbol'],d[3]['Name']],          
				      five=[d[4]['Symbol'],d[4]['Name']])          
                         
@app.route('/stock', methods=['POST'])          

def stock():

  if re.search("\W",request.form['stock']):
      flash("Not a valid stock symbol")
      return redirect("/")


  if len(request.form['stock']) < 1:
      flash("Stock symbol blank")
      return redirect("/")

  return redirect("/")

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)      

