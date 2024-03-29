import cv2

def main():
    # Load the image
    image = cv2.imread("animal.jpeg")

    # Check if the image was loaded successfully
    if image is not None:
        # Get the image shape
        height, width, channels = image.shape

        # Display image shape information
        print(f"The shape of the image is: ({height}, {width}, {channels})")

        # Display pixel content of a portion of the image
        print(image[:3, :3])  # Display the first 3x3 pixels as an example

        # Save the image with scales on the X and Y axes
        scale_text = f"X: {width}px, Y: {height}px"
        cv2.putText(image, scale_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Display the image in a window
        cv2.imshow("Image", image)
        key = cv2.waitKey(0)  # Wait for a key press indefinitely
        if key == ord('q'):
            cv2.destroyAllWindows()

    else:
        print("Error: Unable to load the image.")

if __name__ == "__main__":
    main()
