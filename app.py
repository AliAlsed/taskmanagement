from flask import Flask,render_template,request, redirect , url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# url of database //username:passwd@host/database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/tasks"

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    taskname = db.Column(db.String(80), unique=True, nullable=False)
    leader =  db.Column(db.String(80), nullable=False)

    # status = db.relationship('Employee', uselist=False, backref='task')
    status = db.Column(db.String(80),  nullable=False)
    event = db.Column(db.String(80),  nullable=False)
    # duedate = db.Column(db.String(120),nullable=False)

# class Employee(db.Model):
#     __tablename__ = 'employee'
#     id = db.Column(db.Integer, primary_key=True)
#     task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
#     taskname = db.Column(db.String(80), unique=True, nullable=False)

db.create_all()
@app.route('/', methods=['GET','POST'])
def admin():
    if request.method == 'POST':
        task = request.form['task']
        leader = request.form['leader']
        status = request.form['status']
        event = request.form['event']

        # CURRENCY = request.form['']
        task = Task(taskname=task,leader=leader,status=status,event=event )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('admin'))
    tasks = Task.query.all()
    if tasks != None:
        return render_template('dash.html',tasklist = tasks)
    else:
        return render_template('dash.html')
@app.route('/admin/task/delete/<id>')
def deletetask(id):
    #remove task using task id
    Task.query.filter_by(id=id).delete()
    # commit using to perform query to database
    db.session.commit()
    return redirect(url_for('admin'))
@app.route('/admin/task/edit/<id>')
def edittask(id):
    #remove task using task id
    Task.query.filter_by(id=id).delete()
    # commit using to perform query to database
    db.session.commit()
    return redirect(url_for('admin'))
@app.route('/admin/signin')
def login():
    return render_template('dashboard/login.html')

if __name__ == '__main__':
    app.run(debug=True,port=3000)
