import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
from scipy.integrate import solve_ivp

# Parameters
g = 9.81  # acceleration due to gravity (m/s^2)
L = 1.0   # length of the pendulum (m)

# Function to compute the derivatives
def pendulum_derivatives(t, y, omega):
    theta, omega_dot = y
    dydt = [omega_dot, - omega**2 * np.sin(theta)]  # Omega squared affects the frequency
    return dydt

# Function to solve the pendulum equations
def solve_pendulum(omega, t_max=10, num_points=1000):
    # Initial conditions
    theta0 = 0.1  # initial angle (radians)
    omega0 = 0.0  # initial angular velocity
    y0 = [theta0, omega0]
    
    # Time array
    t = np.linspace(0, t_max, num_points)
    
    # Solve ODE
    sol = solve_ivp(pendulum_derivatives, [0, t_max], y0, t_eval=t, args=(omega,))
    
    return sol.t, sol.y[0]  # return time and angle

# Plot setup
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.25, top=0.9, hspace=0.4)

# Initial data setup
t_init = np.linspace(0, 10, 1000)
theta_init = np.zeros_like(t_init)
pendulum_line, = ax1.plot([], [], 'ro-', lw=2)
cosine_curve, = ax2.plot([], [], 'r-', lw=2)
time_text = ax1.text(0.02, 0.95, '', transform=ax1.transAxes)

# Set up axes
ax1.set_xlim(-1.5, 1.5)
ax1.set_ylim(-1.5, 1.5)
ax1.set_xlabel('X position (m)')
ax1.set_ylabel('Y position (m)')
ax1.set_title('Pendulum Motion')
ax1.set_aspect('equal')

ax2.set_xlim(0, 10)
ax2.set_ylim(-0.2, 0.2)
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Angle (rad)')
ax2.set_title('Cosine Curve of Angle')

# Slider setup
axcolor = 'lightgoldenrodyellow'
ax_omega = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor=axcolor)
s_omega = Slider(ax_omega, 'Frequency', 0.1, 2.0, valinit=1.0)

# Initialize function for animation
def init():
    pendulum_line.set_data([], [])
    cosine_curve.set_data([], [])
    return pendulum_line, cosine_curve

# Update function for animation
def update(frame):
    omega = s_omega.val  # Get current value from slider
    t_max = 10
    num_points = 1000
    
    # Solve pendulum ODE with current frequency
    t, theta = solve_pendulum(omega, t_max, num_points)
    
    # Calculate the current state of the pendulum
    x = L * np.sin(theta[frame])
    y = -L * np.cos(theta[frame])
    
    # Update pendulum position plot
    pendulum_line.set_data([0, x], [0, y])
    
    # Update cosine curve plot
    cosine_curve.set_data(t[:frame], theta[:frame])
    
    # Update time text
    time_text.set_text(f'Frequency: {omega:.2f} rad/s')
    
    return pendulum_line, cosine_curve

# Animation function
def animate(frame):
    return update(frame)

# Set up the animation
ani = FuncAnimation(fig, animate, frames=1000, interval=20, repeat=True, init_func=init, blit=True)

# Slider update function
def slider_update(val):
    ani.event_source.stop()
    ani.event_source.start()

s_omega.on_changed(slider_update)

plt.show()
