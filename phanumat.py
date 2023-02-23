import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image #pillow
import joblib
from sklearn.linear_model import LinearRegression


st.title("💸""Calculation of  fare!!!""💸")
st.title("🚕""Calculation of taxi fare!!!""💸")
#st.markdown('## ร้านกาแฟสไตล์อบอุ่น')
st.markdown(
    f"""
         <style>
         .stApp {{
             background-image: url("https://wallpaperaccess.com/full/3748642.jpg");
             background-attachment: fixed;https://png.pngtree.com/thumb_back/fh260/background/20210625/pn
             background-size: cover;
             /* opacity: 0.3; */
         }}
         </style>
         """,
    unsafe_allow_html=True
)
def create_model():
   # model = svm.SVC()
   # X_train, x_test, y_train
    pass

def load_model():
    pass

def predict():
    pass
def add_logo(logo_path, width, height):
    logo = Image.open('image/susuchil.png')
    modified_logo = logo.resize((width, height))
    return modified_logo

my_logo = add_logo(logo_path="your/logo/path", width=100, height=100)
st.sidebar.image(my_logo)

st.sidebar.markdown('## Home')


taxi_size = st.selectbox('กรุณาเลือกประเภทของแท็กซี่!', ['แบบปกติ', 'แบบพิเศษ'])
st.markdown("✨""แบบปกติได้แก่รถยนต์รับจ้างที่มีลักษณะเป็นรถเก๋ง แบบธรรมดา ")
st.markdown("✨""แบบพิเศษหรือแบบใหญ่พิเศษได้แก่รถรับจ้างแบบพิเศษ(VIP)หรือรถรับจ้างที่มีขนาดใหญ่พิเศษ ")
distance = st.number_input('กรุณาระบุระยะทางเป็นกิโลเมตร', min_value=0.0, step=0.1)
time = st.number_input("กรุณาระบุเวลาที่รถติดเป็นนาที", value=0, step=1)

def calculate_fare1(distance):
    if taxi_size == 'ขนาดปกติ':
        default_fare = 35.0
        if distance <= 1:
            return default_fare
        elif distance <= 10:
            return default_fare + (distance - 1) * 6.5
        elif distance <= 20:
            return default_fare + 9 * 6.5 + (distance - 10) * 7
        elif distance <= 40:
            return default_fare + 9 * 6.5 + 10 * 7.0 + (distance - 20) * 8
        elif distance <= 60:
            return default_fare + 9 * 6.5 + 10 * 7.0 + 20 * 8.0 + (distance - 40) * 8.5
        elif distance <= 80:
            return default_fare + 9 * 6.5 + 10 * 7.0 + 20 * 8.0 + 20 * 8.5 + (distance - 60) * 9
        else:
            return default_fare + 9 * 6.5 + 10 * 7.0 + 20 * 8.0 + 20 * 8.5 + 20 * 9.0 + (distance - 80) * 10.5

    else:
        default_fare = 40.0
        if distance <= 1:
            return default_fare
        elif distance <= 10:
            return default_fare + (distance - 1) * 7.5
        elif distance <= 20:
            return default_fare + 9 * 7.5 + (distance - 10) * 8
        elif distance <= 40:
            return default_fare + 9 * 7.5 + 10 * 8.0 + (distance - 20) * 9
        elif distance <= 60:
            return default_fare + 9 * 7.5 + 10 * 8.0 + 20 * 9.0 + (distance - 40) * 9.5
        elif distance <= 80:
            return default_fare + 9 * 7.5 + 10 * 8.0 + 20 * 8.0 + 20 * 9.5 + (distance - 60) * 10.50


if st.button("Calculate Fare"):
        fare = calculate_fare1(distance)
        fare02 = calculate_fare1(distance)
        default_fare1 = 35
        default_fare2 =40
        if time > 0:
            fare += time * 3.0
        st.write("ค่าแท็กซี่: {:.2f} บาท ระยะทาง {} กิโลเมตร เวลารถติด {} นาที ".format(fare, distance, time))
image = Image.open('image/Taxi2.jpg')
st.image(image, caption='นี่คือบริการรถแท็กซี่')


def load_pocket_data():
    return pd.read_excel('taxi_fare.xlsx')

def save_model():
    joblib.dump(model, 'model.joblib')

def load_model():
    return joblib.load('model.joblib')

loadb = st.button('load taxi_fare.xlsx')
if loadb:
    st.write('loading "taxi_fare.xlsx ..."')
    df = pd.read_excel('taxi_fare.xlsx')
    st.write('... done')
    st.dataframe(df)

    fig, ax = plt.subplots()
    ax.scatter(df['distance'], df['fare'])
    plt.xlabel('distance', color='green')
    plt.ylabel('fare', color='red')
    st.pyplot(fig)

trainb = st.button('train fare Taxi')
if trainb:
    st.write('training model ...')
    df = pd.read_excel('taxi_fare.xlsx')
    model = LinearRegression()
    model.fit(df['distance'].values.reshape(-1, 1), df['fare'])
    st.write('... done')
    st.dataframe(df)

st.title("🚕""Calculation of tuk tuks!!""💸")

st.markdown('![image](https://media.istockphoto.com/id/1089588942/vector/tourism-on-tuk-tuk-driving-to-travel-journey-trips-adventure-transportation-thailand.jpg?s=612x612&w=0&k=20&c=HW8VrIjAhfD51kKyV76ZvjhdGbSgs_OFW8IvBEybGW4=)')
st.caption('นี่คือบริการรถตุ๊กๆ')


distance2 = st.number_input("กรุณาระบุระยะทางเป็นกิโลเมตร", value=1.0, step=0.1, min_value=0.1)

if distance2 <= 1.0:
    fare = 35.0
elif distance2 <= 10.0:
    fare = 35.0 + (distance2 - 1.0) * 6.5
elif distance2 <= 20.0:
    fare = 35.0 + 9 * 6.5 + (distance2 - 10.0) * 7.0
elif distance2 <= 40.0:
    fare = 35.0 + 9 * 6.5 + 10 * 7.0 + (distance2 - 20.0) * 8.0
elif distance2 <= 60.0:
    fare = 35.0 + 9 * 6.5 + 10 * 7.0 + 20 * 8.0 + (distance2 - 40.0) * 8.5
elif distance2 <= 80.0:
    fare = 35.0 + 9 * 6.5 + 10 * 7.0 + 20 * 8.0 + 20 * 8.5 + (distance2 - 60.0) * 9.0
else:
    fare = 35.0 + 9 * 6.5 + 10 * 7.0 + 20 * 8.0 + 20 * 8.5 + 20 * 9.0 + (distance2 - 80.0) * 11.5

st.write("ระยะทาง {} กิโลเมตร ค่าโดยสาร {:.2f} บาท ".format(distance2, fare))



def load_pocket_data():
    return pd.read_excel('tuktuk_fare.xlsx')

def save_model(model):
    joblib.dump(model, 'model.joblib')

def load_model():
    return joblib.load('model.joblib')

loadb = st.button('load tuktuk_fare.xlsx')
if loadb:
    st.write('loading "tuktuk_fare.xlsx ..."')
    df = pd.read_excel('tuktuk_fare.xlsx')
    st.write('... done')
    st.dataframe(df)

    fig, ax = plt.subplots()
    ax.scatter(df['distance'], df['fare'])
    plt.xlabel('distance', color='pink')
    plt.ylabel('fare', color='purple')
    st.pyplot(fig)

trainb = st.button('train fare tuktuk')
if trainb:
    st.write('training model ...')
    df = pd.read_excel('tuktuk_fare.xlsx')
    model = LinearRegression()
    model.fit(df[['distance']], df['fare'])
    save_model(model)
    st.write('... done')

    fig, ax = plt.subplots()
    ax.scatter(df['distance'], df['fare'])
    ax.plot(df['distance'], model.predict(df[['distance']]), color='red')
    plt.xlabel('distance', color='pink')
    plt.ylabel('fare', color='purple')
    st.pyplot(fig)



st.title("🏍️""Calculate the fare of a motorcycle""💸")
image = Image.open('image/motorcycle taxi.jpg')
st.image(image, caption='นี่คือบริการรถมอเตอร์ไซค์รับจ้าง')
distance3 = st.number_input("กรุณาระบุระยะทางเป็นกิโลเมตร", min_value=0.0)
if distance3 <= 1.0:
    fare3 = 40
elif distance3 <= 10.0:
    fare3 = 40 + (distance3 - 1.0) * 7.0
elif distance3 <= 20.0:
    fare3 = 40 + 9 * 7.0 + (distance3 - 10.0) * 8.0
elif distance3 <= 40.0:
    fare3 = 40 + 9 * 7.0 + 10 * 8.0 + (distance3 - 20.0) * 9.0
elif distance3 <= 60.0:
    fare3 = 40 + 9 * 7.0 + 10 * 8.0 + 20 * 9.0 + (distance3 - 40.0) * 10.0
elif distance3 <= 80.0:
    fare3 = 40 + 9 * 7.0 + 10 * 8.0 + 20 * 9.0 + 20 * 10.0 + (distance3 - 60.0) * 10.50
else:
    fare3 = 40 + 9 * 7.0 + 10 * 8.0 + 20 * 9.0 + 20 * 8.5 + 20 * 10.50 + (distance3 - 80.0) * 11.5

st.write("ค่าโดยสาร: {} บาท".format(fare3))


def load_pocket_data():
    return pd.read_excel('win_fare.xlsx')

def save_model(model):
    joblib.dump(model, 'model.joblib')

def load_model():
    return joblib.load('model.joblib')

loadb = st.button('load win_fare.xlsx')
if loadb:
    st.write('loading "win_fare.xlsx ..."')
    df = pd.read_excel('win_fare.xlsx')
    st.write('... done')
    st.dataframe(df)

    fig, ax = plt.subplots()
    ax.scatter(df['distance'], df['fare'])
    plt.xlabel('distance', color='yellow')
    plt.ylabel('fare', color='blue')
    st.pyplot(fig)

trainb = st.button('train fare win')
if trainb:
    st.write('training model ...')
    df = pd.read_excel('win_fare.xlsx')
    model = LinearRegression()
    model.fit(df[['distance']], df['fare'])
    save_model(model)
    st.write('... done')

    fig, ax = plt.subplots()
    ax.scatter(df['distance'], df['fare'])
    ax.plot(df['distance'], model.predict(df[['distance']]), color='green')
    plt.xlabel('distance', color='yellow')
    plt.ylabel('fare', color='blue')
    st.pyplot(fig)


