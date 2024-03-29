from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

def display_images(images, titles):
    from PIL import Image
    import numpy as np
    import matplotlib.pyplot as plt

    num_images = len(images)
    rows = 2
    cols = (num_images + 1) // 2  # Arrange images in a 2xN grid

    fig, axes = plt.subplots(rows, cols, figsize=(12, 6))
    axes = axes.ravel()

    for i in range(num_images):
        img = Image.fromarray(np.uint8(images[i]))
        axes[i].imshow(img)
        axes[i].set_title(titles[i])
        axes[i].axis('off')

    plt.tight_layout()
    plt.show()

array = ft_load("landscape.jpg")
ft_invert_array = ft_invert(array)
ft_red_array = ft_red(array)
ft_green_array = ft_green(array)
ft_blue_array = ft_blue(array)
ft_grey_array = ft_grey(array)

# Prepare the images and titles for display
images = [array, ft_invert_array, ft_red_array, ft_green_array, ft_blue_array, ft_grey_array]
titles = ["Original Image", "Inverted Image", "Red Filtered", "Green Filtered", "Blue Filtered", "Grayscale"]

# Display all images at once
display_images(images, titles)
