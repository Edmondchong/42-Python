# load_image.py

import cv2

def load_and_transpose_image(image_path):
    """
    Loads an image from the specified path, extracts a square part, and transposes it.
    
    Args:
        image_path (str): The path to the input image.

    Returns:
        transposed_image (numpy.ndarray): The transposed image.
    """

    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Extract a square part (let's assume we want the top-left corner)
    square_part = image[:400, :400]

    # Transpose the square part
    transposed_image = cv2.transpose(square_part)

    return transposed_image

if __name__ == "__main__":
    image_path = "animal.jpeg"
    transposed_image = load_and_transpose_image(image_path)

    # Display the transposed image
    cv2.imshow("Transposed Image", transposed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Print the shape of the transposed image
    shape = transposed_image.shape
    print(f"The shape of image is: ({shape[0]}, {shape[1]})")

    # Print the data of the transposed image
    print("Data of the image after transpose:")
    print(transposed_image)

