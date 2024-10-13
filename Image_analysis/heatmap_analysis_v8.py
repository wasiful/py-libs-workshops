import svgwrite
import numpy as np
from PIL import Image
import math
import matplotlib.pyplot as plt

# Define a function to compute the gradient direction in degrees
def compute_gradient_direction(dx, dy):
    """Compute gradient direction in degrees from dx, dy."""
    angle = math.degrees(math.atan2(dy, dx))
    return angle if angle >= 0 else angle + 360

# Define a function to create the SVG file and plot arrow population
def process_image_to_svg_and_plot(image_path, output_svg_path, grid_size_mm=5, resolution_dpi=300, arrow_size=5):
    """
    Process the image to analyze color transitions in grid_size_mm x grid_size_mm boxes, 
    generate an SVG with arrows, and plot the population density of angles.
    
    Parameters:
    - image_path (str): Path to the input image.
    - output_svg_path (str): Path to save the output SVG file.
    - grid_size_mm (int): Size of each grid cell in mm.
    - resolution_dpi (int): Resolution of the image in DPI (dots per inch).
    - arrow_size (int): Length of the arrows in the SVG.
    """
    # Convert mm to pixels using the DPI (dots per inch) of the image
    mm_to_inch = 25.4
    box_size_px = int((grid_size_mm / mm_to_inch) * resolution_dpi)

    # Load the image and convert to RGB
    img = Image.open(image_path).convert("RGB")
    img_np = np.array(img)
    height, width, _ = img_np.shape

    # Create the SVG drawing
    dwg = svgwrite.Drawing(output_svg_path, size=(width, height))
    dwg.add(dwg.image(image_path, insert=(0, 0), size=(width, height)))

    # Define minimum arrowhead size
    min_arrowhead_size = 5  # Minimum size for the arrowhead

    # List to store angles for histogram
    angles_list = []

    # Iterate through each box in the grid
    for y in range(0, height, box_size_px):
        for x in range(0, width, box_size_px):
            # Extract the current box
            box = img_np[y:y + box_size_px, x:x + box_size_px]

            # Compute gradients in the box using numpy's gradient function for the red channel
            red_channel = box[:, :, 0]  # Extract the red channel
            gradient_y, gradient_x = np.gradient(red_channel)

            # Compute the mean gradient in the x and y directions
            mean_dx = np.mean(gradient_x)
            mean_dy = np.mean(gradient_y)

            # Only proceed if the gradient indicates a transition from lighter red to deeper red
            if mean_dx < 0 or mean_dy < 0:
                # Calculate the gradient direction
                gradient_direction = compute_gradient_direction(mean_dx, mean_dy)

                # Convert gradient direction to the range [0, 180] degrees for the histogram
                angle_180 = gradient_direction % 180
                angles_list.append(angle_180)

                # Determine the arrow direction and length
                start_x = x + box_size_px // 2
                start_y = y + box_size_px // 2
                end_x = start_x + arrow_size * math.cos(math.radians(gradient_direction))
                end_y = start_y + arrow_size * math.sin(math.radians(gradient_direction))

                # Draw the arrow as a line
                line = dwg.line(start=(start_x, start_y), end=(end_x, end_y), stroke='black', stroke_width=2)
                dwg.add(line)

                # Calculate dynamic arrowhead size based on the size of the grid box
                arrowhead_size = max(min_arrowhead_size, arrow_size * 0.2)  # Scale based on arrow size but enforce minimum

                # Create an arrowhead at the end point
                arrowhead = dwg.polygon(
                    points=[
                        (end_x, end_y),
                        (end_x - arrowhead_size * math.cos(math.radians(gradient_direction - 30)),
                         end_y - arrowhead_size * math.sin(math.radians(gradient_direction - 30))),
                        (end_x - arrowhead_size * math.cos(math.radians(gradient_direction + 30)),
                         end_y - arrowhead_size * math.sin(math.radians(gradient_direction + 30)))
                    ],
                    fill='black'
                )
                dwg.add(arrowhead)

    # Save the SVG
    dwg.save()

    # Create the histogram of angles
    plt.figure(figsize=(8, 5))
    plt.hist(angles_list, bins=1000, range=(0, 180), edgecolor='black', alpha=0.75)
    plt.title('Arrow Direction Distribution')
    plt.xlabel('Angle (0° to 180°)')
    plt.ylabel('Count of Arrows')
    plt.grid(True)

    # Show the plot
    plt.show()

# Example usage:
process_image_to_svg_and_plot("Image_analysis/ESA_Planck_CMB.jpg", "output_with_arrows.svg", grid_size_mm=0.2, resolution_dpi=300, arrow_size=0.2)
