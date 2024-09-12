import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

matplotlib.use('TkAgg')

# Set up data
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)
data = pd.DataFrame({'X': x, 'Y': y, 'Z': z, 'Category': np.random.choice(['A', 'B', 'C'], size=100)})

# Create a figure and a set of subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Line plot
axs[0, 0].plot(x, y, label='sin(x)', color='blue')
axs[0, 0].plot(x, z, label='cos(x)', color='red')
axs[0, 0].set_title('Line Plot')
axs[0, 0].set_xlabel('X Axis')
axs[0, 0].set_ylabel('Y Axis')
axs[0, 0].legend()

# Scatter plot with customization
scatter = axs[0, 1].scatter(data['X'], data['Y'], c=pd.factorize(data['Category'])[0], cmap='viridis', s=100)
axs[0, 1].set_title('Scatter Plot')
axs[0, 1].set_xlabel('X Axis')
axs[0, 1].set_ylabel('Y Axis')
fig.colorbar(scatter, ax=axs[0, 1], label='Category')

# 3D plot
ax3d = fig.add_subplot(223, projection='3d')
ax3d.plot3D(x, y, z, label='3D Line')
ax3d.scatter3D(data['X'], data['Y'], data['Z'], c=data['X'], cmap='inferno')
ax3d.set_title('3D Plot')
ax3d.set_xlabel('X Axis')
ax3d.set_ylabel('Y Axis')
ax3d.set_zlabel('Z Axis')

# Histogram
axs[1, 1].hist(y, bins=15, alpha=0.7, label='sin(x)')
axs[1, 1].hist(z, bins=15, alpha=0.7, label='cos(x)')
axs[1, 1].set_title('Histogram')
axs[1, 1].set_xlabel('Value')
axs[1, 1].set_ylabel('Frequency')
axs[1, 1].legend()

# Set a tight layout
plt.tight_layout()

# Animation: Updating a line plot over time
fig_anim, ax_anim = plt.subplots()
line, = ax_anim.plot(x, np.sin(x), color='green')
ax_anim.set_xlim(0, 10)
ax_anim.set_ylim(-1, 1)
ax_anim.set_title('Animated Line Plot')
ax_anim.set_xlabel('X Axis')
ax_anim.set_ylabel('Y Axis')

def update(frame):
    line.set_ydata(np.sin(x + frame / 10.0))
    return line,

ani = FuncAnimation(fig_anim, update, frames=np.arange(0, 100, 1), blit=True, interval=100)

# Save the animation as a gif
ani.save('animated_plot.gif', writer='imagemagick')

# Save the figure
fig.savefig('multi_plot_figure.png', dpi=300)

# Show plots
plt.show()
