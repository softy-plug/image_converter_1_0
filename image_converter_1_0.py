import os
from PIL import Image

# List of image formats to convert
extensions = ['.tga', '.jpg', '.jpeg', '.heif', '.heic', '.png', '.ico', '.tga', '.gif', '.tiff', '.tif', '.svg', '.jfif', '.pct', '.pict', '.raw', '.jp2', '.bmp']

# Function to convert images
def convert_image(input_image_path, output_image_path, max_quality):
    try:
        with Image.open(input_image_path) as image:
            image.save(output_image_path, quality=max_quality)
            print(f"Converted {input_image_path} to {output_image_path} with maximum quality")
    except:
        print(f"Unable to convert {input_image_path}")

# Function to prompt user to select folder
def select_folder():
    from tkinter import Tk
    from tkinter.filedialog import askdirectory

    # Create Tkinter root window
    root = Tk()

    # Hide the root window
    root.withdraw()

    # Prompt user to select folder
    folder_selected = askdirectory()

    # Destroy the root window
    root.destroy()

    return folder_selected

# Get input folder with images to convert
input_folder = select_folder()
if not input_folder:
    print("No input folder selected. Exiting program!")
    exit()

# Get output folder to save converted images
output_folder = select_folder()
if not output_folder:
    print("No output folder selected. Exiting program!")
    exit()

# Get maximum quality for output images
max_quality = int(input("Enter maximum quality for output images (0-100): "))

# Loop through all files in input folder and convert any image files
for file in os.listdir(input_folder):
    current_filename, current_extension = os.path.splitext(file)
    if current_extension.lower() in extensions:
        input_image_path = os.path.join(input_folder, file)
        output_image_path = os.path.join(output_folder, f"{current_filename}.jpg")
        convert_image(input_image_path, output_image_path, max_quality)

print("Conversion completed successfully!")

# softy_plug