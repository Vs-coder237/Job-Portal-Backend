from flask import Flask

app = Flask(__name__)

@app.route("/")
def Home():
    return "<p>Wellcome!</p>"

if __name__ == "__main__":
    app.run(debug=False, host = '0.0.0.0')