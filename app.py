from flask import Flask

app = Flask(__name__)                     # Create a flask application

@app.route('/')                           # Creating a route to the homepage 'wepage.com/'

def hello_world():                        # Creating a function
    return '<p>Hello, World!</p>'


if __name__ == '__main__':                # Runnning the app if the file is run directly
    app.run(host='0.0.0.0',debug=True)