from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
  return "<p>hello word Teste teste teste</p>"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  #app.run(host='127.0.0.1', port=80, debug=True)
