import os
import cv2

# Set the path to your images folder
path = "C:/Users/naina/Downloads/Pyhton programs of PRO! classes/ProP105/PRO-C105-Project-Images-main/Images"  # Replace with your actual folder path

# Create an empty list to store image names
images = []

# Loop through all files in the folder
for filename in os.listdir(path):
  # Separate filename and extension
  file, ext = os.path.splitext(filename)

  # Check if it's an image file (adjust extensions as needed)
  if ext.lower() in ('.jpg', '.jpeg', '.png'):
    # Create the full path to the image
    file_name = os.path.join(path, filename)

    # Print the filename for verification (optional)
    # print(file_name)

    # Add the image path to the list
    images.append(file_name)

# Get the number of images
count = len(images)

# Read the first image
frame = cv2.imread(images[0])

# Get the width, height, and channels of the image
width, height, channels = frame.shape

# Define the video size based on the first image
size = (width, height)

# Print the video size for verification (optional)
# print(size)

# Create a video writer object
out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

# Add images to the video
for i in range(count):
  # Read the image
  frame = cv2.imread(images[i])

  # Write the image to the video
  out.write(frame)

# Release the video writer
out.release()

# Print a completion message
print("Video created successfully!")
