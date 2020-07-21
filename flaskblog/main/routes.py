from flask import render_template, request, Blueprint
from flaskblog.models import Post


main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    # posts = Post.query.all()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5) # order desc order of date
    return render_template('home.html', posts=posts)


@main.route('/about')
def about():
    return render_template('about.html', title='About')



