import cv2
import numpy as np
import os

def stack_video_frames(video_path, output_image_path):
    # Check if the file exists
    if not os.path.exists(video_path):
        print(f"Error: File '{video_path}' not found.")
        return

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Unable to open video file '{video_path}'")
        return

    # Get video properties for debugging purposes
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Video Properties - Width: {frame_width}, Height: {frame_height}, Total Frames: {total_frames}")

    # Read the first frame to initialize the stack
    ret, frame = cap.read()
    if not ret:
        print(f"Error: Unable to read the first frame from '{video_path}'")
        return

    # Convert the first frame to float32 for precision during stacking
    frame_stack = np.float32(frame)
    frame_count = 1  # Initialize the frame counter
    print(f"Processing frame {frame_count}...")

    # Iterate through each frame in the video
    while True:
        # Read the next frame
        ret, frame = cap.read()
        if not ret:
            break  # Break if no more frames are available

        # Stack the frames by summing them up
        frame_stack += frame.astype(np.float32)
        frame_count += 1
        print(f"Processing frame {frame_count}/{total_frames}...")

    # Average out the stack to get the final image
    frame_stack /= frame_count

    # Convert back to uint8 (standard image format)
    stacked_image = np.uint8(np.clip(frame_stack, 0, 255))

    # Save the stacked image
    cv2.imwrite(output_image_path, stacked_image)

    # Release video capture
    cap.release()
    print(f"Saved the stacked image as '{output_image_path}'")

# Example usage
stack_video_frames('Image_analysis/input_video.mp4', 'stacked_output_image.jpg')
