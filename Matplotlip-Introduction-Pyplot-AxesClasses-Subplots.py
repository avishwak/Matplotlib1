import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = [5, 2, 9, 4, 7]
y = [10, 4, 5, 6, 3]

# line plot
plt.plot(x, y)
plt.show()

# bar plot
plt.bar(x,y)
plt.show()

# histogram
plt.hist(y) #frequency 
plt.show()

# scatter plot
plt.scatter(x, y)
plt.show()

# other attribues
plt.plot(x, y, 's')  # 's' for square markers, you can use 'o' for circles, '^' for triangles, 
plt.show()

# axis limits
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.axis([0, 6, 0, 20]) # x-axis from 0 to 6, y-axis from 0 to 20
plt.show()

# axis labels and title
year = [1972, 1982, 1992, 2002, 2012]
e_india = [100.6, 158.61, 245.78, 300.02, 350.20]
e_bangladesh = [10.5, 20.6, 55.89, 60.98, 100.2]
plt.plot(year, e_india, label='India', color = 'orange', linestyle='dashed')
plt.plot(year, e_bangladesh, label='Bangladesh', marker = 'o', markersize=3, color = 'g')
plt.xlabel('Year')
plt.ylabel('Electricity Consumption in kWH')
plt.title('Electricity Consumption')
plt.legend()
plt.show()

"""
- figures: it is a container for all the plots
- it can contain multiple axes (subplots)
- axes: it is a container for a single plot
# in the axes we can have axis and plots
fig = plt.figure()
# axes: left, bottom, width, height in range(0, 1)
ax = plt.axes([0.1, 0.1, 0.8, 0.8]) # 10% from left, 10% from bottom, 80% width, 80% height
"""

# create the dataset
x = np.linspace(-np.pi, np.pi, 20) # 20 points from -pi to pi equally spaced
C = np.cos(x)
S = np.sin(x)

fig = plt.figure()
ax = plt.axes([0.1, 0.1, 0.8, 0.8])
ax1 = ax.plot(x, S, 'bs:') # blue square markers with a dashed line #CML: color marker linestyle
ax2 = ax.plot(x, C, 'ro-') 
ax.legend(labels = ('Sine Function', 'Cosine Function'), loc = 'upper left')
plt.show()

# two subplots: plt.subplots() creates subplots
x = [1, 2, 3]
y = [0, 1, 0]
z = [1, 0, 1]
fig, ax = plt.subplots(2)
ax[0].plot(x, y)
ax[1].plot(x, z)
ax[0].set_xlabel('X1')
ax[0].set_ylabel('Y')
ax[1].set_xlabel('X2')
ax[1].set_ylabel('Z')
ax[0].set_title('X vs Y')
ax[1].set_title('X vs Z')
plt.tight_layout() # to avoid overlapping of the subplots
plt.show()


x = np.arange(0.0, 2.0, 0.01)
y = 1 + np.sin(2 * np.pi * x)

fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3)  # 6 subplots in a 2x3 grid rowxcol
# fig, ((ax1, ax2), (ax4, ax5), (ax6, ax3)) = plt.subplots(3, 2)  # 6

ax1.plot(x, y, color='orange')
ax2.plot(x, y, color='g')
ax3.plot(x, y, color='blue')
ax4.plot(x, y, color='red')
ax5.plot(x, y, color='magenta')
ax6.plot(x, y, color='black')

ax1.set_xlabel('X')
ax2.set_ylabel('Y')

plt.tight_layout()
plt.show()

df = pd.read_csv('Churn_Modelling.csv')
df['Gender'].value_counts()
gender = df.groupby(['Gender']).size().reset_index(name='count') # creates a dataframe with gender counts
plt.bar(gender['Gender'], gender['count'])
# directly from the original dataframe
plt.hist(df['Gender'])