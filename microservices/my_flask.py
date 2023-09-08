# we may need to pip install flask
# Flask is a microservice that implements a simple web server
# if you need a public-facing server then use Flask with Apache etc. (for security)
# Flask is a lightweight service, it leaves security to others
from flask import Flask

# to make a Flask web server...
app = Flask(__name__) # this is conventional
# we declare 'routes' for our web server (remember web servers talk over HTTP)
@app.route('/') # if anyone arrives at our server tey will be given this outcome
def root():
    return 'Hello and welcome to Flask'
@app.route('/map')
def map():
    return '<h2>Here is a map of Paris in deep snow</h2>'
# we can have multiple ways to access a route
@app.route('/info') # we can handle typos, old links etc.
@app.route('/about')
def about():
    return 'this is info about the stuff'

# we can pass REST parameters (Represent State Transfer)
# e.g. /greet or /greet/Ada or /greet/Ada/Lovelace
@app.route('/greet')
@app.route('/greet/<name>') # the <> indicate a URL parameter
@app.route('/greet/<name>/<sname>')
def greet(name=None, sname=None):
    if name:
        if sname:
            return f'<h3>Greetings {name} {sname}</h3>' # Flask has a micro-syntax
        else:
            return f'<h3>Greetings {name}</h3>'
    else:
        return '<h3>Greetings Earthling<h3>'

# we can build the HTML response
@app.route('/menu')
def menu():
    link1 = '<a href="/">Home</a>'
    link2 = '<a href="/about">About</a>'
    link3 = '<a href="/greet">Greet</a>'
    link4 = '<a href="/map">Map</a>'
    return f'{link1} | {link2} | {link3} | {link4}'

if __name__ == '__main__':
    # debug=True will live reload on changes
    app.run(host='127.0.0.1', debug=True)

