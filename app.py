from flask import Flask, request, render_template, redirect, url_for, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, User
import os

app = Flask(__name__)
app.secret_key = 'ITSAHACKATHON_ET4_teamnova'  

# Database configuration
DATABASE_URL = "mysql+mysqlconnector://root:ShravaniSJ@localhost/GradeBook"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)
db_session = Session()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        role = request.form['role']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']  
        
        new_user = User(role=role, username=username, email=email, password=password)
        db_session.add(new_user)
        db_session.commit()

        session['user_id'] = new_user.id  

        if new_user.role == 'student':
            return redirect(url_for('student_homepage'))  
        elif new_user.role == 'teacher':
            return redirect(url_for('teacher_homepage'))  

    return render_template('register.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = db_session.query(User).filter_by(username=username).first()
        
        if user and user.password == password: 
            session['user_id'] = user.id

            if user.role == 'student':
                 return redirect(url_for('student_homepage'))  
            elif user.role == 'teacher':
                return redirect(url_for('teacher_homepage'))   
        else:
            return "Invalid credentials, please try again."
    
    return render_template('login.html')

@app.route('/student_homepage')
def student_homepage():
    return render_template('student_homepage.html')

@app.route('/teacher_homepage')
def teacher_homepage():
    return render_template('teacher_homepage.html') 



if __name__ == '__main__':
    app.run(debug=True)

