from flask import Flask, render_template

#We created new Flask app object.
app = Flask(__name__)

#This is a controller.
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/kavbojke")
def kavbojke():
    return render_template("kavbojke.html")

@app.route("/majica")
def majica():
    return render_template("majica.html")

if __name__ == '__main__':
    app.run(use_reloader=True)
