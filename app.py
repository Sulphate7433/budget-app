from flask import Flask, render_template
from database import engine
import pandas as pd
from pretty_html_table import build_table

# Create a flask application
app = Flask(__name__)

# Loadable query
def load_db(query):
  with engine.connect() as connection:
      df = pd.read_sql(query, connection)
  return df

accounts_query = '''SELECT a.[Accounts]
      ,a.[ID]
      ,a.[Type]
      ,a.[Interest_Rate]
      ,a.[Grace_Period]
      ,a.[Starting_Balance]
	  ,SUM(t.Debits) as 'Debits'
	  ,SUM(t.Credits) as 'Credits'
	  ,a.Starting_Balance + SUM(t.Debits) - SUM(t.Credits) AS 'Current Balance'
  FROM [dbo].[Accounts] a
  LEFT JOIN dbo.Transactions t ON a.Accounts = t.Account 

  GROUP BY a.[Accounts]
      ,a.[ID]
      ,a.[Type]
      ,a.[Interest_Rate]
      ,a.[Grace_Period]
      ,a.[Starting_Balance]

   ORDER BY [Type], [Current Balance] DESC'''

# Creating a route to the homepage 'wepage.com/'
@app.route('/')
def home():
  return render_template('home.html')
  
@app.route('/budgetapp/')
def budgetapp():
    transactions = pd.DataFrame(load_db('SELECT * FROM [dbo].[Transactions] ORDER BY DATE ASC'))
    accounts = pd.DataFrame(load_db(accounts_query))
    results = {"transactions": [build_table(transactions,'grey_dark')],
               "accounts":[build_table(accounts,'grey_dark')]}
    return render_template('budgetapp.html',results_dict=results)

@app.route('/login/')
def login():
    return render_template('login.html')

# Runnning the app if the file is run directly
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
