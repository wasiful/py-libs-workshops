import cv2
import numpy as np
import os

def set_fps_interval(video_fps, target_fps):
    """
    Calculates the frame interval based on the desired FPS.
    If video is at 60fps and target is 2fps, this function will
    return an interval of 30, meaning we will take 1 frame every 30 frames.
    """
    if target_fps <= 0:
        raise ValueError("Target FPS must be a positive value.")
    return int(video_fps / target_fps)

def set_video_duration(total_frames, video_fps, duration):
    """
    Calculates the maximum frame count based on the desired duration (in seconds).
    If duration is 10 seconds and FPS is 30, then max frame count is 300.
    """
    if duration <= 0:
        raise ValueError("Duration must be a positive value.")
    return min(total_frames, int(video_fps * duration))

def calculate_opacity_weight(index, total_frames):
    """
    Calculate opacity weight for each frame based on its index.
    Starts from 1 (100% opacity) and decreases to 0.5 (50% opacity).
    """
    return 1.0 - (0.5 * (index / total_frames))

def stack_video_frames(video_path, output_image_path, target_fps=None, duration=None):
    # Check if the file exists
    if not os.path.exists(video_path):
        print(f"Error: File '{video_path}' not found.")
        return

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Unable to open video file '{video_path}'")
        return

    # Get video properties
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f"Video Properties - Width: {frame_width}, Height: {frame_height}, Total Frames: {total_frames}, FPS: {video_fps}")

    # Determine frame interval based on the desired FPS
    frame_interval = 1  # Default: Take every frame
    if target_fps and target_fps < video_fps:
        frame_interval = set_fps_interval(video_fps, target_fps)
        print(f"Target FPS: {target_fps}. Taking 1 frame every {frame_interval} frames.")

    # Determine the maximum number of frames to process based on the desired duration
    max_frame_count = total_frames  # Default: Use the whole video
    if duration:
        max_frame_count = set_video_duration(total_frames, video_fps, duration)
        print(f"Target Duration: {duration} seconds. Processing up to frame {max_frame_count}.")

    # Read the first frame to initialize the stack
    ret, frame = cap.read()
    if not ret:
        print(f"Error: Unable to read the first frame from '{video_path}'")
        return

    # Convert the first frame to float32 for precision during stacking
    frame_stack = np.zeros_like(frame, dtype=np.float32)
    weight_sum = 0.0  # Sum of weights for normalizing the final image
    frame_count = 1  # Initialize the frame counter
    processed_frames = 1  # Frames that have been stacked
    print(f"Processing frame {frame_count}/{max_frame_count}...")

    # Iterate through each frame in the video
    while frame_count < max_frame_count:
        # Read the next frame
        ret, frame = cap.read()
        if not ret:
            break  # Break if no more frames are available

        # Skip frames based on the frame interval
        if frame_count % frame_interval == 0:
            # Calculate the opacity weight for this frame
            opacity_weight = calculate_opacity_weight(processed_frames, max_frame_count)
            print(f"Stacking frame {frame_count}/{max_frame_count} with opacity {opacity_weight:.2f}...")

            # Stack the frames by summing them up using the calculated opacity weight
            frame_stack += frame.astype(np.float32) * opacity_weight
            weight_sum += opacity_weight  # Keep track of total weight sum
            processed_frames += 1

        frame_count += 1

    # Normalize the stacked image by dividing by the total weight sum
    frame_stack /= weight_sum

    # Convert back to uint8 (standard image format)
    stacked_image = np.uint8(np.clip(frame_stack, 0, 255))

    # Save the stacked image
    cv2.imwrite(output_image_path, stacked_image)

    # Release video capture
    cap.release()
    print(f"Saved the stacked image as '{output_image_path}' after stacking {processed_frames} frames.")

# Example usage with target FPS, duration control, and opacity weighting
stack_video_frames('Image_analysis/input_video.mp4', 'stacked_output_image.jpg', target_fps=60, duration=13)
