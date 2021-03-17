from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/date')
def datee():
    date = datetime.now()
    d1 = date.strftime("%Y-%m-%d")
    return d1, 200

@app.route('/square')
def square():
    a = request.args.get('a',default=1, type=int)
    sum=int(a)*int(a)
    return (sum), 200

@app.route('/divide')
def divide(x,y):
    x=request.args.get('x',default=1, type=float)
    y=request.args.get('x',default=1, type=float)
    try:
        div=float(x)/float(y)
        return str(div),200
    except:
        return "Error", 400


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
