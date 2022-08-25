import imgConv
import numpy as np
from flask import Flask, render_template, request

app =Flask(__name__)
#where to save a file if we add this option, now the image uploaded isn't saved
# app.config['UPLOAD_FOLDER']="./" 
# app.config['MAX_CONTENT_PATH']=100

#index route
@app.route("/")
def index():
    answer="CC"
    return render_template("index.html",answer=answer)

#when image upload route
@app.route("/upload", methods = ['GET', 'POST'])
def uploaded():
    if request.method == 'POST':
        f = request.files['file'].read()
        if f != b"":
            file_bytes = np.frombuffer(f, np.uint8)
            final1DImage=imgConv.getImageAsArray(file_bytes)
            #TODO: connect the model, insert the prediction into the HTML
            answer="i need to implement this..."
        else:
            answer="TEST"

        return render_template("index.html",answer=answer)

if __name__=="__main__":
    app.run(debug=True)
