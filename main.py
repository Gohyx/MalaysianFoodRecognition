import streamlit as st
import matplotlib.pylab as plt
import numpy as np
import food_info
import pandas as pd

from tensorflow import keras
from tensorflow import image as img
from tensorflow import squeeze

@st.cache()
def load_label_list() ->list:
    ds_label_list = food_info.food_namelist
    return ds_label_list

@st.cache()
def load_food_ingredients() ->list:
    food_ingredients = food_info.malaysian_food
    return food_ingredients

@st.cache(allow_output_mutation=True)
def load_model():
    model = food_model = keras.models.load_model('food_recognition_inceptionV3.h5')
    return model

@st.cache()
def predict(
    image,
    ds_label_list: list,
    food_ingredients: list,
    food_model,
    reminder,
    threshold_low=.33,
    threshold_high=.63,
):
    prediction_temp = food_model.predict(image)
    prediction_temp = squeeze(prediction_temp).numpy()
    if np.max(prediction_temp) >= threshold_low:
        prediction_id = np.argmax(prediction_temp, axis=-1)
        prediction = ds_label_list[prediction_id]
        explaination_prediction = food_ingredients[prediction_id]
        if np.max(prediction_temp) < threshold_high:
            reminder = True
    else:
        prediction = "-"
        explaination_prediction = "Unable to recognise the picture, please try again."
    return prediction, explaination_prediction, reminder

def calculate_total_calories(ingredients, calories, quantities):
    total_calories = 0
    for i in range(len(ingredients)):
        total_calories += (calories[i] * quantities[i])
    return total_calories

if __name__ == '__main__':
    ds_label_list = load_label_list()
    food_ingredients = load_food_ingredients()
    food_model = load_model()
    image = np.ones((1,228,228,3))
    prediction = ""
    explaination_prediction = ""
    reminder = False

st.title("Hi! Welcome to Malaysian Food Recognition")
about = "This web application offers Malaysian food recognition for advancing AI in food and healthcare, particularly for Malaysian local food. The food image recognition technology is powered by the state-of-the-art deep learning techniques."
st.write(about)

st.header("Upload A Food Image Here:")
file = st.file_uploader('')
if file:
    image = plt.imread(file)
    image = img.resize(image,(228,228))
    image = np.array(image)
    image = image.reshape(1,228,228,3)/255.0
    prediction, explaination_prediction, reminder = predict(image, ds_label_list, food_ingredients, food_model, reminder)
else:
    prediction = "No image file detected"


st.header("Detected food: "+ prediction)
st.image(image)
# st.write("")
# st.image(image, use_column_width=True)

if explaination_prediction != "Unable to recognise the picture, please try again.":
    st.header("Ingredients and Calories")
    ingredients = explaination_prediction['ingredients']
    calories = explaination_prediction['calories']
    data = {'Ingredients': ingredients, 'Calories(kcal)': calories}
    df = pd.DataFrame(data)
    df = df.assign(Quantity=np.nan)
    for i in range(len(df)):
        df.at[i,'Quantity'] = st.number_input(f'Enter the quantity of {df.at[i,"Ingredients"]}',min_value=0)
    df["Quantity"] = df["Quantity"].astype(int)
    st.table(df)
    total_calories = calculate_total_calories(df['Ingredients'],df['Calories(kcal)'],df['Quantity'])
    st.header(f'Total calories: {total_calories} kcal')
    
if reminder:
    st.subheader("\nThe system cannot detect the picture accurately, please use a clearer picture of food.")

