#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# !pip3 install -U flask-cors
# !pip3 install flask
# !pip3 install pandas

# !python -m pip3 install -U flask-cors
# !pip3 install flask
# !pip3 install pandas 


# In[1]:


import pandas as pd
from flask import Flask  , request, render_template
from flask_cors import CORS


# In[2]:


df = pd.read_csv('database.csv')


# In[3]:


new_header = df.iloc[0] 
df = df[1:]
df.columns = new_header
res = {}


# In[4]:


df.head()


# In[ ]:


def calculateCalibrationValidation(f2_cal,f3_cal,f1_val,f2_val,f3_val):
    #f2_yield calibration
    if (f2_cal):
        f2_yield = 1545.24 + float(df.loc[f2_cal]['Z141']) * 0.3971 + float(df.loc[f2_cal]['Z351']) * 0.1693 + f2_cal * 50.53
        res["f2_yield_calib"] = round(f2_yield, 2)
       
    #f3_yield ... calibration
    if (f3_cal):
        f3_yield = 1406.01+ float(df.loc[f3_cal]['Z231']) * 0.685 + float(df.loc[f3_cal]['Z141']) * 0.353 + f3_cal * 50.11 
        res["f3_yield_calib"] =  round(f3_yield, 2)
    
    #fi_yield...validation
    if (f1_val):
        f1_yield = 2566.3 + float(df.loc[f1_val]['Z121']) * 2.525 + float(df.loc[f1_val]['Z31']) * 21.8 + f1_val * 47.43 
        res["f1_yield_valid"] = round(f1_yield, 2)
    
    #fi_yield...validation
    if (f2_val):
        f2_yield = 2327.93 + float(df.loc[f2_val]['Z231']) * 1.15 + float(df.loc[f2_val]['Z251']) * 0.45 + f2_val * 47.60
        res["f2_yield_valid"] =   round(f2_yield, 2)  
    
    #fi_yield...validation
    if (f3_val):
        f3_yield = 2163.26 + float(df.loc[f3_val]['Z141']) * 0.25 + float(df.loc[f3_val]['Z351']) * 0.16+ f3_val * 48.11
        res["f3_yield_valid"] =     round(f3_yield, 2)
    
    print("result is :" , res)
    return res

app = Flask(__name__)
CORS(app)

	
@app.route("/")
def index():
	# return "ohh yeah!!"
	return render_template("index.html")


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


# In[ ]:


# [f2_cal,f3_cal,f1_val,f2_val,f3_val] = int(input()),int(input()),int(input()),int(input()),int(input())
# result = calculateCalibrationValidation(f2_cal,f3_cal,f1_val,f2_val,f3_val)
# print(result)


# In[ ]:





# In[ ]:





# In[ ]:




