from flask import Flask, render_template, url_for, request
import psycopg2

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=['GET','POST'] )
def login():
    if request.method == 'GET':        
        return f"""
        Method GET
        <h1>Hello Dear, {request.args.get('uname')}</h1>
        <h2>Successfully Signup with {request.args.get('email')}</h2>
        """
    elif request.method == 'POST':
        return f"""
        Method POST
        {connect(request.form['uname'], request.form['psw'] )}       
        
        """    

def connect(uname, pwd):
    """ Connect to the PostgreSQL database server """
    conn = None
    email = ''
    try:
        # read connection parameters
        # params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
        host="ec2-3-227-68-43.compute-1.amazonaws.com",
        database="d3a7ul7391rt0c",
        user="cacshabpfxwzxh",
        password="ae8e8579d0c5b2285ff4d8a95b4ae249f850a279998bbe445cd13b125439b2dc")
		
        # create a cursor
        cur = conn.cursor()
        
	    # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        
        cmd = f"""SELECT * FROM persons\n
    WHERE username='{uname}' AND password='{pwd}';"""
        cur.execute(cmd)        
        for db in cur:
            print(db) 
            email =  db[2]  
        if email:       
            reply = f"""
        <h1> Hello Dear, {uname}</h1>
        <h2> Your registered email id is: {email}</h2>
        <h0> Successfully logged in </h2>"""
        else:
            reply = f"""
        <h1> Failed to login with given credential combination {uname} </h1>
        <h2> Please try again </h2>
        """
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        reply = """
    <h1> Database Error detected </h1>
    """
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    
    return reply


app.run(debug=True)    
