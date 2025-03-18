import numpy as np
import matplotlib.pyplot as plt


xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints,color='r',label='x^2')
plt.title('Random Plot')
plt.xlabel('Salaries')
plt.ylabel('age')
plt.legend()
plt.savefig('prettier-plot.png')
plt.show()