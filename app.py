from flask import Flask, render_template

# Create a flask application
app = Flask(__name__)


# Creating a route to the homepage 'wepage.com/'
@app.route('/')
def home():
  return render_template('home.html')
  
@app.route('/budgetapp/')
def budgetapp():
    return render_template('budgetapp.html')
  
@app.route('/login/')
def login():
    return render_template('login.html')

# Runnning the app if the file is run directly
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
