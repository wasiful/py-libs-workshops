import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

# Create some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)
data = pd.DataFrame({
    'X': x,
    'Y': y,
    'Z': z,
    'Category': np.random.choice(['A', 'B', 'C'], size=100),
    'Value': np.random.randn(100)
})

# Create a figure and a grid of subplots
fig, axs = plt.subplots(4, 3, figsize=(15, 15))

# 1. Line Plot
axs[0, 0].plot(x, y, label='sin(x)', color='blue')
axs[0, 0].plot(x, z, label='cos(x)', color='red')
axs[0, 0].set_title('Line Plot')
axs[0, 0].legend()

# 2. Scatter Plot
scatter = axs[0, 1].scatter(data['X'], data['Y'], c=pd.factorize(data['Category'])[0], cmap='viridis', s=50)
axs[0, 1].set_title('Scatter Plot')
fig.colorbar(scatter, ax=axs[0, 1])

# 3. Bar Plot
categories = ['A', 'B', 'C']
values = [data[data['Category'] == cat].shape[0] for cat in categories]
axs[0, 2].bar(categories, values, color=['red', 'green', 'blue'])
axs[0, 2].set_title('Bar Plot')

# 4. Histogram
axs[1, 0].hist(y, bins=15, alpha=0.7, label='sin(x)')
axs[1, 0].hist(z, bins=15, alpha=0.7, label='cos(x)')
axs[1, 0].set_title('Histogram')
axs[1, 0].legend()

# 5. Box Plot
axs[1, 1].boxplot([data['Y'], data['Z']], labels=['sin(x)', 'cos(x)'])
axs[1, 1].set_title('Box Plot')

# 6. Pie Chart
pie_sizes = [sum(data['Category'] == cat) for cat in categories]
axs[1, 2].pie(pie_sizes, labels=categories, autopct='%1.1f%%', colors=['red', 'green', 'blue'])
axs[1, 2].set_title('Pie Chart')

# 7. 3D Plot
ax3d = fig.add_subplot(437, projection='3d')
ax3d.plot3D(x, y, z, label='3D Line')
ax3d.scatter3D(data['X'], data['Y'], data['Z'], c=data['X'], cmap='inferno')
ax3d.set_title('3D Plot')

# 8. Contour Plot
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
contour = axs[2, 0].contourf(X, Y, Z, cmap='coolwarm')
fig.colorbar(contour, ax=axs[2, 0])
axs[2, 0].set_title('Contour Plot')

# 9. Heatmap
heatmap_data = np.random.rand(10, 12)
heatmap = axs[2, 1].imshow(heatmap_data, cmap='viridis', aspect='auto')
fig.colorbar(heatmap, ax=axs[2, 1])
axs[2, 1].set_title('Heatmap')

# 10. Polar Plot
theta = np.linspace(0, 2.*np.pi, 100)
r = np.abs(np.sin(theta))
axs[2, 2] = plt.subplot(4, 3, 9, polar=True)
axs[2, 2].plot(theta, r)
axs[2, 2].set_title('Polar Plot')

# 11. Quiver Plot
X, Y = np.meshgrid(np.arange(-2, 2, 0.2), np.arange(-2, 2, 0.2))
U = -1 - X**2 + Y
V = 1 + X - Y**2
axs[3, 0].quiver(X, Y, U, V, color='blue')
axs[3, 0].set_title('Quiver Plot')

# 12. Streamplot
Y, X = np.mgrid[-3:3:100j, -3:3:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
axs[3, 1].streamplot(X, Y, U, V, color=np.sqrt(U**2 + V**2), cmap='autumn')
axs[3, 1].set_title('Streamplot')

# 13. Stem Plot
axs[3, 2].stem(x, y, basefmt=" ")
axs[3, 2].set_title('Stem Plot')

# Set a tight layout to avoid overlaps
plt.tight_layout()

# Save the figure
fig.savefig('all_plots.png', dpi=300)

# Show plots
plt.show()
