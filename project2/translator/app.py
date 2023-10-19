from flask import Flask, render_template, request
from summarizer4u import summary


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        user_input = request.form['user_input']
        result = summary(user_input)
    return render_template('index.html', result=result)

@app.route('/hello')
def hello():
    return "Hello"

    
if __name__ == '__main__':
    app.run(debug=True)
