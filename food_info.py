import pandas as pd

food_namelist = ["Ayam Goreng",
                "Bubur Ayam",
                "Char Kuey Teow",
                "Curry Puff",
                "Kaya Toast",
                "Nasi Goreng",
                "Nasi Lemak",
                "Popiah",
                "Roti Canai",
                "Satay"]

malaysian_food = [
    {
        'name':'Ayam Goreng',
        'ingredients':['Drumstick','Thigh','Breast','Wing'],
        'calories':[160,287,342,188]
    },
    {
        'name':'Bubur Ayam',
        'ingredients':['Rice','Chicken','Onion','Garlic','Ginger','Coriander','Cumin','Coconut Milk','Salt','Pepper'],
        'calories':[220,200,54,4,3,3,3,350,1,1]
    },
    {
        'name':'Char Kuey Teow',
        'ingredients':['Rice Noodles', 'Egg', 'Prawns', 'Bean Sprouts', 'Chili', 'Garlic', 'Onion', 'Coriander', 'Lime Juice', 'Soy Sauce'],
        'calories':[220, 90, 130, 18, 6, 4, 54, 3, 3, 9]
    },
    {
        'name':'Curry Puff',
        'ingredients':['Potatoes', 'Onion', 'Curry Powder', 'Garlic', 'Coriander', 'Cumin', 'Flour', 'Egg', 'Salt'],
        'calories':[120, 54, 9, 4, 3, 3, 120, 90, 1]
    },
    {
        'name':'Kaya Toast',
        'ingredients':['Bread', 'Butter', 'Kaya', 'Egg'],
        'calories':[150, 80, 200, 90]
    },
    {
        'name':'Nasi Goreng',
        'ingredients':['Rice(medium bowl)', 'Egg', 'Onion', 'Garlic', 'Chili', 'Shrimp', 'Cumin', 'Coriander', 'Salt', 'Pepper'],
        'calories':[136, 90, 54, 4, 6, 130, 3, 3, 1, 1]
    },
    {
        'name':'Nasi Lemak',
        'ingredients':['Rice(medium bowl)', 'Hard-Boiled Egg(100g)', 'Sunny Side Up Egg', 'Fried Anchovies(1 teaspoon)', 'Cucumber(1 slice)', 'Roasted Peanuts(1 teaspoon)'],
        'calories':[136, 155, 97, 280, 16, 50]
    },
    {
        'name':'Popiah',
        'ingredients':['Turnip(100g)', 'Carrot(100g)', 'Cucumber(1 slice)', 'Onion', 'Garlic', 'Cilantro', 'Shrimp', 'Egg', 'Flour', 'Salt'],
        'calories':[36, 30, 18, 54, 4, 3, 130, 90, 120, 1]
    },
    {
        'name':'Roti Canai',
        'ingredients':['Flour(100g)', 'Coconut Milk(100g)', 'Egg', 'Salt(100g)', 'Butter(1 table spoon)', 'Yeast(12g)'],
        'calories':[120, 350, 90, 1, 80, 39]
    },
    {
        'name':'Satay',
        'ingredients':['Chicken', 'Onion(100g)', 'Garlic(100g)', 'Cumin(1 teaspoon)', 'Turmeric(1 teaspoon)', 'Lemongrass'],
        'calories':[200, 54, 4, 3, 3, 3]
}
]