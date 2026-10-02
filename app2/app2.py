from flask import Flask

#create a Flask Application
app = Flask(__name__)

#define a route for the root URL
@app.route('/')
def hello_world():
    return "Hello, World App 2!"

#run the application if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=8081, host='0.0.0.0')
    