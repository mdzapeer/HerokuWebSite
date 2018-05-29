from flask import Flask, render_template
import chart

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/chart/')
def chartpage():
    return render_template("chart.html", script1=chart.script1, div1=chart.div1)

if __name__=="__main__":
    app.run(debug=True)
