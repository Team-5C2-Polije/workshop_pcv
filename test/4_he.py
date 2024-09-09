import cv2
import matplotlib.pyplot as plt

def histogram_equalization(image_path):
    image_asli = cv2.imread(image_path)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    equalized_image = cv2.equalizeHist(image)

    histogram_image = cv2.calcHist([image], [0], None, [256], [0, 256])
    histogram_equalized_image = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 2, 1)
    plt.title('Gambar Asli')
    plt.imshow(image, cmap="gray")
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.title('Gambar Equalization')
    plt.imshow(equalized_image, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.title('Histogram Gambar Asli')
    plt.plot(histogram_image)
    plt.xlim([0, 256])

    plt.subplot(2, 2, 4)
    plt.title('Histogram Gambar Equalized')
    plt.plot(histogram_equalized_image)
    plt.xlim([0, 256])

    plt.show()

histogram_equalization(r'C:\Users\Achmad Baihaqi\Pictures\PCV\gbr.jpg')