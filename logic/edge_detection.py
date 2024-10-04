import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage import data

# Mengambil gambar contoh dari skimage
image_path = rf'C:\Users\Achmad Baihaqi\Pictures\PCV\gbr.jpg'
image_example_pre = cv2.imread(image_path)
image_example = cv2.cvtColor(image_example_pre, cv2.COLOR_BGR2GRAY)

# Terapkan deteksi tepi Sobel
sobel_x = cv2.Sobel(image_example, cv2.CV_64F, 1, 0, ksize=3)  # Gradien horizontal
sobel_y = cv2.Sobel(image_example, cv2.CV_64F, 0, 1, ksize=3)  # Gradien vertikal
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Terapkan deteksi tepi Prewitt secara manual
prewitt_x = cv2.filter2D(image_example, -1, np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]]))
prewitt_y = cv2.filter2D(image_example, -1, np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]]))
prewitt_combined = np.sqrt(np.square(prewitt_x) + np.square(prewitt_y))

# Terapkan deteksi tepi Canny
canny_edges = cv2.Canny(image_example, 100, 200)

# Visualisasikan hasil dari Sobel, Prewitt, dan Canny
plt.figure(figsize=(15, 10))

# Tampilkan gambar asli
plt.subplot(2, 2, 1)
plt.title("Gambar Asli")
plt.imshow(image_example)
plt.axis('off')

# Tampilkan hasil deteksi tepi Sobel
plt.subplot(2, 2, 2)
plt.title("Deteksi Tepi (Sobel)")
plt.imshow(sobel_combined, cmap='gray')
plt.axis('off')

# Tampilkan hasil deteksi tepi Prewitt
plt.subplot(2, 2, 3)
plt.title("Deteksi Tepi (Prewitt)")
plt.imshow(prewitt_combined, cmap='gray')
plt.axis('off')

# Tampilkan hasil deteksi tepi Canny
plt.subplot(2, 2, 4)
plt.title("Deteksi Tepi (Canny)")
plt.imshow(canny_edges, cmap='gray')
plt.axis('off')

plt.show()
