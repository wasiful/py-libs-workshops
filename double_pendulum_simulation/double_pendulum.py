import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Double Pendulum Simulation")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Define pendulum parameters
L1 = 200  # Length of the first rod
L2 = 200  # Length of the second rod
m1 = 40   # Mass of the first pendulum
m2 = 40   # Mass of the second pendulum
g = 9.81  # Acceleration due to gravity

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
    x1 = L1 * np.sin(theta1) + width // 2
    y1 = L1 * np.cos(theta1) + height // 4
    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 + L2 * np.cos(theta2)
    return x1, y1, x2, y2

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    theta1, theta2, omega1, omega2 = calculate_next_position(theta1, theta2, omega1, omega2, dt)
    x1, y1, x2, y2 = polar_to_cartesian(L1, L2, theta1, theta2)

    # Draw the rods
    pygame.draw.line(screen, black, (width // 2, height // 4), (x1, y1), 2)
    pygame.draw.line(screen, black, (x1, y1), (x2, y2), 2)

    # Draw the masses
    pygame.draw.circle(screen, black, (int(x1), int(y1)), m1 // 2)
    pygame.draw.circle(screen, black, (int(x2), int(y2)), m2 // 2)

    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()
