import numpy as np
import matplotlib.pyplot as plt
min_salary = 20000
max_salary = 80000
number_of_entries = 10
# setup seed
np.random.seed(42)
salaries = np.random.randint(min_salary,max_salary,number_of_entries)
ages = np.random.randint(21,65,number_of_entries)

print(salaries)

# now add 5000 to each salary
salaries_plus = salaries + 5000
print(salaries_plus)

# now add 5% to each salary
salaries_plus5 = salaries * 1.05
print(salaries_plus5)

#plt.hist(salaries, bins=100, color='blue')
plt.show()