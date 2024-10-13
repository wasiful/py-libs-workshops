import cv2
import numpy as np
import os

def blend_images_with_opacity(folder_path, output_image_path):
    # Verify the folder exists
    if not os.path.isdir(folder_path):
        raise FileNotFoundError(f"Error: Folder '{folder_path}' not found.")

    # Get list of image files from folder
    image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    
    # Check if there are any valid images
    if not image_files:
        raise ValueError("Error: No valid images found in the folder.")

    # Load images
    images = []
    for image_file in image_files:
        img = cv2.imread(image_file)
        if img is not None:
            images.append(img)
            print(f"Loaded image: {os.path.basename(image_file)} ({img.shape})")
        else:
            print(f"Warning: Failed to load image '{image_file}'. Skipping.")

    # Check if any images were successfully loaded
    if not images:
        raise RuntimeError("Error: No images could be loaded.")

    # Resize all images to match the size of the first image (for uniformity)
    base_image = images[0]
    base_height, base_width = base_image.shape[:2]
    resized_images = [cv2.resize(img, (base_width, base_height)) for img in images]

    # Initialize the blended image as the first image (with 100% opacity)
    blended_image = resized_images[0].astype(float)

    # Calculate the opacity decrement factor
    num_images = len(resized_images)
    initial_alpha = 1.0  # 100% opacity for the first image
    final_alpha = 0.5    # 50% opacity for the last image
    alpha_step = (initial_alpha - final_alpha) / (num_images - 1)

    # Blend subsequent images with decreasing opacity
    current_alpha = initial_alpha
    for i in range(1, num_images):
        next_image = resized_images[i].astype(float)
        blended_image = cv2.addWeighted(blended_image, 1.0, next_image, current_alpha, 0)
        current_alpha = max(final_alpha, current_alpha - alpha_step)  # Gradually decrease opacity

    # Normalize values to valid image range [0, 255]
    blended_image = np.clip(blended_image, 0, 255).astype(np.uint8)

    # Ensure the output directory exists, or create it if necessary
    output_dir = os.path.dirname(output_image_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    # Convert to absolute path
    output_image_path = os.path.abspath(output_image_path)
    print(f"Attempting to save combined image at: {output_image_path}")

    # Save the blended image as .jpg
    success = cv2.imwrite(output_image_path, blended_image)
    
    if not success:
        # Try saving as .png if .jpg fails
        output_image_path = output_image_path.replace('.jpg', '.png')
        print(f"Warning: Failed to save as .jpg. Trying to save as .png at {output_image_path}")
        success = cv2.imwrite(output_image_path, blended_image)

    if success:
        print(f"Successfully saved the blended image to '{output_image_path}'")
    else:
        raise IOError(f"Error: Failed to save the blended image to '{output_image_path}'")

# Example usage:
blend_images_with_opacity('Image_analysis/Burst', 'output/blended_output_image_v2.png')
