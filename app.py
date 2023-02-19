#print("Hello, World")

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, Alex"

if __name__ == '__main__':
  #print("I'm inside")
  app.run(host='0.0.0.0', debug=True)