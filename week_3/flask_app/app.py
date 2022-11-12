import pandas as pd
from pycaret.regression import load_model, predict_model
from flask import Flask, request
import numpy as np


median_value_model = load_model("./gbr_model_pipeline")


app = Flask(__name__)

@app.route("/")
def index():
    return """
    <form action="/model" method="post">
    <h1>Insurance AI prediction Model</h1>
    <label>CRIM - per capita crime rate by town:</label> <input type="text" name="crim"><br>
     <label>ZN - proportion of residential land zoned for lots over 25,000 sq.ft:</label> <input type="text" name="zn"><br>
     <label>INDUS - proportion of non-retail business acres per town.:</label> <input type="text" name="indus"><br>
     <label>CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise):</label> <input type="text" name="chas"><br>
     <label>NOX - nitric oxides concentration (parts per 10 million):</label> <input type="text" name="nox"><br>
     <label>RM - average number of rooms per dwelling:</label> <input type="text" name="rm"><br>
     <label>AGE - proportion of owner-occupied units built prior to 1940:</label> <input type="text" name="age"><br>
     <label>DIS - weighted distances to five Boston employment centre:</label> <input type="text" name="dis"><br>
     <label>RAD - index of accessibility to radial highways:</label> <input type="text" name="rad"><br>
     <label>TAX - full-value property-tax rate per $10,000:</label> <input type="text" name="tax"><br>
     <label>PTRATIO - pupil-teacher ratio by town:</label> <input type="text" name="ptratio"><br>
     <label>BLACK - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town:</label> <input type="text" name="black"><br>
     <label>LSTAT - percent lower status of the population:</label> <input type="text" name="lstat"><br>     


     <input type="submit" value="Predict now">
    </form>
    """

@app.route("/model", methods=['POST'])
def about():
    crim = np.float(request.form['crim'])
    zn = np.float(request.form['zn'])
    indus = np.float(request.form['indus'])
    chas = np.int64(request.form['chas'])
    nox = np.float(request.form['nox'])
    rm_b = np.float(request.form['rm'])
    age = np.float(request.form['age'])
    dis = np.float(request.form['dis'])
    rad = np.int64(request.form['rad'])
    tax = np.float(request.form['tax'])
    ptratio = np.float(request.form['ptratio'])  
    black = np.float(request.form['black'])
    lstat = np.float(request.form['lstat'])      
    dummy_mdev = 0.0


    df = pd.DataFrame([[crim,zn,indus,chas,nox,rm_b,age,dis,rad,tax,ptratio,black,lstat,dummy_mdev]], 
    columns=['crim', 'zn', 'indus', 'chas', 'nox','rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'black', 'lstat', 'medv'])
    print(df)
    df1 = predict_model(median_value_model,df)
    result = df1['Label'].values[0]
    print(result)

    return f"""
    CRIM - per capita crime rate by town {crim}<br>
    ZN - proportion of residential land zoned for lots over 25,000 sq.ft {zn}<br>
    INDUS - proportion of non-retail business acres per town. {indus}<br>
    CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise) {chas}<br>
    NOX - nitric oxides concentration (parts per 10 million) {nox}<br>
    RM - average number of rooms per dwelling {rm_b}<br>
    AGE - proportion of owner-occupied units built prior to 1940 {age}<br>
    DIS - weighted distances to five Boston employment centres {dis}<br>
    RAD - index of accessibility to radial highways {rad}<br>
    TAX - full-value property-tax rate per $10,000 {tax}<br>
    PTRATIO - pupil-teacher ratio by town {ptratio}<br>
    BLACK - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town {black}<br>
    LSTAT - % lower status of the population {lstat}<br>
    <br>
    <h1>Predict Medain Value {result}</h1>
    """        

app.run(debug=True)
