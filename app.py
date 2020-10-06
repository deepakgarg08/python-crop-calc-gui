#!/usr/bin/env python
# coding: utf-8

# virtualenv==20.0.23
# In[ ]:


# !pip3 install -U flask-cors
# !pip3 install flask
# !pip3 install pandas

# !python -m pip3 install -U flask-cors
# !pip3 install flask
# !pip3 install pandas 
# !pip3 install xlrd

# In[1]:


import pandas as pd
from flask import Flask  , request, render_template
from flask_cors import CORS

res = {}
app = Flask(__name__)
CORS(app)

	
@app.route("/")
@app.route("/index")

def index():
	return render_template("index.html")

@app.route("/upload", methods = ['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        global xls, df1_Z141, df2_Z351, df3_Z231, df4_Z121, df5_Z251, df6_Z31
        xls = df1_Z141 = df2_Z351 = df3_Z231 = df4_Z121 = df5_Z251 = df6_Z31 = None
        f = request.files['file']
        xls = pd.ExcelFile(f)
        df1_Z141 = pd.read_excel(xls, 'Sheet9')
        df2_Z351 = pd.read_excel(xls, 'Sheet17')
        df3_Z231 = pd.read_excel(xls, 'Sheet12')
        df4_Z121 = pd.read_excel(xls, 'Sheet7')
        df5_Z251 = pd.read_excel(xls, 'Sheet14')
        df6_Z31 = pd.read_excel(xls, 'Sheet3')
    return render_template("upload.html")   

def calculateCalibrationValidation(f2_cal,f3_cal,f1_val,f2_val,f3_val):
    #f2_yield calibration
    if (f2_cal):
        f2_yield = 1545.24 + float(df1_Z141.loc[f2_cal]['Z141']) * 0.3971 + float(df2_Z351.loc[f2_cal]['Z351']) * 0.1693 + f2_cal * 50.53
        res["f2_yield_calib"] = round(f2_yield, 2)
        print("z141")
        print(df1_Z141.loc[f2_cal]['Z141'])
       
    #f3_yield ... calibration
    if (f3_cal):
        f3_yield = 1406.01+ float(df3_Z231.loc[f3_cal]['Z231']) * 0.685 + float(df1_Z141.loc[f3_cal]['Z141']) * 0.353 + f3_cal * 50.11 
        res["f3_yield_calib"] =  round(f3_yield, 2)
    
    #fi_yield...validation
    if (f1_val):
        f1_yield = 2566.3 + float(df4_Z121.loc[f1_val]['Z121']) * 2.525 + float(df6_Z31.loc[f1_val]['Z31']) * 21.8 + f1_val * 47.43 
        res["f1_yield_valid"] = round(f1_yield, 2)
    
    #fi_yield...validation
    if (f2_val):
        f2_yield = 2327.93 + float(df3_Z231.loc[f2_val]['Z231']) * 1.15 + float(df5_Z251.loc[f2_val]['Z251']) * 0.45 + f2_val * 47.60
        res["f2_yield_valid"] =   round(f2_yield, 2)  
    
    #fi_yield...validation
    if (f3_val):
        f3_yield = 2163.26 + float(df1_Z141.loc[f3_val]['Z141']) * 0.25 + float(df2_Z351.loc[f3_val]['Z351']) * 0.16+ f3_val * 48.11
        res["f3_yield_valid"] =     round(f3_yield, 2)
    
    print("result is :" , res)
    return res

@app.route('/calc',methods=['POST'])
def createEmp():   
    f2_cal = request.json['f2_cal']
    f3_cal = request.json['f3_cal']
    f1_val = request.json['f1_val']
    f2_val = request.json['f2_val']
    f3_val = request.json['f3_val']
    result = calculateCalibrationValidation(f2_cal,f3_cal,f1_val,f2_val,f3_val)
    return result


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True,host='0.0.0.0', port=3000)
