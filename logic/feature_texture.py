# import os
# import cv2
# import pandas as pd
# import mahotas as mt

# # folder_path = rf'C:\Users\Achmad Baihaqi\Pictures\PCV'
# data = []

# def extract_glcm_features(image_gray):
#     glcm = mt.features.haralick(image_gray).mean(axis=0)
#     contrast = glcm[1]
#     homogeneity = glcm[4]
#     energy = glcm[8]
#     correlation = glcm[2]
#     return contrast, homogeneity, energy, correlation

# for index, filename in enumerate(os.listdir(folder_path)):
#     if filename.endswith(('.png', '.jpg', '.jpeg')):
#         img_path = os.path.join(folder_path, filename)
#         img = cv2.imread(img_path)
#         img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         contrast, homogeneity, energy, correlation = extract_glcm_features(img_gray)
#         data.append([index + 1, filename, contrast, homogeneity, energy, correlation])

# df = pd.DataFrame(data, columns=['No', 'Nama', 'Kontras', 'Homogenitas', 'Energi', 'Korelasi'])
# documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
# output_path = os.path.join(documents_path, 'Kelompok C2', 'feature_texture.xlsx')
# output_dir = os.path.dirname(output_path)
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)
# df.to_excel(output_path, index=False)

# print(f'Hasil ekstraksi fitur GLCM telah disimpan di {output_path}')
