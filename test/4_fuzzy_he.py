import numpy as np
import cv2
import matplotlib.pyplot as plt

def fuzzy_membership_function(x, mean, stddev):
    epsilon = 1e-5 # Menambah epsilon agar tdk ada pembagian dengan nol
    return np.exp(-((x - mean) ** 2) / (2 * (stddev ** 2 + epsilon)))

def fuzzy_histogram_equalization(image, block_size=16):
    # konversi gambar ke grayscale
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    height, widht = image.shape #dapatkan dimensi gambar

    equalized_image = np.zeros_like(image, dtype=np.uint8) # Buat gambar yang telah di equalize

    # ukuran blok
    block_height = block_size
    block_widht = block_size

    for y in range(0, height, block_height):
        for x in range(0, widht, block_widht):
            # definisi batas blok
            block = image[y:y+block_height, x:x+block_widht]
            if block.size == 0:
                continue

            # hitung histogram lokal
            hist, bins = np.histogram(block.flatten(), bins=256, range=[0, 256])
            cdf = hist.cumsum()
            cdf_normalized = cdf * 256 / cdf[-1]
            equalized_block = np.interp(block.flatten(), bins[:-1], cdf_normalized).reshape(block.shape)

            # hitung keanggotaan fuzzy
            mean = np.mean(equalized_block)
            stddev = np.std(equalized_block)
            membership = fuzzy_membership_function(equalized_block, mean, stddev)

            # Terapkan penyesuaian kontras fuzzy
            equalized_image[y:y+block_height, x:x+block_widht] = np.clip(equalized_block * membership, 0, 255).astype(np.uint8)

    return equalized_image

image_path = r'C:\Users\Achmad Baihaqi\Pictures\PCV\gbr.jpg' # Path ke gambar
image = cv2.imread(image_path) 

fhe_image = fuzzy_histogram_equalization(image) # Terapkan fhe


histogram_image = cv2.calcHist([image], [0], None, [256], [0, 256])
histogram_equalized_image = cv2.calcHist([fhe_image], [0], None, [256], [0, 256])

# Menampilkan gambar asli dan yang telah di FHE
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Fuzzy Histogram Equalization Image')
plt.imshow(fhe_image, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Origninal Image Histogram')
plt.plot(histogram_image)
plt.xlim([0, 256])

plt.subplot(2, 2, 4)
plt.title('Equalization Image Histogram')
plt.plot(histogram_equalized_image)
plt.xlim([0, 256])

plt.show()