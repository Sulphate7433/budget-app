from flask import Flask, render_template
from database import engine
import pandas as pd

# Create a flask application
app = Flask(__name__)

# Loadable query
def load_db(query):
  with engine.connect() as connection:
      df = pd.read_sql(query, connection)
  return df


# Creating a route to the homepage 'wepage.com/'
@app.route('/')
def home():
  return render_template('home.html')
  
@app.route('/budgetapp/')
def budgetapp():
    data = pd.DataFrame(load_db('SELECT * FROM [SalesLT].[SalesOrderDetail]'))
    results = {"data": [data.to_html().replace('\n','')]}
    return render_template('budgetapp.html',results_dict=results)

@app.route('/login/')
def login():
    return render_template('login.html')

# Runnning the app if the file is run directly
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
