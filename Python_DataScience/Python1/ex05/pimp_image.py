import numpy as np

def ft_invert(array):
    """
    Inverts the color of the image received.
    
    :param array: The input image as a NumPy array.
    :return: The inverted image as a NumPy array.
    """
    inverted_array = 255 - array
    return inverted_array

def ft_red(array):
    """
    Apply a red color filter to the image.
    
    :param array: The input image as a NumPy array.
    :return: The image with the red filter as a NumPy array.
    """
    red_filtered_array = array.copy()
    red_filtered_array[:, :, 1] = 0  # Set green channel to 0
    red_filtered_array[:, :, 2] = 0  # Set blue channel to 0
    return red_filtered_array

def ft_green(array):
    """
    Apply a green color filter to the image.
    
    :param array: The input image as a NumPy array.
    :return: The image with the green filter as a NumPy array.
    """
    green_filtered_array = array.copy()
    green_filtered_array[:, :, 0] = 0  # Set red channel to 0
    green_filtered_array[:, :, 2] = 0  # Set blue channel to 0
    return green_filtered_array

def ft_blue(array):
    """
    Apply a blue color filter to the image.
    
    :param array: The input image as a NumPy array.
    :return: The image with the blue filter as a NumPy array.
    """
    blue_filtered_array = array.copy()
    blue_filtered_array[:, :, 0] = 0  # Set red channel to 0
    blue_filtered_array[:, :, 1] = 0  # Set green channel to 0
    return blue_filtered_array

def ft_grey(array):
    """
    Convert the image to grayscale.
    
    :param array: The input image as a NumPy array.
    :return: The grayscale image as a NumPy array.
    """
    grey_array = np.mean(array, axis=2, dtype=np.uint8)
    return np.stack((grey_array, grey_array, grey_array), axis=2)