import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Data preparation
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)
X, Y = np.meshgrid(np.linspace(-5, 5, 50), np.linspace(-5, 5, 50))
Z = np.sin(np.sqrt(X**2 + Y**2))

# Plotting
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(14, 10), dpi=100)

# Subplot 1: Line plot
axs[0, 0].plot(x, y, color='blue', linestyle='-', linewidth=2, marker='o', markersize=5, label='Sine wave')
axs[0, 0].set_title('Line Plot', fontsize=14, fontweight='bold', color='blue', loc='center', pad=10)
axs[0, 0].legend(loc='best', fontsize=12, title='Legend', shadow=True, fancybox=True, ncol=1)

# Subplot 2: Scatter plot
sc = axs[0, 1].scatter(x, y, c=z, marker='x', s=100, label='Scatter', alpha=0.7, cmap='viridis')
axs[0, 1].set_title('Scatter Plot', fontsize=14, fontweight='bold', color='blue', loc='center', pad=10)
plt.colorbar(sc, ax=axs[0, 1], orientation='vertical', fraction=0.05, pad=0.04, aspect=20, shrink=0.9)

# Subplot 3: Bar plot
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 7]
axs[1, 0].bar(categories, values, width=0.6, color='blue', edgecolor='black', align='center', label='Bar')
axs[1, 0].set_title('Bar Plot', fontsize=14, fontweight='bold', color='blue', loc='center', pad=10)
axs[1, 0].legend(loc='best', fontsize=12, title='Legend', shadow=True, fancybox=True)

# Subplot 4: Pie chart
sizes = [15, 30, 45, 10]
labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
axs[1, 1].pie(sizes, explode=(0.1, 0, 0, 0), labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
axs[1, 1].set_title('Pie Chart', fontsize=14, fontweight='bold', color='blue', loc='center', pad=10)

# 3D Plot
fig = plt.figure(figsize=(8, 6), dpi=100)
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(x, y, z, c=z, marker='o')
ax.plot3D(x, y, z, color='blue', linestyle='-', linewidth=2)
ax.set_title('3D Scatter and Line Plot')

# Contour Plot
fig, ax = plt.subplots(figsize=(6, 6), dpi=100)
contour = ax.contour(X, Y, Z, levels=10, colors='black', linestyles='solid', linewidths=1)
ax.set_title('Contour Plot', fontsize=14, fontweight='bold', color='blue', loc='center', pad=10)
plt.colorbar(contour, ax=ax, orientation='vertical', fraction=0.05, pad=0.04, aspect=20, shrink=0.9)

# Image plot with imshow
fig, ax = plt.subplots(figsize=(6, 6), dpi=100)
image = ax.imshow(Z, cmap='viridis', interpolation='nearest', aspect='auto', extent=[-5, 5, -5, 5], origin='lower')
ax.set_title('Image Plot', fontsize=14, fontweight='bold', color='blue', loc='center', pad=10)
plt.colorbar(image, ax=ax, orientation='vertical', fraction=0.05, pad=0.04, aspect=20, shrink=0.9)

# Boxplot
data = np.random.rand(10, 5)
fig, ax = plt.subplots(figsize=(6, 6), dpi=100)
ax.boxplot(data, notch=True, vert=True, patch_artist=True, boxprops=dict(facecolor='blue', color='black'))
ax.set_title('Boxplot', fontsize=14, fontweight='bold', color='blue', loc='center', pad=10)

# Histogram
fig, ax = plt.subplots(figsize=(6, 6), dpi=100)
ax.hist(y, bins=10, density=False, color='blue', alpha=0.7, label='Histogram')
ax.set_title('Histogram', fontsize=14, fontweight='bold', color='blue', loc='center', pad=10)
ax.legend(loc='best', fontsize=12, title='Legend', shadow=True, fancybox=True)

# Quiver Plot
fig, ax = plt.subplots(figsize=(6, 6), dpi=100)
U, V = np.sin(X), np.cos(Y)
ax.quiver(X, Y, U, V, color='blue', scale=20)
ax.set_title('Quiver Plot', fontsize=14, fontweight='bold', color='blue', loc='center', pad=10)

# Streamplot
fig, ax = plt.subplots(figsize=(6, 6), dpi=100)
ax.streamplot(X, Y, U, V, color='blue', linewidth=1, density=1, arrowstyle='-|>', minlength=0.1)
ax.set_title('Streamplot', fontsize=14, fontweight='bold', color='blue', loc='center', pad=10)

# Polar Plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(6, 6), dpi=100)
theta = 2 * np.pi * x
r = y
ax.plot(theta, r, color='blue', linestyle='-', linewidth=2, marker='o')
ax.set_title('Polar Plot', fontsize=14, fontweight='bold', color='blue', loc='center', pad=10)

# Barbs Plot
fig, ax = plt.subplots(figsize=(6, 6), dpi=100)
ax.barbs(X, Y, U, V, length=7, pivot='middle', barbcolor='blue', flagcolor='red', sizes=dict(emptybarb=0.1, spacing=0.2))
ax.set_title('Barbs Plot', fontsize=14, fontweight='bold', color='blue', loc='center', pad=10)

# Annotate example
fig, ax = plt.subplots(figsize=(6, 6), dpi=100)
ax.plot(x, y, label='Sine wave')
ax.annotate('Max', xy=(np.pi/2, 1), xytext=(np.pi/2 + 1, 1.5), arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)
ax.set_title('Annotation Example', fontsize=14, fontweight='bold', color='blue', loc='center', pad=10)

# Save the figure
fig.savefig('matplotlib_overview.png', dpi=300, format='png', bbox_inches='tight', pad_inches=0.1)

# Show all plots
plt.show()
