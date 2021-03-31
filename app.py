from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import pyodbc 


app = Flask(__name__)
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-5OJ0R1H\SQLEXPRESS;'
                      'Database=student;'
                      'Trusted_Connection=yes;')
cur = conn.cursor()
app.secret_key = 'many random bytes'

#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'DESKTOP-5OJ0R1H\12499'
#app.config['MYSQL_PASSWORD'] = ''
#app.config['MYSQL_DB'] = 'student'

#mysql = MySQL(app)


@app.route('/')
def Index():
   # cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM student.dbo.student_info")
    data = cur.fetchall()
   # cur.close()
    return render_template('index2.html', record=data )



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        student_id = request.form['student_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        amount_due = request.form['amount_due']
        #cur = mysql.connection.cursor()
        cur.execute("INSERT INTO student.dbo.student_info VALUES (?,?,?,?,?)", (student_id, first_name, last_name, dob, amount_due))
        conn.commit()
        return redirect(url_for('Index'))




@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    #cur = mysql.connection.cursor()
    cur.execute("DELETE FROM dbo.student_info WHERE student_id=?", (id_data,))
    #mysql.connection.commit()
    conn.commit()
    return redirect(url_for('Index'))





@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['student_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        amount_due = request.form['amount_due']
        #cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE dbo.student_info
               SET first_name=?, last_name=?, dob=?, amount_due=?
               WHERE student_id=?
            """, (first_name, last_name, dob, amount_due, id_data))
        flash("Data Updated Successfully")
        conn.commit()
        return redirect(url_for('Index'))









if __name__ == "__main__":
    app.run(debug=True)