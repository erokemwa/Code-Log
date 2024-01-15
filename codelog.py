from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Eric Okemwa',
        'title': 'Code Log',
        'content': 'First post content',
        'date_posted': 'January 15, 2018'
    },
    {
        'author': 'Peter White',
        'title': 'Code Log 2',
        'content': 'Second post content',
        'date_posted': 'January 15, 2023'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)