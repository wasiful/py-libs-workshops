import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Function to find the bright ribbon area in each frame
def find_bright_ribbon_area(frame):
    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Focus on the Value channel (brightness) to detect bright areas
    _, _, v = cv2.split(hsv)
    
    # Threshold the Value channel to get bright regions
    _, thresh = cv2.threshold(v, 200, 255, cv2.THRESH_BINARY)  # Adjust threshold as needed
    
    # Apply morphological operations to clean up the noise and better detect the ribbon
    kernel = np.ones((5, 5), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)  # Closing to fill small gaps
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)   # Opening to remove small noise

    # Find contours of the bright regions
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw the contours (ribbon) on the frame in green
    marked_frame = frame.copy()
    cv2.drawContours(marked_frame, contours, -1, (0, 255, 0), 2)  # Mark the ribbon in green

    # Calculate the total area of the bright ribbon
    total_area = sum(cv2.contourArea(c) for c in contours)

    return marked_frame, total_area

# Function to process the video and analyze the ribbon area
def process_video(video_path, output_folder):
    # Open the video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error opening video file")
        return [], [], 0

    fps = cap.get(cv2.CAP_PROP_FPS)  # Frames per second
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    dt = 1 / fps  # Time difference between frames

    areas = []
    times = []
    frame_idx = 0
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each frame of the video
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # End of video

        # Find the ribbon area in the current frame
        marked_frame, area = find_bright_ribbon_area(frame)

        # Save the marked frame at specific intervals
        if frame_idx % int(fps) == 0:  # Save one frame per second
            cv2.imwrite(os.path.join(output_folder, f"frame_{frame_idx}.png"), marked_frame)
        
        # Append area and corresponding time
        areas.append(area)
        times.append(frame_idx * dt)
        
        frame_idx += 1

    cap.release()
    return areas, times, fps

# Function to calculate the velocity from the area changes
def calculate_velocity(areas, times):
    velocities = []
    for i in range(1, len(areas)):
        dA = areas[i] - areas[i - 1]
        dt = times[i] - times[i - 1]
        velocity = dA / dt if dt != 0 else 0  # Avoid division by zero
        velocities.append(velocity)
    return velocities

# Function to plot the results (area and velocity)
def plot_results(areas, velocities, times):
    plt.figure(figsize=(12, 6))

    # Plot Area vs Time
    plt.subplot(1, 2, 1)
    plt.plot(times, areas, label="Area", color='b')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Area (pixels)')
    plt.title('Bright Ribbon Area vs Time')

    # Plot Velocity vs Time
    plt.subplot(1, 2, 2)
    plt.plot(times[1:], velocities, label="Velocity", color='r')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Velocity (pixels/second)')
    plt.title('Change in Area (Velocity) vs Time')

    plt.tight_layout()
    plt.show()

# Main function to execute everything
def main(video_path, output_folder):
    # Process the video to get areas and times
    areas, times, fps = process_video(video_path, output_folder)

    # Calculate velocity from the change in area
    velocities = calculate_velocity(areas, times)

    # Plot the area and velocity over time
    plot_results(areas, velocities, times)

# Example usage
video_path = 'picvid/pendulum1.mp4'  # Path to your video file
output_folder = 'saved_frames/'  # Folder to save marked frames
main(video_path, output_folder)
