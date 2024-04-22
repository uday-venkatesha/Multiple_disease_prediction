import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from os import path

st.markdown(
    """
    <style>
    /* Set the width of the text input boxes */
    div.stTextInput>div>div>input {
        width: 300px !important; /* Adjust the width as needed */
    }
    /* Set the width of the text input labels */
    div.stTextInput>div>label {
        width: 350px !important; /* Adjust the width as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# loading the saved models

diabetes_model = pickle.load(open(path.join('Model','LR_model.sav'), 'rb'))

heart_disease_model = pickle.load(open(path.join('Model','svm_model_heart.sav'),'rb'))

parkinsons_model = pickle.load(open(path.join('Model','svc_model_park.sav'), 'rb'))




# sidebar for navigation
def main():
    with st.sidebar:
        
        selected = option_menu('Multiple Disease Prediction System',
                              
                              ['Diabetes Prediction',
                               'Heart Disease Prediction',
                               'Parkinsons Prediction'],
                              icons=['activity','heart','person'],
                              default_index=0)
        
        
    # Diabetes Prediction Page
    if (selected == 'Diabetes Prediction'):
        
        # page title
        st.title('Diabetes Prediction using ML')
        
        
        # getting the input data from the user
        col1, col2, col3 = st.columns(3)
        
        with col1:
            Pregnancies = st.text_input('Number of Pregnancies', help='Enter the number of pregnancies. NOTE: Please enter the value as 0 if the sex of the patient is Male')
            
        with col2:
            Glucose = st.text_input('Glucose Level', help='Enter the glucose levels which ranges between 70 mg/dl and 100 mg/dl')
        
        with col3:
            BloodPressure = st.text_input('Blood Pressure value', help='Enter the blood pressure value which ranges between 0 mmHg and 120 mmHg')
        
        with col1:
            SkinThickness = st.text_input('Skin Thickness value',help='Enter the triceps skin thickness value which rangrs between 0 and 99mm')
        
        with col2:
            Insulin = st.text_input('Insulin Level', help='Enter the insulin level which is usually less than 17mcU/mL')
        
        with col3:
            BMI = st.text_input('BMI value', help='Enter the BMI value which ranges between 18.5 and 24.9')
        
        with col1:
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', help='Enter the pedigree value is between range of 0.08 and 2.42')
        
        with col2:
            Age = st.text_input('Age of the Person', help='Enter the age of the person')
        
        
        # code for Prediction
        diab_diagnosis = ''
        
        # creating a button for Prediction
        
        if st.button('Diabetes Test Result'):
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            
            if (diab_prediction[0] == 1):
              diab_diagnosis = 'The person is diagnosed with diabetes. Lifestyle modifications and medical management are recommended.'
            else:
              diab_diagnosis = 'The person is not diagnosed with diabetes. However, maintaining a healthy lifestyle and regular screenings are important for diabetes prevention.'
            
        st.success(diab_diagnosis)


    if selected == 'Heart Disease Prediction':
    
        # page title
        st.title('Heart Disease Prediction using ML')
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            age = st.text_input('Age', placeholder='Enter your age')
            
        with col2:
            sex_options = {'Select gender': None, 'Male': 1, 'Female': 0}
            sex = st.selectbox('Sex', list(sex_options.keys()))
            
        with col3:
            cp_options = {'Select Chest Pain Level': None, 'Low': 0, 'Medium': 1, 'High': 2}
            cp = st.selectbox('Chest Pain Level', list(cp_options.keys()), help='Select the chest pain based on the pain severity')
            
        with col1:
            trestbps = st.text_input('trestbps - Resting Blood Pressure', placeholder='Enter Resting Blood Pressure value',help='Enter the resting blood pressure value which ranges between 90 and 120')
            
        with col2:
            chol = st.text_input('chol - Serum Cholestoral', placeholder='Enter Cholestrol value in which is usally less than 120mg/dl which is considered as normal.')
            
        with col3:
            fbs_options = {'Select the FBS Value': None, 'Greater than 120 mg/dl': 1, 'Less than 120 mg/dl': 0}
            fbs = st.selectbox('Fasting blood sugar', list(fbs_options.keys()))
            
        with col1:
            restecg_options = {'Select the resting electrocardiographic results': None, 'Normal': 0, 'Abnormality in ST-T wave': 1, 'Left ventricular hypertrophy': 2}
            restecg = st.selectbox('restecg', list(restecg_options.keys()))
            
        with col2:
            thalach = st.text_input('thalach - Maximum Heart Rate achieved', placeholder='Enter heart rate in beats per minute',help='Enter maximum heart rate value which usually ranges between 70 and 205')
            
        with col3:
            exang_options = {'Select exercise induced agina': None, 'No': 0, 'Yes': 1}
            exang = st.selectbox('exang', list(exang_options.keys()))
            
        with col1:
            oldpeak = st.text_input('oldpeak - ST depression induced by exercise', placeholder='Enter the value', help='Enter the oldpeak value that usally ranges between 0 and 6.2')
            
        with col2:
            slope_options = {'Select Slope value': None, 'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
            slope = st.selectbox('Slope', list(slope_options.keys()))
            
        with col3:
            ca = st.text_input('ca - Number of major vessels colored by flourosopy', placeholder='Enter the value', help='Enter the number of major vessels colored which ranges between 0 and 2')
            
        with col1:
            thal_options = {'Select Thalassemia value': None, 'Normal': 0, 'Fixed defect': 1, 'Reversible defect': 2}
            thal = st.selectbox('Thalassemia', list(thal_options.keys()))
            
        # code for Prediction
        heart_diagnosis = ''
        
        # creating a button for Prediction
        
        if st.button('Heart Disease Test Result'):
            col = [age, sex_options[sex], cp_options[cp], trestbps, chol, fbs_options[fbs], restecg_options[restecg], thalach, exang_options[exang], oldpeak, slope_options[slope], ca, thal_options[thal]]
            
            # Convert to float where possible
            col = [float(item) if str(item).replace('.', '', 1).isdigit() else item for item in col]

            heart_prediction = heart_disease_model.predict([col])                          
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is diagnosed with heart disease. Further evaluation and treatment are recommended.'
            else:
                heart_diagnosis = 'The person is not diagnosed with heart disease. However, regular check-ups are advised to monitor their heart health.'
            
        st.success(heart_diagnosis)


 

    # Parkinson's Prediction Page
    if (selected == "Parkinsons Prediction"):
        
        # page title
        st.title("Parkinson's Disease Prediction using ML")
        
        col1, col2, col3 = st.columns(3)  
        
        with col1:
            fo = st.text_input('MDVP : Fo(Hz) -  Avg vocal fundamental frequency', placeholder="Enter value b/w 88.3 and 260")
            
        with col2:
            fhi = st.text_input('MDVP : Fhi(Hz) - Max vocal fundamental frequency', placeholder = 'Enter value b/w 102.0 and 592.0')
            
        with col3:
            flo = st.text_input('MDVP : Fli(Hz) - Min vocal fundamental frequency', placeholder = 'Enter value b/w 65.5 and 239.0')
            
        with col1:
            Jitter_percent = st.text_input('MDVP : Jitter(%) - Measures of variation in fundamental frequency', placeholder = 'Enter value b/w 0 and 0.03')
            
        with col2:
            Jitter_Abs = st.text_input('MDVP : Jitter(ABS) - Measures of variation in fundamental frequency', placeholder = 'Enter value b/w 0 and 0.1')
            
        with col3:
            RAP = st.text_input('MDVP : RAP - Measures of variation in fundamental frequency', placeholder = 'Enter value b/w 0 and 0.02')
            
        with col1:
            PPQ = st.text_input('MDVP : PPQ - Measures of variation in fundamental frequency', placeholder = 'Enter value b/w 0 and 0.02')
            
        with col2:
            DDP = st.text_input('Jitter : DDP - Measures of variation in fundamental frequency', placeholder = 'Enter value b/w 0 and 0.06')
            
        with col3:
            Shimmer = st.text_input('MDVP : Shimmer - Measures of variation in amplitude', placeholder = 'Enter value b/w 0.01 and 0.12')
            
        with col1:
            Shimmer_dB = st.text_input('MDVP : Shimmer(dB) - Measures of variation in amplitude', placeholder = 'Enter value b/w 0.09 and 1.3')
            
        with col2:
            APQ3 = st.text_input('Shimmer : APQ3 - Measures of variation in amplitude', placeholder = 'Enter value b/w 0 and 0.06') 
            
        with col3:
            APQ5 = st.text_input('Shimmer : APQ5 - Measures of variation in amplitude', placeholder = 'Enter value b/w 0.01 and 0.08') 
            
        with col1:
            APQ = st.text_input('MDVP : APQ - Measures of variation in amplitude', placeholder = 'Enter value b/w 0.01 and 0.14')
            
        with col2:
            DDA = st.text_input('Shimmer : DDA - Measures of variation in amplitude', placeholder = 'Enter value b/w 0.01 and 0.17') 
            
        with col3:
            NHR = st.text_input('NHR - Noise to Harmonics Ratio', placeholder = 'Enter value b/w 0 and 0.31')
            
        with col1:
            HNR = st.text_input('HNR - Harmonics to Noise Ratio', placeholder = 'Enter value b/w 8.44 and 33') 
            
        with col2:
            RPDE = st.text_input('RPDE - Nonlinear dynamical complexity measures', placeholder ='Enter value b/w 0.26 and 0.69')
            
        with col3:
            DFA = st.text_input('DFA - Signal fractal scaling exponent', placeholder = 'Enter value b/w 0.57 and 0.83')
            
        with col1:
            spread1 = st.text_input('Spread 1 - Nonlinear measures of fundamental frequency variation', placeholder = 'Enter value b/w -7.96 and -2.43')
            
        with col2:
            spread2 = st.text_input('Spread 2 - Nonlinear measures of fundamental frequency variation', placeholder = 'Enter value b/w 0.01 and 0.45')
            
        with col3:
            D2 = st.text_input('D2 - Nonlinear dynamical complexity measure', placeholder = 'Enter value b/w 1.42 and 3.67')
            
        with col1:
            PPE = st.text_input('PPE - Nonlinear measures of fundamental frequency variation', placeholder = 'Enter value b/w 0.04 and 0.53')
            
        
        
        # code for Prediction
        parkinsons_diagnosis = ''
        
        # creating a button for Prediction    
        if st.button("Parkinson's Test Result"):
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])             
            
            if (parkinsons_prediction[0] == 1):
              parkinsons_diagnosis = "The person is diagnosed with Parkinson's disease. Further evaluation by a healthcare professional specializing in movement disorders is recommended."
            else:
              parkinsons_diagnosis = "The person is not diagnosed with Parkinson's disease. However, if symptoms persist, consultation with a healthcare provider is advised for further assessment."
            
        st.success(parkinsons_diagnosis)




if __name__=='__main__':
    main()


