import streamlit as st
import requests

st.title("Прогноз цены на жильё")

MedInc = st.number_input("Медианный доход", value=3.0)
HouseAge = st.number_input("Средний возраст жилья", value=3.0)
AveRooms = st.number_input("Общее кол-во комнат", value=3.0)
AveBedrms = st.number_input("Общее кол-во спален", value=3.0)
Population = st.number_input("Население", value=1500.0)
AveOccup = st.number_input("Кол-во домохозяйств", value=500.0)
Latitude = st.number_input("Широта", value=37.88)
Longitude = st.number_input("Долгота", value=-122.33)

if st.button("Получить прогноз"):
    data = {
    "MedInc": MedInc,
    "HouseAge": HouseAge,
    "AveRooms": AveRooms,
    "AveBedrms": AveBedrms,
    "Population": Population,
    "AveOccup": AveOccup,
    "Latitude": Latitude,
    "Longitude": Longitude
    }

    url = 'https://california-regression.onrender.com/predict'
    response = requests.post(url, json=data)

    if response.status_code == 200:
        try:
            data = response.json()
            prediction = data.get('prediction')
            if prediction is not None:
                st.success(f'Прогнозируемая цена: {prediction*1000:.2f}$')
                st.subheader('Визуализация прогноза')
                st.bar_chart({"Прогноз":[prediction]})
            else:
                st.error("Ошибка! Ответ API не содержит прогноз!")
        except:
            st.error("Ошибка! Ответ API не является валидным json!")
    else:
        st.error("Ошибка! API вернул статус: {response.status_code}")

