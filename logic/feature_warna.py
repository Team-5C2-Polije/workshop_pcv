# import cv2
# import os
# import pandas as pd

# # folder_path = rf'C:\Users\Achmad Baihaqi\Pictures\PCV'

# data = []

# for index, filename in enumerate(os.listdir(folder_path)):
#     if filename.endswith(('.png', '.jpg', '.jpeg')):
#         img_path = os.path.join(folder_path, filename)
#         img = cv2.imread(img_path)
#         avg_color_per_row = cv2.mean(img)[:3]
#         R, G, B = avg_color_per_row
#         data.append([index + 1, filename, R, G, B])

# df = pd.DataFrame(data, columns=['No', 'Nama', 'R', 'G', 'B'])
# documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
# output_path = os.path.join(documents_path, 'Kelompok C2', 'feature_color.xlsx')
# output_dir = os.path.dirname(output_path)
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)
# df.to_excel(output_path, index=False)

# print(f'File has been saved at {output_path}')
# print(f'Hasil ekstraksi telah disimpan di {output_path}')
