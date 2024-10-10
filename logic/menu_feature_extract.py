import cv2
import os
import pandas as pd
import mahotas as mt

class MenuFeatureExtract:
    
    def color(folder_path):
        data = []

        # Iterating through all image files in the folder
        for index, filename in enumerate(os.listdir(folder_path)):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(folder_path, filename)
                img = cv2.imread(img_path)
                avg_color_per_row = cv2.mean(img)[:3]  # Get RGB values
                R, G, B = avg_color_per_row
                data.append([index + 1, filename, R, G, B])

        # Create a DataFrame with the extracted data
        df = pd.DataFrame(data, columns=['No', 'Nama', 'R', 'G', 'B'])

        # Save the DataFrame to Excel in the user's Documents directory
        documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
        output_path = os.path.join(documents_path, 'Kelompok C2', 'feature_color.xlsx')
        output_dir = os.path.dirname(output_path)
        
        # Create directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Save the dataframe to the Excel file
        df.to_excel(output_path, index=False)

        print(f'File has been saved at {output_path}')
        print(f'Hasil ekstraksi telah disimpan di {output_path}')

    def extract_glcm_features(image_gray):
        glcm = mt.features.haralick(image_gray).mean(axis=0)
        contrast = glcm[1]
        homogeneity = glcm[4]
        energy = glcm[8]
        correlation = glcm[2]
        return contrast, homogeneity, energy, correlation

    def texture(folder_path):
        data = []
        
        for index, filename in enumerate(os.listdir(folder_path)):
            if filename.endswith(('.png', '.jpg', '.jpeg')):  # Check for image files
                img_path = os.path.join(folder_path, filename)
                img = cv2.imread(img_path)
                
                # Convert image to grayscale
                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                
                # Extract GLCM features
                contrast, homogeneity, energy, correlation = MenuFeatureExtract.extract_glcm_features(img_gray)
                
                # Append extracted data
                data.append([index + 1, filename, contrast, homogeneity, energy, correlation])

        # Create DataFrame with the results
        df = pd.DataFrame(data, columns=['No', 'Nama', 'Kontras', 'Homogenitas', 'Energi', 'Korelasi'])
        
        # Save the DataFrame to Excel in the user's Documents folder
        documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
        output_path = os.path.join(documents_path, 'Kelompok C2', 'feature_texture.xlsx')
        output_dir = os.path.dirname(output_path)
        
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Save the DataFrame to an Excel file
        df.to_excel(output_path, index=False)

        print(f'Hasil ekstraksi fitur tekstur telah disimpan di {output_path}')

# folder_path = r'C:\Users\Achmad Baihaqi\Pictures\PCV'
# MenuFeatureExtract.color(folder_path)
# MenuFeatureExtract.texture(folder_path)