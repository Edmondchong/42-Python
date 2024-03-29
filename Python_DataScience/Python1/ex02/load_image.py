from PIL import Image
import numpy as np

def ft_load(path: str):
    try:
        # Open the image file
        image = Image.open(path)

        # Get the format of the image (JPEG, JPG, etc.)
        image_format = image.format

        # Get the pixel data as a NumPy array, [225, 123, 34] == this is the type of data being stored in pixel_data
        pixel_data = np.array(image)

        # Print the shape of the image and the pixel content
        print(f"The shape of the image is: {pixel_data.shape}")
        print(pixel_data)

        return pixel_data  # You can return the pixel data in your desired format
    except Exception as e:
        print(f"An error occurred: {str(e)}")