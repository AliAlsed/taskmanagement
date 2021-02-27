from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# url of database //username:passwd@host/database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/tasks"

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    taskname = db.Column(db.String(80), unique=True, nullable=False)
    member = db.relationship('Employee', uselist=False, backref='task')
    duedate = db.Column(db.String(120),nullable=False)

class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
    taskname = db.Column(db.String(80), unique=True, nullable=False)

db.create_all()
@app.route('/')
def hello_world():
    return render_template('first.html')


if __name__ == '__main__':
    app.run(debug=True,port=3000)
