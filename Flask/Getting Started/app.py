## Create a simple flask applicatio
from flask import Flask,render_template,request,redirect,url_for
## create the flask app

app=Flask(__name__)

@app.route('/')
def home():
    return "<h2>Hello, World!</h2>"

@app.route('/welcome')
def welcome():
    return "Welcome to the Flask Tutorials"


@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("user",name="Himani"))

@app.route('/success/<int:score>')
def success(score):
    return "the person is passed and the score is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the score is "+str(score)




if __name__=='__main__':
    app.run(debug=True)

