import matplotlib.pyplot as plt
import numpy as np

x = list(range((4)))
y = list(range((4)))

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(x,y)  # Plot some data on the axes.
plt.show()


