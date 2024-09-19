import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

# Constants
g = 9.81  # Gravitational acceleration

# Function to calculate the position of the pendulum with deformation (arch)
def calculate_pendulum_position(theta, L, deformation):
    num_points = 100  # Number of points along the beam
    y = np.linspace(0, -L, num_points)
    x = np.zeros_like(y)
    z = np.zeros_like(y)

    arch_amplitude = deformation * L * 0.5  # Arching effect
    x = arch_amplitude * np.sin(np.linspace(0, np.pi, num_points))
    z = arch_amplitude * np.cos(np.linspace(0, np.pi, num_points)) - arch_amplitude

    x_rotated = x * np.cos(theta) - y * np.sin(theta)
    y_rotated = x * np.sin(theta) + y * np.cos(theta)

    return x_rotated, y_rotated, z

# Function to calculate velocity2 and center of mass and gravity
def calculate_velocity2_and_center_of_gravity(theta, L, deformation, velocity):
    velocity2 = velocity * (1 - deformation)  # Relation for demonstration
    num_points = 100
    y = np.linspace(0, -L, num_points)
    y_avg = np.mean(y * (1 - deformation))  # Adjust the center of gravity for deformation
    center_of_gravity = abs(y_avg)

    x, y, z = calculate_pendulum_position(theta, L, deformation)
    center_of_mass_x = np.mean(x)
    center_of_mass_y = np.mean(y)
    center_of_mass2 = np.sqrt(center_of_mass_x**2 + center_of_mass_y**2)

    return velocity2, center_of_gravity, center_of_mass2

# Pendulum plot update function for animation
def update_pendulum(frame, line, velocity, L, deformation, ax, velocity_display, cog_display, com2_display):
    # Set minimum velocity to stop motion if velocity is very low
    if velocity < 0.01:
        velocity = 0

    velocity2, center_of_gravity, center_of_mass2 = calculate_velocity2_and_center_of_gravity(np.pi / 4, L, deformation, velocity)
    
    # Adjust angular frequency based on velocity; larger velocity -> faster motion
    omega = np.sqrt(g / center_of_gravity) * velocity

    # Update pendulum motion based on angular frequency and velocity
    theta = np.pi / 4 * np.cos(omega * frame / 10)

    x, y, z = calculate_pendulum_position(theta, L, deformation)

    line.set_data(x, y)
    line.set_3d_properties(z)

    velocity_display.set_text(f"Velocity2: {velocity2:.2f}")
    cog_display.set_text(f"Center of Gravity: {center_of_gravity:.2f}")
    com2_display.set_text(f"Center of Mass2: {center_of_mass2:.2f}")

    return line

# COG and COM plot update function for animation
def update_cog_com(frame, L, deformation, velocity, cog_data, com2_data, velocity_data, cog_plot, com2_plot, velocity_plot):
    velocity2, center_of_gravity, center_of_mass2 = calculate_velocity2_and_center_of_gravity(np.pi / 4, L, deformation, velocity)

    cog_data.append(center_of_gravity)
    com2_data.append(center_of_mass2)
    velocity_data.append(velocity2)

    if len(cog_data) > 300:
        cog_data.pop(0)
        com2_data.pop(0)
        velocity_data.pop(0)

    cog_plot.set_data(range(len(cog_data)), cog_data)
    com2_plot.set_data(range(len(com2_data)), com2_data)
    velocity_plot.set_data(range(len(velocity_data)), velocity_data)

    cog_ax.set_xlim(0, len(cog_data))
    cog_ax.set_ylim(min(cog_data) - 0.1, max(cog_data) + 0.1)
    com2_ax.set_xlim(0, len(com2_data))
    com2_ax.set_ylim(min(com2_data) - 0.1, max(com2_data) + 0.1)
    velocity_ax.set_xlim(0, len(velocity_data))
    velocity_ax.set_ylim(min(velocity_data) - 0.1, max(velocity_data) + 0.1)

    return cog_plot, com2_plot, velocity_plot

# Main function to initialize the plots and sliders
def interactive_pendulum():
    fig1 = plt.figure(figsize=(10, 8))

    ax1 = fig1.add_subplot(111, projection='3d')
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    ax1.set_zlim(-2, 2)
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')

    L = 2.0  # Length of the pendulum
    velocity = 1.0  # Initial velocity
    deformation = 0.1  # Initial deformation

    x, y, z = calculate_pendulum_position(np.pi / 4, L, deformation)
    line1, = ax1.plot(x, y, z, color='black', lw=3)

    velocity_display = ax1.text2D(0.05, 0.95, "Velocity2: 0.00", transform=ax1.transAxes)
    cog_display = ax1.text2D(0.05, 0.90, "Center of Gravity: 0.00", transform=ax1.transAxes)
    com2_display = ax1.text2D(0.05, 0.85, "Center of Mass2: 0.00", transform=ax1.transAxes)

    ax_velocity = plt.axes([0.2, 0.02, 0.65, 0.03], facecolor='lightgoldenrodyellow', figure=fig1)
    ax_deformation = plt.axes([0.2, 0.06, 0.65, 0.03], facecolor='lightgoldenrodyellow', figure=fig1)

    velocity_slider = Slider(ax_velocity, 'Velocity', 0.0, 5.0, valinit=velocity)
    deformation_slider = Slider(ax_deformation, 'Deformation', 0.0, 0.5, valinit=deformation)

    fig2 = plt.figure(figsize=(10, 7))

    global cog_ax
    cog_ax = fig2.add_subplot(311)
    cog_ax.set_title("COG over Time")
    cog_ax.set_xlabel("Frame")
    cog_ax.set_ylabel("Center of Gravity")
    cog_data = []
    cog_plot, = cog_ax.plot([], [], lw=2)

    global com2_ax
    com2_ax = fig2.add_subplot(312)
    com2_ax.set_title("COM over Time")
    com2_ax.set_xlabel("Frame")
    com2_ax.set_ylabel("Center of Mass")
    com2_data = []
    com2_plot, = com2_ax.plot([], [], lw=2)

    global velocity_ax
    velocity_ax = fig2.add_subplot(313)
    velocity_ax.set_title("Velocity over Time")
    velocity_ax.set_xlabel("Frame")
    velocity_ax.set_ylabel("Velocity2")
    velocity_data = []
    velocity_plot, = velocity_ax.plot([], [], lw=2)

    def animate_pendulum(frame):
        return update_pendulum(frame, line1, velocity_slider.val, L, deformation_slider.val, ax1, velocity_display, cog_display, com2_display)

    def animate_cog_com(frame):
        return update_cog_com(frame, L, deformation_slider.val, velocity_slider.val, cog_data, com2_data, velocity_data, cog_plot, com2_plot, velocity_plot)

    ani_pendulum = FuncAnimation(fig1, animate_pendulum, frames=300, interval=50, blit=False)
    ani_cog_com = FuncAnimation(fig2, animate_cog_com, frames=300, interval=50, blit=False)

    def update_slider(val):
        fig1.canvas.draw_idle()
        fig2.canvas.draw_idle()

    velocity_slider.on_changed(update_slider)
    deformation_slider.on_changed(update_slider)

    plt.show()

# Call the interactive pendulum function
interactive_pendulum()
