from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", user = "Yasin Kath")

@app.route("/breweries")
def breweries():
    return render_template("breweries.html", user = "Yasin Kath")

@app.route("/beer_types")
def beer_types():
    return render_template("beer_types.html", user = "Yasin Kath")

@app.route("/about")
def about():
    return render_template("about.html", user = "Yasin Kath")
    
if __name__ == "__main__":
    app.run(debug=True)