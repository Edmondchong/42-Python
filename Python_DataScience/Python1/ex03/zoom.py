import cv2

def main():
    # Load the modified image with scales
    image = cv2.imread("animal_with_scales.jpeg")

    # Check if the image was loaded successfully
    if image is not None:
        # Perform zooming by slicing the image
        zoomed_image = image[100:500, 100:500]  # Adjust the slice to your desired zoom level

        # Get the new shape of the zoomed image
        zoomed_height, zoomed_width, _ = zoomed_image.shape

        # Display the new shape
        print(f"New shape after slicing: ({zoomed_height}, {zoomed_width})")

        # Display the zoomed image in a window
        cv2.imshow("Zoomed Image", zoomed_image)
        key = cv2.waitKey(0)  # Wait for a key press indefinitely
        if key == ord('q'):
            cv2.destroyAllWindows()

    else:
        print("Error: Unable to load the modified image with scales.")

if __name__ == "__main__":
    main()
