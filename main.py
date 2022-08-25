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
    return render_template("index.html")

@app.route("/upload", methods = ['GET', 'POST'])
def uploaded():
    if request.method == 'POST':
        f = request.files['file'].read()
        file_bytes = np.frombuffer(f, np.uint8)
        final1DImage=imgConv.getImageAsArray(file_bytes)

        #TODO: connect the model, insert the prediction into the HTML
        print(final1DImage)
        return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)
