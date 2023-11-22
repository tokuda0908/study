from flask import Flask, render_template
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    html = render_template('index.html')
    l = ['段落', '箇条書き', '手順']
    return render_template("index.html", l = l) 

if __name__ == "__main__":
    app.run()