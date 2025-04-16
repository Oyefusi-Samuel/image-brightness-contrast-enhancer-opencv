# Import OpenCV for image processing
import cv2

# Import NumPy for numerical operations
import numpy as np

# Import matplotlib for plotting histograms
import matplotlib.pyplot as plt

# Import Tkinter for file dialog GUI
from tkinter import Tk, filedialog

# Function to adjust brightness and contrast
def adjust_brightness_contrast(image, alpha, beta):
    # Convert image pixel values using a linear transformation: new = alpha * old + beta
    adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted  # Return the adjusted image

# Function to plot histogram of the image
def plot_histogram(image, title="Histogram"):
    # Define color channels: blue, green, red
    colors = ('b', 'g', 'r')
    plt.figure()  # Create a new figure for the histogram
    plt.title(title)  # Set the title of the plot
    plt.xlabel("Pixel Value")  # X-axis label
    plt.ylabel("Frequency")    # Y-axis label

    # Loop over each color channel
    for i, color in enumerate(colors):
        # Calculate histogram for the current channel
        hist = cv2.calcHist([image], [i], None, [255], [0, 255])
        plt.plot(hist, color=color)  # Plot the histogram with the corresponding color

    plt.xlim([0, 256])  # Set X-axis limits

# Main execution function
def main():
    # Open a file dialog for the user to select an image file
    Tk().withdraw()  # Hide the root Tkinter window
    file_path = filedialog.askopenfilename(
        title="Select an Image", 
        filetypes=[("Image Files", "*.jpg;*.png;*.jpeg;*.bmp;*.tiff")]
    )

    # If user cancels or does not select a file
    if not file_path:
        print("No file selected. Exiting...")
        return

    # Load the image using OpenCV
    image = cv2.imread(file_path)

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Could not load image.")
        return

    # Define contrast and brightness parameters
    alpha = 1.5  # Contrast control (1.0-3.0; >1 increases contrast)
    beta = 50    # Brightness control (0-100; >0 brightens image)

    # Apply brightness and contrast enhancement
    adjusted_image = adjust_brightness_contrast(image, alpha, beta)

    # Allow resizing of the "Original Image" window and set it to original image dimensions
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Original Image", image.shape[1], image.shape[0])

    # Same for the "Adjusted Image" window
    cv2.namedWindow("Adjusted Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Adjusted Image", adjusted_image.shape[1], adjusted_image.shape[0])

    # Display the original image
    cv2.imshow("Original Image", image)

    # Display the adjusted image
    cv2.imshow("Adjusted Image", adjusted_image)

    # Plot histogram for the original image
    plot_histogram(image, "Original Image Histogram")

    # Plot histogram for the adjusted image
    plot_histogram(adjusted_image, "Adjusted Image Histogram")

    plt.show()  # Show the histogram plots

    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close all OpenCV windows

# Entry point of the program
if __name__ == "__main__":
    main()
    
 # type: ignore comments lines