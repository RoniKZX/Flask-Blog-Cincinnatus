from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '2dab6e03ed72c36217d09d9c7dfca09a'

posts = [
    {
        'author': "Winter Fell",
        'title': "Blog Post 1",
        'content': "First post content",
        'date_posted': "December 10, 2023"
    },
    {
        'author': "Summer Ends",
        'title': "Blog Post 2",
        'content': "Second post content",
        'date_posted': "October 10, 2022"
    },
    {
        'author': "Autumn Noon",
        'title': "Blog Post 3",
        'content': "Third post content",
        'date_posted': "April 9, 2020"
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = RegistrationForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run()
