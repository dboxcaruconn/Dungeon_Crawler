# Re-importing necessary libraries and redefining functions after reset
import pandas as pd
import random
import pandasgui as pg 
import plotly.express as px
from sklearn.linear_model import LinearRegression

def dmg(x, y):
    min_val = (1) * (1 + y)
    max_val = (x) * (1 + y)
    return round(random.uniform(min_val, max_val))

# Initialize the dataset
data = {
    'damage_base': [],
    'damage_bonus': [],
    'average_difference': []
}

# Populate the dataset with the specified ranges and calculations
for base in range(4, 13):  # damage_base from 4 to 12 inclusive
    for bonus in [i * 0.1 for i in range(-5, 6)]:  # damage_bonus from -0.5 to 0.5
        results = [dmg(base, bonus) for _ in range(100000)]
        average_damage = sum(results) / len(results)
        average_difference = (average_damage / (base / 2 + 0.5) - 1)
        data['damage_base'].append(base)
        data['damage_bonus'].append(bonus)
        data['average_difference'].append(average_difference)

# Convert to DataFrame
df = pd.DataFrame(data)


# Initialize the dataset for coefficients and intercepts
coeff_intercept_data = {
    'damage_base': [],
    'damage_bonus_coef': [],
    'intercept': []
}

# Calculate coefficients and intercepts for damage bases 4 through 12
for base in range(4, 13):
    filtered_df = df[df['damage_base'] == base]
    X = filtered_df[['damage_bonus']]
    y = filtered_df['average_difference']
    model = LinearRegression()
    model.fit(X, y)
    coefficients = model.coef_
    intercept = model.intercept_
    coeff_intercept_data['damage_base'].append(base)
    coeff_intercept_data['damage_bonus_coef'].append(coefficients[0])
    coeff_intercept_data['intercept'].append(intercept)

# Convert to DataFrame
coeff_intercept_df = pd.DataFrame(coeff_intercept_data)

# Display the DataFrame using pandasgui
#pg.show(df)

fig = px.scatter(df, 
                 x='damage_base', 
                 y='average_difference', 
                 color='damage_bonus',
                 color_continuous_scale=px.colors.sequential.Viridis, # This is optional, for custom color scale
                 title='Damage Base vs. Average Difference by Damage Bonus')

fig.show()



