from flask import Flask, render_template

app = Flask(__name__)

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
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()