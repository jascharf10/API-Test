from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello, World!"

@app.route("/<int:value>")
def home(value):
    add_one = value + 1
    return render_template('index.html', string="TESTING!!!", value=add_one)
    
if __name__ == "__main__":
    app.run(debug=True)
    
