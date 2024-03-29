from PIL import Image
import numpy as np

def ft_load(image_path):
    """
    Load an image from the given file path and return it as a NumPy array.
    
    :param image_path: The path to the image file.
    :return: A NumPy array representing the image.
    """
    image = Image.open(image_path)
    image_array = np.array(image)
    print("The shape of the image is:", image_array.shape)
    return image_array
