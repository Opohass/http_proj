import imgConv
import numpy as np
from flask import Flask, render_template, request
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

app =Flask(__name__)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
#where to save a file if we add this option, now the image uploaded isn't saved
# app.config['UPLOAD_FOLDER']="./" 
# app.config['MAX_CONTENT_PATH']=100

#index route
@app.route("/")
def index():
    return render_template("login.html") #TODO: check if user is logged in
    # return render_template("index.html",answer="XX")

#when image upload route
@app.route("/upload", methods = ['GET', 'POST'])
def uploaded():
    if request.method == 'POST':
        f = request.files['file']

        validExtention='.' in f.filename and f.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
        if f != "" and validExtention:
            f=f.read()
            file_bytes = np.frombuffer(f, np.uint8)
            final1DImage=imgConv.getImageAsArray(file_bytes)
            #TODO: connect the model, insert the prediction into the HTML
            answer="i need to implement this..."
        else:
            answer="please make sure to send an allowed file of png/jpg/jpeg"

        return render_template("index.html",answer=answer)

@app.route("/signup", methods = ['GET', 'POST'])
def signup():
    # print("")
    # print(request.form['uname'])
    return render_template("signup.html")

if __name__=="__main__":
    app.run(debug=True)
