# on index() see if variable stock_queue exists, if not 
# create stock_list from StockList and run add_stocks, run begin rotator

from flask import Flask, render_template, request, redirect,flash,session 
import re

app = Flask(__name__)    
app.secret_key = "secret"

@app.route('/', methods=['GET'])          

def index():
  if 'status' not in session:
      session['message'] = ""
  return render_template('index.html')          
                         
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

