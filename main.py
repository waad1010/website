from flask import Flask, render_template
import  os

# Create an instance of Flask
app = Flask(__name__)

# Define a route for the root URL ("/") and associate it with a view function
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/request')
def request():
    return render_template('request.html')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)





