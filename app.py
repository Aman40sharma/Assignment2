from flask import Flask
app = Flask(__name__)
@app.route('/flask')
def hello():
 return "Hello from flusk"
@app.route('/chintu')
def bello():
 return "Hello from chintu"
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)
