

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskProject.db'
db=SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    content = db.Column(db.Text, nullable=False)
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/posts')
def posts():
    posts = Post.query.all()


    return render_template('posts.html', posts=posts)





@app.route('/create',methods=['POST','GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']

        post = Post(title=title, content=text)

        try:
            db.session.add(post)

            db.session.commit()
            return redirect(url_for('index'))
        except:
            return 'Something went wrong'


    else:
        return render_template('create.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
