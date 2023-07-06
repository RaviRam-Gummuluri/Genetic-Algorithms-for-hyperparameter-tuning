from flask import Flask, request, jsonify
import pickle
import numpy as np

model=pickle.load(open('model.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def home():
    return "Hello, world!"

@app.route('/predict',methods=['POST'])
def predict():
    age=request.form.get('age')
    sex=request.form.get('sex')
    Chest_pain_type=request.form.get('Chest_pain_type')
    BP=request.form.get('BP')
    Cholestrol=request.form.get('Cholestrol')
    FBS_over_120=request.form.get('FBS_over_120')
    EKG=request.form.get('EKG')
    MAX_HR=request.form.get('MAX_HR')
    Excercise_angina=request.form.get('Excercise_angina')
    ST_depression=request.form.get('ST_depression')
    Slope_st=request.form.get('Slope_st')
    Vessels_Fluro=request.form.get('Vessels_Fluro')
    Thallium=request.form.get('Thallium')

    inp_query=np.array([[int(age),int(sex),int(Chest_pain_type),float(BP),int(Cholestrol),int(FBS_over_120),int(EKG),
                         int(MAX_HR),int(Excercise_angina),float(ST_depression),int(Slope_st),int(Vessels_Fluro),int(Thallium)+1]])
    result= model.predict(inp_query)[0]
    return jsonify({"target":str(int(result[0]))})

if __name__=="__main__":
    app.run(debug=True)
