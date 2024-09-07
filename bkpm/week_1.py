import os
import glob
from PIL import Image

# Init Directory
directory = r'C:\Users\Achmad Baihaqi\Pictures\PCV'
output_directory = r'C:\Users\Achmad Baihaqi\Pictures\PCV\output'

# menampilkan list gambar dengan library os
def withOs():
    for filename in os.listdir(directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            print(os.path.join(directory, filename))


# menampilkan list gambar dengan library glob
def withGlob():
    images = glob.glob(directory + r'\*.jpg')
    for image in images:
        print(image)

# membuka gambar yang telah di resize
def withPill(filename):
    # membuka gambar default
    img = Image.open(rf"{directory}\{filename}")
    img.show()

    # membuka gambar yg telah di resize
    img_resized = img.resize((300, 300))
    img_resized.show()

# mengubah semua ukuran gambar dan menyimpannya
def getDirAndImages(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # membaca semua file gambar
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(directory, filename)
            img = Image.open(img_path)
            img_resized = img.resize((200, 200)) # resize gambar
            img_resized.save(os.path.join(output_dir, filename)) # simpan hasil resiize

# memmbuka gambar dan save gambar ke dir dan format lain
def openAndSaveImage():
    img = Image.open(directory + '\gbr.jpg')
    img.save(output_directory + '\gbr.png') # change format
    img.save(output_directory + r'\new_gbr.jpg') # change dir
    img.save(output_directory + r'\new_gbr_quality.jpg', quality=85) # change quality


# ubah ukuran gambar dan simpan hasilnya
def saveAndResize():
    img = Image.open(directory + '\gbr.jpg')
    img_resized = img.resize((800, 800))
    img_resized.save(output_directory + '\gbr_resized.jpg')

# ubah mode gambar, kompresi dan simpan hasilnya
def saveWithOtherFormat():
    img = Image.open(directory + '\gbr.jpg')
    img_gray = img.convert("L")
    img_gray.save(output_directory + '\gbr_gray.png')
    img.save(output_directory + '\compressed_gbr.png', optimize=True)


# withOs()
# withGlob()
# withPill('gbr.jpg')
# getDirAndImages(r'C:\Users\Achmad Baihaqi\Pictures\PCV\output\resized')
# openAndSaveImage()
# saveAndResize()
saveWithOtherFormat()