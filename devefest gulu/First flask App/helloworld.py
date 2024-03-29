# hello_flask: First Python-Flask webapp

from flask import Flask  # From module flask import class Flask


app = Flask(__name__)    # Construct an instance of Flask class for our webapp

app.debug = True # Debug mode

@app.route('/')   # URL '/' to be handled by main() route handler
def index():
    """Say hello"""
    return 'Hello, world!'

if __name__ == '__main__':  # Script executed directly?
    app.run()  # Launch built-in web server and run this Flask webapp