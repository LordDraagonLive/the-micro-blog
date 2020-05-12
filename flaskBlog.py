from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author':'some name',
        'title':'first post',
        'content':'first post here',
        'date_posted':'12/01/2020'
    },
     {
        'author':'some other name',
        'title':'Third post',
        'content':'first post here',
        'date_posted':'03/01/2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')



if __name__ == '__main__':
    app.run(debug=True)