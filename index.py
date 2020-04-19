from flask import Flask, render_template, request, redirect, url_for
from bs4   import BeautifulSoup
import numpy as np
import pandas as ps

app = Flask(__name__)

def picked_up():
    messages = [
        'こんにちは、あなたの名前はなんですか？',
        'やあ！お名前はなんですか？',
        'あなたの名前を教えてね？'
    ]
    return np.random.choice(messages)

@app.route('/')
def index():
    title   = 'ようこそ！！'
    message = picked_up()
    return render_template('index.html', message=message, title=title)

@app.route('/post',methods = ['GET','POST'])
def post():
    title = 'こんにちは'
    if request.method == 'POST':
        name = request.form['name']
        return render_template('index.html',name=name,title=title)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0')