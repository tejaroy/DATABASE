from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import migrate,Migrate
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///teja.db'

db=SQLAlchemy(app)

migrate=Migrate(db,app)


#models
class All(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(25),unique=True,nullable=False)
    last_name=db.Column(db.String(25),unique=True,nullable=False)
    username=db.Column(db.String(25),unique=True,nullable=False)
    age=db.Column(db.Integer,nullable=False)
    phonenumber=db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f"Name:{self.first_name},Age:{self.age}"


@app.route('/')
def index():
    all=All.query.all()
    return render_template('index.html',all=all)


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/add',methods=['POST'])
def profile():
    first_name=request.form.get("first_name")
    last_name=request.form.get("last_name")
    username=request.form.get('username')
    age=request.form.get('age')
    phonenumber=request.form.get('phonenumber')

    if first_name!=" " and last_name!=" " and username!=" " and age is not None and phonenumber is not None:
        p=All(first_name=first_name,last_name=last_name,username=username,age=age,phonenumber=phonenumber)
        db.session.add(p)
        db.session.commit()
        return redirect('/')
    else:
        return redirect('/')






if __name__=='__main__':
    app.run(debug=True)