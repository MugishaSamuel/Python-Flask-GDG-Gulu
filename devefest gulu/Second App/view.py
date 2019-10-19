# hello_flask: First Python-Flask webapp

from flask import Flask, redirect, url_for, render_template,request


app = Flask(__name__)

app.debug = True 

@app.route('/')
def index():
    """Say hello"""
    return 'Hello, world!'

if __name__ == '__main__':  
    app.run()