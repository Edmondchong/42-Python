# rotate.py

import cv2

def rotate_image(image_path):
    """
    Loads an image and rotates it 90 degrees anticlockwise.

    Args:
        image_path (str): The path to the input image.

    Returns:
        rotated_image (numpy.ndarray): The rotated image.
    """

    # Load the image
    image = cv2.imread(image_path)

    # Rotate the image 90 degrees anticlockwise
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    return rotated_image

if __name__ == "__main__":
    image_path = "animal.jpeg"
    rotated_image = rotate_image(image_path)

    # Display the rotated image
    cv2.imshow("Rotated Image", rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Print the shape of the rotated image
    shape = rotated_image.shape
    print(f"The shape of image is: ({shape[0]}, {shape[1]})")

    # Print the data of the rotated image
    print("Data of the image after rotation:")
    print(rotated_image)

