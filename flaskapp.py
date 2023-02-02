from flask import *
import sqlite3
app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('/var/www/html/flaskapp/users.db')
    conn.row_factory = sqlite3.Row
    return conn

#print([x['fname'] for x in posts])
@app.route('/',methods=['GET','POST'])
def hello_world():
    if(request.method=='GET'):
        return  render_template('index.html')
    else:
        print("here",request.form)
        
        #o=request.form["signup"]
        #print(request.form["login"])
        if('signup' in request.form.keys()):
            print("inside condition")
            print("values",request.form["fname"])
            fname=request.form["fname"]
            lname=request.form["lname"]
            print("values",request.form["lname"])
            username=request.form["Uname"]
            #username=request.form["Uname"]
            print("values",request.form["Uname"])
            password=request.form["Pass"]
            print("values",request.form["Pass"])
            email=request.form["email"]
            print(request.form["filename"])
            filedata=request.form["filename"]
            filecontent=request.form["filecont"]
            print((lname,fname,email,password,username))
            with sqlite3.connect('/var/www/html/flaskapp/users.db') as conn:
                print("connected")
                cur=conn.cursor()
                cur.execute("""INSERT INTO users (lname,fname,email,password,username,filename,file_blob) VALUES (?,?,?,?,?,?,?)""",(lname,fname,email,password,username,filedata,filecontent))
                conn.commit()
            conn.close()
            return render_template('message.html',msg=['signedup'])

        else:
            print('in login')
            username=request.form["Uname"]
            #username=request.form["Uname"]
            print("values",request.form["Uname"])
            password=request.form["Pass"]
            print("values",request.form["Pass"])
        
            conn = get_db_connection()
            posts = conn.execute('SELECT * FROM users where username=?',[username]).fetchall()
        #conn.close()
            resp=[]
            for i in posts:
                k={}
                k['userid']=i['userid']
                k['username']=i['username']
                k['password']=i['password']
                k['fname']=i['fname']
                k['lname']=i['lname']
                k['email']=i['email']
                if(not (password ==i['password'] )):
                    return render_template("message.html",msg=["Wrong password ","Authentication Failed"])
                try:
                    k['word_count']=len(i['file_blob'].split(' '))
                except:
                    pass
                resp.append(k)
            print(len(resp))
            conn.close()
            if(len(resp)==0):
                print("here bro")
                return render_template("message.html",msg=["you are not registered ","kindly register"])
            else:
                try:
                    return render_template('submit.html',result=resp,file_cont=i['file_blob'])
                except:
                    return render_template('submit.html',result=resp,file_cont="file not loaded while signup")

@app.route('/countme/<input_str>')
def count_me(input_str):
    return str(len(input_str))
@app.route('/pdf/', methods=['GET', 'POST'])
def download():
    import os
    pdf = os.path.join(current_app.root_path, app.config['pdf'])
    c=[]
    with open("limerick.txt", "r+") as file1:
    # Reading from a file
        c.append(file1.read())
    print(c)
    return send_from_directory(path=pdf, filename='limerick.txt')

if __name__ == '__main__':
  app.run()
