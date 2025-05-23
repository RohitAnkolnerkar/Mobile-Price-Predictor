import streamlit as st
import pandas as pd
import numpy as np

import pickle
pipe=pickle.load(open('mobile_price_model.pkl','rb'))
mob2=pd.read_csv('cleaned_mob.csv')
mob=pickle.load(open('data.pkl','rb'))
mob1=pd.DataFrame(mob)
st.title('mobile price predictor')
name=st.selectbox('how do you like to be contacted',mob2['Name'].values)
brand=st.selectbox('brand',mob2['company'].unique())
processor=st.selectbox('processor',mob2['Processor_name'].values)
ram=st.selectbox('Ram',[2,4,6,8,10,12])
spec_score=st.selectbox('Spec_score',list(np.arange(1,101)))
Rate=st.selectbox('Rating',list(np.arange(1,11)))
display=st.selectbox('DisplaySize',mob2['Display'].unique())
Battery=st.selectbox('Battery',[1000,2000,3000,4000,5000,6000,7000,8000])
InbuiltMemory=st.selectbox('Rom',[32,64,128,256,512])
Front=st.selectbox('Front',mob2['Front_camera'].unique())
Back=st.selectbox('Back',mob2['Back_camera'].unique())
charging=st.selectbox('charger',mob2['fast_charging'].unique())

if st.button('predict price'):
    query= np.array([name,Rate,spec_score,ram,Battery,display,brand,InbuiltMemory,charging,processor,Front,Back])
    query=query.reshape(1,12)
    pipe.predict(query)

