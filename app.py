from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Flask Server Home Page')

@app.route('/About')
def About():
  return render_template('About.html', pageTitle='About')

@app.route('/Estimate')
def Estimate():
  return render_template('Estimate.html', pageTitle='Estimate')

if __name__ == '__main__':
    app.run(debug=True)
