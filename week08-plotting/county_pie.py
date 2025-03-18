import numpy as np
import matplotlib.pyplot as plt

possible_choice = ['Mayo', 'Galway', 'Roscommon', 'Sligo', 'Leitrim', 'Donegal', 'Cavan', 'Monaghan', 'Louth', 'Meath', 'Westmeath', 'Longford', 'Offaly', 'Kildare', 'Wicklow', 'Laois', 'Carlow', 'Kilkenny', 'Wexford', 'Waterford', 'Tipperary', 'Limerick', 'Clare', 'Galway', 'Kerry', 'Cork', 'Kilkenny', 'Dublin']
counties = np.random.choice(possible_choice, 1000)
unique, counts = np.unique(counties, return_counts=True)
plt.bar(counts, height=counts)
plt.legend()
plt.show()