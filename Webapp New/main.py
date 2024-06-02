from flask import Flask,render_template,request
import joblib
import numpy as np
from keras.models import load_model
from keras import backend as K

model=load_model('models/model-118.model')

scaler_data=joblib.load('models/sacler_data.sav')
scaler_target=joblib.load('models/scaler_target.sav')

app=Flask(__name__) #application

@app.route('/')
def index():

	return render_template('patient_details.html')

@app.route('/getresults',methods=['POST'])
def getresults():

	result=request.form 

	print(result)

	name=result['name']
	gender=float(result['gender'])
	age=float(result['age'])
	tc=float(result['tc'])
	hdl=float(result['hdl'])
	smoke=float(result['smoke'])
	bpm=float(result['bpm'])
	diab=float(result['diab'])

	test_data=np.array([gender,age,tc,hdl,smoke,bpm,diab]).reshape(1,-1)

	test_data=scaler_data.transform(test_data) #scaling the features before applying to the model

	prediction=model.predict(test_data)

	prediction=scaler_target.inverse_transform(prediction) #inverse scaling the prediction(target) before returning
	print(prediction,prediction[0],prediction[0][0])
	
	resultDict={"name":name,"risk":round(prediction[0][0],2)}

	return render_template('patient_results.html',results=resultDict)

app.run(debug=True)