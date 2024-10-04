import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
from skimage import data

class MenuEdgeDetection:
    outputPath = ".output"
    outputFile = rf"{outputPath}\output.png"

    def sobel(image_path):
        # Ensure the output directory exists
        os.makedirs(MenuEdgeDetection.outputPath, exist_ok=True)

        # Read the image and convert to grayscale
        image_read = cv2.imread(image_path)
        image_gray = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)

        # Apply Sobel operator
        sobel_x = cv2.Sobel(image_gray, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(image_gray, cv2.CV_64F, 0, 1, ksize=3)
        sobel_combined = cv2.magnitude(sobel_x, sobel_y)

        # Save the result to outputFile
        cv2.imwrite(MenuEdgeDetection.outputFile, sobel_combined)

        plt.figure(figsize=(6, 6))
        plt.subplot(1, 1, 1)
        plt.title("Deteksi Tepi (Sobel)")
        plt.imshow(sobel_combined, cmap='gray')
        plt.axis('off')
        plt.show()

    def prewitt(image_path):
        # Ensure the output directory exists
        os.makedirs(MenuEdgeDetection.outputPath, exist_ok=True)

        # Read the image and convert to grayscale
        image_read = cv2.imread(image_path)
        image_gray = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)

        # Apply Prewitt operator
        prewitt_x = cv2.filter2D(image_gray, -1, np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]]))
        prewitt_y = cv2.filter2D(image_gray, -1, np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]]))
        prewitt_combined = np.sqrt(np.square(prewitt_x) + np.square(prewitt_y))

        # Normalize the result to 0-255 and convert to uint8
        prewitt_combined = np.uint8(255 * (prewitt_combined / np.max(prewitt_combined)))

        # Save the result to outputFile
        cv2.imwrite(MenuEdgeDetection.outputFile, prewitt_combined)

        # Display the result using matplotlib
        plt.figure(figsize=(6, 6))
        plt.subplot(1, 1, 1)
        plt.title("Prewitt Combined")
        plt.imshow(prewitt_combined, cmap='gray')
        plt.axis('off')
        plt.show()

        return MenuEdgeDetection.outputFile

    def canny(image_path):
        os.makedirs(MenuEdgeDetection.outputPath, exist_ok=True)
        image_read = cv2.imread(image_path)
        image_gray = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)
        canny_edges = cv2.Canny(image_gray, 100, 200)
        cv2.imwrite(MenuEdgeDetection.outputFile, canny_edges)

        plt.figure(figsize=(6, 6))
        plt.subplot(1, 1, 1)
        plt.title("Canny Edges")
        plt.imshow(canny_edges, cmap='gray')
        plt.axis('off')
        plt.show()

        return MenuEdgeDetection.outputFile


# MenuEdgeDetection.sobel(rf'C:\Users\Achmad Baihaqi\Pictures\PCV\gbr.jpg')
# MenuEdgeDetection.prewitt(rf'C:\Users\Achmad Baihaqi\Pictures\PCV\gbr.jpg')
# MenuEdgeDetection.canny(rf'C:\Users\Achmad Baihaqi\Pictures\PCV\gbr.jpg')