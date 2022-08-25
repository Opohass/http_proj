import imgConv
import numpy as np
from flask import Flask, render_template, request

app =Flask(__name__)
app.config['UPLOAD_FOLDER']="./"
app.config['MAX_CONTENT_PATH']=100

#index route
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods = ['GET', 'POST'])
def uploaded():
    if request.method == 'POST':
        f = request.files['file'].read()
        file_bytes = np.fromstring(f, np.uint8)
        final1DImage=imgConv.getImageAsArray(file_bytes)

        #TODO: connect the model, insert the prediction into the HTML
        
        return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)

# #read image file string data
# filestr = request.files['file'].read()
# #convert string data to numpy array
# file_bytes = numpy.fromstring(filestr, numpy.uint8)
# # convert numpy array to image
# img = cv.imdecode(file_bytes, cv.IMREAD_UNCHANGED)