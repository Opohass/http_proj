
from flask import Flask

app =Flask(__name__)

#index route

@app.route("/")
def index():
    return "test"


if __name__=="__main__":
    app.run(debug=True)
