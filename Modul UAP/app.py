import pickle
import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model

# Load the saved models
random_forest_model = pickle.load(open('UAP/random_forest_model.pkl', 'rb'))
ffnn_model = load_model('UAP/ffnn_model.h5')

# Set up the title for the app
st.title('Prediksi Status Gizi Berdasarkan Data Input')

# Input form
col1, col2 = st.columns(2)

# Mapping input string to numerical values
jenis_kelamin_map = {'laki-laki': 0, 'perempuan': 1}  # Mapping for gender

# Input fields
with col1:
    jenis_kelamin = st.selectbox('Jenis Kelamin (laki-laki atau perempuan)', ['laki-laki', 'perempuan'])
with col2:
    umur = st.slider('Usia (bulan)', min_value=0, max_value=60, step=1, value=24)

tinggi_badan = st.slider('Tinggi Badan (cm)', min_value=40.00, max_value=128.00, step=0.01, value=100.00)

# For prediction model selection
model_choice = st.selectbox('Pilih Model:', ['Random Forest', 'FFNN'])

# Prediction button
if st.button('Prediksi Status Gizi'):
    try:
        # Prepare input data for prediction
        input_data = np.array([[ 
            jenis_kelamin_map[jenis_kelamin], 
            umur, 
            tinggi_badan
        ]])

        # Choose model based on user's selection
        if model_choice == 'Random Forest':
            prediction = random_forest_model.predict(input_data)
            model_used = 'Random Forest'
        else:
            prediction = ffnn_model.predict(input_data)
            model_used = 'FFNN'

            # If the FFNN model returns probabilities, get the class with the highest probability
            if prediction.ndim > 1 and prediction.shape[1] > 1:
                prediction = np.argmax(prediction, axis=1)  # Get the index of the maximum probability

            # If the FFNN model is binary (e.g., sigmoid), round the prediction
            elif prediction.ndim == 2 and prediction.shape[1] == 1:
                prediction = (prediction > 0.5).astype(int)  # Convert probability to class (0 or 1)

        # Map prediction result to the status gizi
        status_gizi_map = {0: 'Normal', 1: 'Severely Stunted', 2: 'Stunted', 3: 'Tinggi'}
        prediction_label = status_gizi_map.get(prediction[0], 'Unknown')

        st.success(f'Prediksi Status Gizi menggunakan model {model_used}: {prediction_label}')

    except KeyError:
        st.error('Input yang diberikan tidak valid. Pastikan Anda mengetik dengan benar!')
