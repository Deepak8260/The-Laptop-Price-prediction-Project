import streamlit as st
import sklearn
import pickle
import numpy as np

# Import Model
pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))

st.title('KD Laptop Price Predictor')

# brand
company = st.selectbox('Brand',df['Company'].unique())

# Type Of Laptop
type = st.selectbox('Type',df['TypeName'].unique())

# Ram
ram = st.selectbox('Ram(in GB',[2,4,8,16,32,64,128])

# Weight
weight = st.number_input('Weight')

# TouchScreen
touchScreen = st.selectbox('TouchScreen',['No','Yes'])

# IPS
ips = st.selectbox('IPS',['No','Yes'])

# Resolution
resolution = st.selectbox('Screen Resolution',['1366x768', '1280x800', '1440x900', '1600x900', '1920x1080', '1920x1200', '2560x1600', '2560x1440', '2880x1800', '3200x1800', '3440x1440', '3840x1600', '3840x2160', '5120x3200', '2304x1440']
)

# Screen Size
screen_size = st.number_input('Screen Size')

# Cpu
cpu = st.selectbox('CPU',df['Cpu Brand'].unique())

gpu = st.selectbox('GPU',df['Gpu'].unique())

os = st.selectbox('OS',df['os'].unique())

hdd=st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

ssd=st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

if st.button('predict price'):
	if touchScreen=='Yes':
		touchScreen=1
	else:
		touchScreen=0

	if 'ips' == 'Yes':
		ips=1
	else:
		ips=0

	x_res= int(resolution.split('x')[0])
	y_res = int(resolution.split('x')[1])
	try:
		ppi = (((x_res ** 2) + (y_res ** 2)) ** 0.5) / screen_size
		querry = np.array([company, type, ram, gpu, weight, touchScreen, ips, ppi, cpu, hdd, ssd, os])

		querry = querry.reshape(1, 12)
		if weight <= 0 or screen_size <= 0:
			st.title('Please Enter all the details correctly')
		elif hdd == 0 and ssd == 0:
			st.title('Please select at least one storage option (HDD or SSD).')
		else:
			st.title("The Predicted Price is: " + str(int(np.exp(pipe.predict(querry))[0])))
	except ZeroDivisionError:
		st.title("Screen Size cannot be zero. Please provide a valid value.")
		ppi = 0

	#ppi = (((x_res**2) + (y_res**2))**0.5)/screen_size













