import streamlit as st
import pandas as pd
import pickle

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

header = st.container()
dataset = st.container()
features = st.container()
model_prediction = st.container()
file_name = "finalized_model.sav"


@st.cache
def get_data(filename):
	ml_service = pickle.load(open(filename,'rb'))
	return ml_service



with header:
	st.title('Welcome to Height vs Weight prediction')	


with dataset:
	st.header('Model has been Trained on linear Regression')
	st.text('dataset is available on everywhere')

	

with features:
	st.header('The features I created')

	st.markdown('* **first feature:** Predict Weight based on Height in inches')
	



with model_prediction:
    st.header('Time to train the model!')
    st.text('Here you get to choose the hyperparameters of the model and see how the performance changes!')
    sel_col, disp_col = st.columns(2)

    height = sel_col.slider('Height in inches ', min_value=20, max_value=96, value=60, step=1)


    ml_service = get_data(file_name)
    result = ml_service.predict([[height]])[0]
    

    disp_col.subheader('Predict Weight in pounds is:')
    disp_col.write(result)

    # disp_col.subheader('Mean squared error of the model is:')
    # disp_col.write(mean_squared_error(y, prediction))

    # disp_col.subheader('R squared score of the model is:')
    # disp_col.write(r2_score(y, prediction))