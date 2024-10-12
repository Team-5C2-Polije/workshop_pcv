# import cv2
# import numpy as np
# from skimage.morphology import skeletonize, thin

# # Baca gambar biner
# # img = cv2.imread(rf'C:\Users\Achmad Baihaqi\Pictures\PCV\gbr.jpg', 0)  # Pastikan gambar sudah biner
# _, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# # Kernel morfologi
# # kernel = np.ones((3,3), np.uint8)
# # kernel = np.ones((5,3), np.uint8)
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

# # 1. Erosi
# erosion = cv2.erode(binary_img, kernel, iterations=1)

# # 2. Dilasi
# dilation = cv2.dilate(binary_img, kernel, iterations=1)

# # 3. Opening (Erosi kemudian dilasi)
# opening = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, kernel)

# # 4. Closing (Dilasi kemudian erosi)
# closing = cv2.morphologyEx(binary_img, cv2.MORPH_CLOSE, kernel)

# # 5. Hit-or-Miss
# # Membuat kernel hit-or-miss (ada berbagai variasi)
# kernel_hitmiss = np.array([[ 1, 1, 1],
#                            [ 0, 1, 0],
#                            [-1, -1, -1]])
# hit_or_miss = cv2.morphologyEx(binary_img, cv2.MORPH_HITMISS, kernel_hitmiss)

# # 6. Thinning (Penipisan)
# thinned_img = thin(binary_img // 255) * 255  # Menggunakan skimage

# # 7. Thickening (Penebalan - tidak ada langsung di OpenCV, bisa dikombinasikan dengan operasi lain)
# thickening = cv2.dilate(binary_img, kernel, iterations=1) - erosion

# # 8. Skeletonization (Kerangka)
# skeleton = skeletonize(binary_img // 255) * 255  # Menggunakan skimage

# # 9. Pruning (Pemangkasan - biasanya dilakukan pada kerangka untuk menghilangkan cabang kecil)
# # Pruning tidak ada di OpenCV secara langsung, harus diimplementasikan menggunakan pendekatan sendiri.
# # Berikut adalah langkah dasar untuk melakukan pruning setelah skeletonization:

# # error bjir
# # def prune_skeleton(skeleton_img, iterations=1):
# #     pruned_img = skeleton_img.copy()
# #     for _ in range(iterations):
# #         pruned_img = cv2.morphologyEx(pruned_img, cv2.MORPH_HITMISS, kernel_hitmiss)
# #     return pruned_img
# def prune_skeleton(skeleton_img, iterations=1):
#     pruned_img = skeleton_img.copy().astype(np.uint8)  # Convert to uint8
#     for _ in range(iterations):
#         pruned_img = cv2.morphologyEx(pruned_img, cv2.MORPH_HITMISS, kernel_hitmiss)
#     return pruned_img

# pruned_skeleton = prune_skeleton(skeleton, iterations=2)

# # Menampilkan hasil
# # cv2.imshow('Original', binary_img)
# cv2.imshow('Erosion', erosion)
# # cv2.imshow('Dilation', dilation)
# # cv2.imshow('Opening', opening)
# # cv2.imshow('Closing', closing)
# # cv2.imshow('Hit-or-Miss', hit_or_miss)
# # cv2.imshow('Thinning', thinned_img.astype(np.uint8))
# # cv2.imshow('Skeleton', skeleton.astype(np.uint8))
# # cv2.imshow('Pruned Skeleton', pruned_skeleton.astype(np.uint8))
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # pip install scikit-image
