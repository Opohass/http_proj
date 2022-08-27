import imgConv
import numpy as np
from manDB import dataBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, session
import pickle


app =Flask(__name__)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.secret_key = '12'
app.config['SESSION_TYPE'] = 'filesystem'
#where to save a file if we add this option, now the image uploaded isn't saved
# app.config['UPLOAD_FOLDER']="./" 
# app.config['MAX_CONTENT_PATH']=100

#index route
@app.route("/")
@app.route("/home")
def index():
    if len(session): #if session is established go to the upload page
        return render_template("index.html",answer="XX")
    return render_template("login.html")
  
#when image upload route
@app.route("/upload", methods = ['GET', 'POST'])
def uploaded():
    if len(session) == 0: #securety, only loaded user can enter the page
        return redirect("/login",code=200)
        
    if request.method == 'POST':
        f = request.files['file']

        validExtention='.' in f.filename and f.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
        if f != "" and validExtention:
            f=f.read()
            file_bytes = np.frombuffer(f, np.uint8)
            final1DImage=imgConv.getImageAsArray(file_bytes)
            #TODO: connect the model, insert the prediction into the HTML
            # answer=f"The number You Drew Is: {model.predict([final1DImage])}"
            answer1=f"The number You Drew According To Brute Force Knn Is: {brute.predict([final1DImage])[0]}"
            answer2=f"The number You Drew According To Knn Tree Is: {knnTree.predict([final1DImage])[0]}"
            answer = answer1+", "+answer2
        else:
            answer="please make sure to send an allowed file of png/jpg/jpeg"

        return render_template("index.html",answer=answer)
    return render_template("index.html",answer="XX")

@app.route("/signup", methods = ['GET', 'POST'])
def signup(ERROR=""):
    if request.method == 'POST':
        uname=request.form['usermane']
        password=request.form['psw']
        passwordValidate=request.form['psw-repeat']

        if password != passwordValidate:
            return render_template("/signup.html",ERROR="password is not the same")
        if db.getUser(uname)!=None:
            return render_template("/signup.html",ERROR="user is already in use")

        hashedPSWD=generate_password_hash(password)
        db.addUser(uname,hashedPSWD)
        return redirect("/home",code=200)
    else:
        return render_template("/signup.html")


@app.route("/login", methods = ['GET', 'POST'])
def login(ERROR=""):
    if request.method == 'POST':
        uname=request.form['uname']
        password=request.form['psw']
        user=db.getUser(uname)

        if user==None or not check_password_hash(user[2],password):
            return render_template("login.html",ERROR="User name or password are incorrect") 

        #create session
        session['loggedin'] = True
        session['username'] = uname

        return redirect("/upload",code=200)

    return render_template("login.html")

def create_model():
    from knn_brute import KNNBrute
    from kneighbors import KnnClassifier
    from MinMaxScale import MinMaxScale
    from keras.datasets import mnist
    import pandas as pd
    brute = KNNBrute()
    knnTree = KnnClassifier(k_neighbors=7, depth=10)
    (X_tr, y_train), (X_te, y_test) = mnist.load_data()
    y_train = np.array(y_train).T
    X_train = []
    for img_xtr in X_tr:
        X_train.append(img_xtr.reshape(img_xtr.shape[0]*img_xtr.shape[1]))
    X_train = np.array(X_train)
    X_train = pd.DataFrame(X_train)
    scaler = MinMaxScale()
    X_train = scaler.fit_transform(X_train)
    X_train = X_train.to_numpy()
    brute.fit(X_train, y_train)
    knnTree.fit(X_train, y_train)
    return knnTree, brute
    
    

if __name__=="__main__":
    db=dataBase()
    # model = pickle.loads(db.import_model("brute knn"))
    knnTree, brute = create_model()
    app.run(debug=True)
