# -- coding: utf-8 -


from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
  
@app.route('/')
def index():
    
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