from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
def index():
    return render_template('html/hello.html') # html/index.htmlを表示しますよという指定

@app.route('/flask')
def flask_hello():
    return render_template('html/flask.html')

# @app.route('/python')
# def hello_python():
#     return 'Hello Python world!'

if __name__ == '__main__':
    app.run(debug=True)