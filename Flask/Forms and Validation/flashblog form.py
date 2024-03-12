from flask import Flask,render_template,url_for,flash,redirect
from form import RegistrationForm,LoginForm
app=Flask(__name__)

#dummy data
#list of dictionaries
app.config['SECRET_KEY']='ed7243d4c0930ea1ebf3e091d1083909'


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

@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)



@app.route("/login")
def login():
    form=LoginForm()
    return render_template('login.html',title='Login',form=form)

if __name__=="__main__":
    app.run(debug=True)