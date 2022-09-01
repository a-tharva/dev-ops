from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_():
    return "<h1 style='margin-left: 35%;'>Hello from flask python</h1>"

@app.route('/test')
def test():
    return '<h1>Test page for flask</h1>'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1532)