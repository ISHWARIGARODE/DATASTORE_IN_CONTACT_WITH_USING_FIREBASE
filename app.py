from flask import Flask,render_template,request,redirect
import firebase_admin
from firebase_admin import credentials,db

app=Flask(__name__)
cred=credentials.Certificate("C:/Users/Ashish/OneDrive/Desktop/python3.10/ishwari-e06de-firebase-adminsdk-fbsvc-99ad2fa7d1.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred,{"databaseURL":"https://ishwari-e06de-default-rtdb.firebaseio.com/"})

@app.route('/')  
def Home():
    ref=db.reference("/visit")
    ref.push({"page": "Home"})
    return render_template("index.html")

@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method=='POST':
       name=request.form.get('name')
       message=request.form.get('message')
       db.reference('/contact').push({'name':name,'message':message})
       return redirect('/contact')
    else:
        db.reference('/visit').push({'page':'contact'})
        return render_template("contact.html")

@app.route('/about')  
def about():
    ref=db.reference("/visit")
    ref.push({"page": "about"})
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
    