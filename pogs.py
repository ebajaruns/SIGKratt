# -- coding: utf-8 -

import os
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
  
@app.route('/')
def index():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Do Something':
            print("poga nospiesta")
            os.system("mpg321 hello.mp3")         
        elif request.form['submit_button'] == 'Do Something Else':
            os.system("mpg321 service.mp3") 
        else:
            return render_template('index.html')
    elif request.method == 'GET':
        print("No Post Back Call")
    return render_template('index.html')
    
    
@app.route('/uzn')
def cakes():
    
    return render_template('uzn.html')   
    
@app.route('/estsak')
def estsak():
    return render_template('estsak.html')  
    
@app.route('/engsak')
def engsak():
    return render_template('engsak.html')      
    
@app.route('/enuzn')
def enuzn():
    return render_template('enuzn.html') 
    
@app.route('/esuzn')
def esuzn():
    return render_template('esuzn.html')         

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')