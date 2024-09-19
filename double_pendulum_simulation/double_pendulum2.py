import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

matplotlib.use('TkAgg')  # Use TkAgg backend for Matplotlib

# Pendulum parameters
L1 = 1.0  # Length of the first rod (in meters)
L2 = 1.0  # Length of the second rod (in meters)
m1 = 1.0  # Mass of the first pendulum (in kg)
m2 = 1.0  # Mass of the second pendulum (in kg)
g = 9.81  # Acceleration due to gravity (in m/s^2)

# Initial angles (in radians)
theta1 = np.pi / 2
theta2 = np.pi / 2

# Angular velocities
omega1 = 0.0
omega2 = 0.0

# Time step
dt = 0.05


# Function to calculate the next position
def calculate_next_position(theta1, theta2, omega1, omega2, dt):
    num1 = -g * (2 * m1 + m2) * np.sin(theta1)
    num2 = -m2 * g * np.sin(theta1 - 2 * theta2)
    num3 = -2 * np.sin(theta1 - theta2) * m2
    num4 = omega2**2 * L2 + omega1**2 * L1 * np.cos(theta1 - theta2)
    denom = L1 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2))
    a1 = (num1 + num2 + num3 * num4) / denom

    num1 = 2 * np.sin(theta1 - theta2)
    num2 = omega1**2 * L1 * (m1 + m2)
    num3 = g * (m1 + m2) * np.cos(theta1)
    num4 = omega2**2 * L2 * m2 * np.cos(theta1 - theta2)
    denom = L2 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2))
    a2 = (num1 * (num2 + num3 + num4)) / denom

    omega1 += a1 * dt
    omega2 += a2 * dt
    theta1 += omega1 * dt
    theta2 += omega2 * dt

    return theta1, theta2, omega1, omega2

# Function to convert polar to cartesian coordinates
def polar_to_cartesian(L1, L2, theta1, theta2):
    x1 = L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)
    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 - L2 * np.cos(theta2)
    return x1, y1, x2, y2

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

line, = ax.plot([], [], 'o-', lw=2)
trace, = ax.plot([], [], '-', lw=1, alpha=0.5)
x_data, y_data = [], []

# Initialization function for the animation
def init():
    line.set_data([], [])
    trace.set_data([], [])
    return line, trace

# Update function for the animation
def update(frame):
    global theta1, theta2, omega1, omega2
    theta1, theta2, omega1, omega2 = calculate_next_position(theta1, theta2, omega1, omega2, dt)
    x1, y1, x2, y2 = polar_to_cartesian(L1, L2, theta1, theta2)

    line.set_data([0, x1, x2], [0, y1, y2])
    x_data.append(x2)
    y_data.append(y2)
    trace.set_data(x_data, y_data)

    return line, trace

# Create the animation
ani = FuncAnimation(fig, update, frames=600, init_func=init, blit=True, interval=20)

plt.show()
