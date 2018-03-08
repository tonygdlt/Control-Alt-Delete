from flask import Flask, request, render_template
import MySQLdb

app = Flask(__name__)

@app.route("/")
def hello():
    db = MySQLdb.connect(host="localhost",  # your host 
        user="root",       # username
        passwd="password",     # password
        db="topscores")   # name of the database
 
    # Create a Cursor object to execute queries.
    cur = db.cursor()
 
    # Select data from table using SQL query.
    cur.execute("""SELECT * FROM win""")

    scores = []
    for row in cur.fetchall() :
        scores.append({row[1] : row[2]});

    for i in scores:
        print i

    db.close()

    #print data['name']
    #print data['score']
    return render_template('index.html', scores=scores)

@app.route('/add', methods=['POST'])
def parse_request():
    data = request.get_json()
    db = MySQLdb.connect(host="localhost",  # your host 
        user="root",       # username
        passwd="password",     # password
        db="topscores")   # name of the database
 
    # Create a Cursor object to execute queries.
    cur = db.cursor()
 
    # Select data from table using SQL query.
    cur.execute("""INSERT INTO win(name,moves) VALUES (%s,%s)""",(data['name'],data['score']))
    db.commit()
    db.close()

    #print data['name']
    #print data['score']
    return ''

if __name__ == '__main__':
    app.run(debug=True)