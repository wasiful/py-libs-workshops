import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))

# Plot the first subplot
ax1.plot(x, y1)
ax1.set_title('Sine')

# Plot the second subplot
ax2.plot(x, y2)
ax2.set_title('Cosine')

plt.tight_layout()
plt.show()
