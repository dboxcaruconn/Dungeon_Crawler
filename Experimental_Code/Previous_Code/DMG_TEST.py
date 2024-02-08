import matplotlib.pyplot as plt
import random

def dmg(x, y, z):
    return round(random.uniform((1 + z)*(1 + y), (x + z)*(1 + y)))

damage_die = 8               # x
damage_bonus = .05           # y
damage_flat = 0              # z

# Running 100,000 cases
results = [dmg(damage_die, damage_bonus, damage_flat) for _ in range(100000)]

# Calculating the average damage
average_damage = sum(results) / len(results)
expected_damage = (damage_die/2 + 0.5 + damage_flat)
average_difference = (average_damage / expected_damage - 1)*100

# Plotting the histogram
plt.hist(results, bins=range(min(results), max(results) + 2), align='left', color='black', edgecolor='black')
plt.title('Damage Distribution for 1d' + str(damage_die) + '+' + str(damage_flat) + ' with ' + str(damage_bonus*100) + '% bonus')
plt.xlabel('Damage')
plt.ylabel('Frequency')
plt.xticks(range(min(results), max(results) + 1))
plt.axvline(expected_damage, color='green', linestyle='dashed', linewidth=1)
plt.text(expected_damage, plt.ylim()[1] * 0.3, ' {:.2f}'.format(expected_damage), color='green')
plt.axvline(average_damage, color='red', linestyle='dashed', linewidth=1)
plt.text(average_damage, plt.ylim()[1] * 0.5, ' Average Damage: {:.2f}'.format(average_damage), color='red')
plt.text(average_damage, plt.ylim()[1] * 0.4, ' Difference %: {:.2f}'.format(average_difference), color='red')
plt.show()

print('Average damage:', average_damage)