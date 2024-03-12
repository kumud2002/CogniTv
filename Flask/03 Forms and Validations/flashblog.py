from flask import Flask,render_template,url_for
app=Flask(__name__)

#dummy data
#list of dictionaries

posts=[#dictionary1
    {'author' : 'Corey Schaef',
        'title': 'Blog Post1',
        'content' : 'First Post Content',
        'Date_posted' : 'April 20,2018'},
       #dictionary2
        {
        'author' : 'Jane Doe',
        'title': 'Blog Post2',
        'content' : 'Second Post Content',
        'Date_posted' : 'April 20,2020'
        }
        ]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title='AboutPage')

if __name__=="__main__":
    app.run(debug=True)