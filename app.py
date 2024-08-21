from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class blogs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(80), unique=False, nullable=False)
    Text = db.Column(db.String(10000), unique=False, nullable=False)
    Image_link = db.Column(db.String(1000), unique=False, nullable=False)

with app.app_context():
    db.create_all()



@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/Blogs",methods=["GET", "POST"])
def all_blogs():
    title = request.form.get('title')
    text = request.form.get('text')
    image = request.form.get('image')
    new_title = blogs(Title=title, Text=text, Image_link=image)
    db.session.add(new_title)
    db.session.commit()
    blog_new = blogs.query.all()
    return render_template("Blogs.html", blog_new=blog_new)

@app.route("/inv/<int:blogs_id>")
def inv(blogs_id):
    blog_new = blogs.query.get(blogs_id)
    db.session.commit()
    return render_template("inv.html", blog_new=blog_new)