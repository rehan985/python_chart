#from crypt import methods
from optparse import Values
from flask import Flask,render_template,request
import os
import pandas as pd

app = Flask(__name__)

@app.route('/', methods = ['GET' , 'POST'])
def index():
    return render_template('index.html')

@app.route('/data',methods = ['GET','POST'])
def data():
    if request.method == 'POST':
        file = request.form['upload-file']
        data=pd.read_excel(file)
        
        label=list(data['X'])
        Value=list(data['Y'])


    return render_template('graph.html',labels=label ,values=Value)



if __name__=='__main__':
        app.run(host="0.0.0.0",port='',debug=True)   
  