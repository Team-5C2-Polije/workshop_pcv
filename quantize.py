import numpy as np
import cv2
import matplotlib.pyplot as plt

# Membaca gambar grayscale dari direktori (ganti path dengan path gambar Anda)
image = cv2.imread(r'C:\Users\Achmad Baihaqi\Pictures\PCV\city-bali.png', cv2.IMREAD_GRAYSCALE)

# Tentukan jumlah level kuantisasi (misalnya 4 level untuk 2-bit)
levels = 4

# Tentukan interval kuantisasi
interval_size = 256 // levels # 256 karena citra 8-bit (0-255)
intervals = [i * interval_size for i in range(levels)]
mid_values = [(i * interval_size) + ((i + 1) * interval_size - 1) // 2 for i in range(levels)]

# Fungsi kuantisasi manual
def quantize(image, intervals, mid_values):
    quantized_image = np.zeros_like(image)
    for i in range(len(intervals)):
        lower_bound = intervals[i]
        upper_bound = lower_bound + interval_size - 1
        mask = (image >= lower_bound) & (image <= upper_bound)
        quantized_image[mask] = mid_values[i]
    return quantized_image

# Terapkan kuantisasi pada gambar
quantized_image = quantize(image, intervals, mid_values)

# Tampilkan gambar asli dan hasil kuantisasi
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title("Gambar Asli")
plt.imshow(image, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Setelah Kuantisasi")
plt.imshow(quantized_image, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.show()
