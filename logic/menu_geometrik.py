from PIL import Image, ImageOps
import os

class MenuGeometrik:

    outputPath = ".output"
    outputFile = rf"{outputPath}\output.png"

    def translate_image(image, x_shift, y_shift):
        width, height = image.size
        translation_matrix = (1, 0, x_shift, 0, 1, y_shift)
        
        # Apply the affine transformation
        translated_image = image.transform((width, height), Image.AFFINE, translation_matrix)
        
        # Buat folder jika belum ada
        if not os.path.exists(MenuGeometrik.outputPath):
            os.makedirs(MenuGeometrik.outputPath)
        
        # Path untuk menyimpan gambar hasil
        output_path = os.path.join(MenuGeometrik.outputFile)
        
        # Simpan gambar
        translated_image.save(output_path)
        
        # Return direktori folder
        return MenuGeometrik.outputFile

    def rotate_image(image, angle):
        # Rotate the image
        rotated_image = image.rotate(angle, expand=True)
        
        # Buat folder jika belum ada
        if not os.path.exists(MenuGeometrik.outputPath):  # Memastikan folder, bukan file
            os.makedirs(MenuGeometrik.outputPath)
        
        # Simpan gambar ke file output yang lengkap
        rotated_image.save(MenuGeometrik.outputFile)  # Simpan gambar dengan path lengkap
        
        # Return direktori folder
        return MenuGeometrik.outputPath

    def flip_image(image, mode='horizontal'):
        # Flip image berdasarkan mode
        if mode == 'horizontal':
            flipped_image = ImageOps.mirror(image)  # Flip horizontal
        elif mode == 'vertical':
            flipped_image = ImageOps.flip(image)  # Flip vertical
        
        # Buat folder jika belum ada
        if not os.path.exists(MenuGeometrik.outputPath):
            os.makedirs(MenuGeometrik.outputPath)
        
        # Simpan gambar hasil flip ke dalam file output
        flipped_image.save(MenuGeometrik.outputFile)
        
        # Return direktori folder
        return MenuGeometrik.outputPath

    def zoom_image(image, zoom_factor):
        # Dapatkan ukuran gambar
        width, height = image.size
        
        # Resize gambar berdasarkan zoom_factor
        zoomed_image = image.resize((int(width * zoom_factor), int(height * zoom_factor)))
        
        # Buat folder jika belum ada
        if not os.path.exists(MenuGeometrik.outputPath):
            os.makedirs(MenuGeometrik.outputPath)
        
        # Simpan gambar hasil zoom ke dalam file output
        zoomed_image.save(MenuGeometrik.outputFile)
        
        # Return direktori folder
        return MenuGeometrik.outputPath

    def crop_image(image, left, top, right, bottom):
        # Memotong gambar berdasarkan koordinat yang diberikan
        cropped_image = image.crop((left, top, right, bottom))
        
        # Buat folder jika belum ada
        if not os.path.exists(MenuGeometrik.outputPath):
            os.makedirs(MenuGeometrik.outputPath)
        
        # Simpan gambar hasil crop ke file output di dalam folder outputPath
        cropped_image.save(MenuGeometrik.outputFile)
        
        # Return path folder
        return MenuGeometrik.outputPath
