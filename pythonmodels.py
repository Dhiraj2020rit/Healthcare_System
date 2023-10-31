# pyscript.write("mytext","I am here")
from pyscript import document
import joblib
def predict_others(event):
    input_arr = []
    loaded_model = joblib.load('logistic_regression_model.pkl')
    predictions = loaded_model.predict(input_arr)
    op_qry = document.querySelector("#predictedop")
    op_qry.innerText = predictions[0]
    pyscript.write("predictedop",predictions[0])