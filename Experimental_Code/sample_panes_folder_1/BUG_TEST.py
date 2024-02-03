import matplotlib.pyplot as plt
import random

def dmg(x, y):
    return max(round((random.random() + y*0.83 - 0.02*y*x) * x + 0.5),1)

damage_base = 10             # x
damage_bonus = -0.15         # y

# Running 100,000 cases
results = [dmg(damage_base, damage_bonus) for _ in range(100000)]

# Calculating the average damage
average_damage = sum(results) / len(results)
average_difference = (average_damage / (damage_base/2 + 0.5) - 1)*100

# Plotting the histogram
plt.hist(results, bins=range(min(results), max(results) + 2), align='left', edgecolor='black')
plt.title('Damage Distribution for ' + str(damage_base) + '-dmg weapon with ' + str(damage_bonus*100) + '% bonus')
plt.xlabel('Damage')
plt.ylabel('Frequency')
plt.xticks(range(min(results), max(results) + 1))
plt.axvline(average_damage, color='red', linestyle='dashed', linewidth=1)
plt.text(average_damage, plt.ylim()[1] * 0.9, 'Average Damage: {:.2f}'.format(average_damage), color='red')
plt.text(average_damage, plt.ylim()[1] * 0.8, 'Difference %: {:.2f}'.format(average_difference), color='red')
plt.show()

print('Average damage:', average_damage)