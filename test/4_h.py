import cv2
import matplotlib.pyplot as plt

# Fungsi untuk menampilkan histogram citra
def tampilkan_histogram_citra(image_path):

    # Membaca citra dari direktori dan konversi ke rgb
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # memisahkan channel
    channels = ('r', 'g', 'b')
    # colors = ('red', 'green', 'blue')

    plt.figure(figsize=(10,5))

    for i, color in enumerate(channels):
        histogram = cv2.calcHist([image_rgb], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color)
        plt.xlim([0, 256])

    plt.title('Histogram untuk setiap kanal warna')
    plt.xlabel('Intensitas Pixel')
    plt.ylabel('Jumlah Pixel')
    plt.show()

# direktori gambar
image = r'C:\Users\Achmad Baihaqi\Pictures\PCV\gbr.jpg' 

# menampilkan hiostogram
tampilkan_histogram_citra(image)