# Re-importing necessary libraries and redefining functions after reset
import pandas as pd
import random
import pandasgui as pg 
from sklearn.linear_model import LinearRegression

def dmg(x, y):
    return max(round((random.random() + 0.83*y - 0.02*y*x) * x + 0.5), 1)

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
pg.show(df)

# Perform new linear regression
X_new = coeff_intercept_df[['damage_base']]
y_new = coeff_intercept_df['damage_bonus_coef']
model_new = LinearRegression()
model_new.fit(X_new, y_new)
coefficients_new = model_new.coef_
intercept_new = model_new.intercept_

# Display the new coefficients and intercept
print("New Coefficients:", coefficients_new)
print("New Intercept:", intercept_new)




