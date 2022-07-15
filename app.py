# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 23:55:36 2022

@author: Kencho
"""

import uvicorn
from fastapi import FastAPI
from noteAuth import BankNote
import pickle

#create the app project

app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier = pickle.load(pickle_in)

#index route,opens automatically 

@app.get('/')
def index():
    return {"message":"Hello,world"}

#4.route with a single parameter, returns the parameter 

@app.get("/{name}")
def get_name(name:str):
    return{"message":f"Hello,{name}"}


#json data and return the predicted bank note
@app.post("/predict")
def predict_bankNote(data:BankNote):
    data =data.dict()
    variance = data["variance"]
    stewness =data["skewness"]
    curtosis = data['curtosis']
    entropy =data['entropy']
    
    prediction= classifier.predict([[variance,stewness,curtosis,entropy]])
    
    if(prediction[0]>0.5):
        prediction = "fake note"
    else:
        prediction = "Its a bank Note"
    
    return{
        'prediction':prediction
    }

#run the api 
if __name__ == "__main__":
    uvicorn.run(app,host='127.0.0.1', port = 8000)
    
    
    
#uvicorn app:app --reload
    
    
    
    
    