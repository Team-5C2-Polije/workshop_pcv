import cv2
import numpy as np
from skimage.morphology import skeletonize, thin
import os

class MenuMorfologi:

    outputPath = ".output"
    outputFile = rf"{outputPath}\output.png"

    def __getKernel__(type):
        if type == 1:
            return np.ones((3, 3), np.uint8)
        elif type == 2:
            return np.ones((5, 3), np.uint8)
        elif type == 3:
                return cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        elif type == 4:
            return np.ones((9, 3), np.uint8)
        else:
            raise ValueError("Invalid type. Please choose 1, 2, or 3.")

    def erotion(imagePath, kernelType):
        img = cv2.imread(imagePath, 0)
        _, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

        kernel = MenuMorfologi.__getKernel__(kernelType)
        eroded_img = cv2.erode(binary_img, kernel, iterations=1)
        outputPath = os.path.join(MenuMorfologi.outputFile)
        cv2.imwrite(outputPath, eroded_img)
        return outputPath

    def dilate(imagePath, kernelType):
        img = cv2.imread(imagePath)
        _, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

        kernel = MenuMorfologi.__getKernel__(kernelType)
        dil_img = cv2.dilate(binary_img, kernel, iterations=1)
        outputPath = os.path.join(MenuMorfologi.outputFile)
        cv2.imwrite(outputPath, dil_img)
        return outputPath
    
    def opening(imagePath, kernelType):
        img = cv2.imread(imagePath, 0)
        _, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

        kernel = MenuMorfologi.__getKernel__(kernelType)
        opn_img = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, kernel)
        outputPath = os.path.join(MenuMorfologi.outputFile)
        cv2.imwrite(outputPath, opn_img)
        return outputPath
    
    def closing(imagePath, kernelType):
        img = cv2.imread(imagePath, 0)
        _, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

        kernel = MenuMorfologi.__getKernel__(kernelType)
        opn_img = cv2.morphologyEx(binary_img, cv2.MORPH_CLOSE, kernel)
        outputPath = os.path.join(MenuMorfologi.outputFile)
        cv2.imwrite(outputPath, opn_img)
        return outputPath
    
    def hit_or_miss(imagePath):
        img = cv2.imread(imagePath, 0)
        _, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

        kernel_hitmiss = np.array([[ 1, 1, 1],
                           [ 0, 1, 0],
                           [-1, -1, -1]])
        
        hit_or_miss = cv2.morphologyEx(binary_img, cv2.MORPH_HITMISS, kernel_hitmiss)

        outputPath = os.path.join(MenuMorfologi.outputFile)
        cv2.imwrite(outputPath, hit_or_miss)
        return outputPath
    
    def thinned(imagePath):
        img = cv2.imread(imagePath, 0)
        _, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        
        thinned_img = thin(binary_img // 255) * 255 

        outputPath = os.path.join(MenuMorfologi.outputFile)
        cv2.imwrite(outputPath, thinned_img)
        return outputPath

    def skeleton(imagePath):
        img = cv2.imread(imagePath, 0)
        _, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        
        skeleton = skeletonize(binary_img // 255) * 255 

        outputPath = os.path.join(MenuMorfologi.outputFile)
        cv2.imwrite(outputPath, skeleton)
        return outputPath
    
    def prune_skeleton(imagePath):
        img = cv2.imread(imagePath, 0)
        _, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        
        skeleton_img = skeletonize(binary_img // 255).astype(np.uint8) * 255
        
        kernel_hitmiss = np.array([[ 0,  1,  0],
                                [ 1, -1,  1],
                                [ 0,  1,  0]], np.int8)

        pruned_img = cv2.morphologyEx(skeleton_img, cv2.MORPH_HITMISS, kernel_hitmiss)
        
        # Konversi hasil ke biner (0 dan 255)
        pruned_img[pruned_img == 1] = 255
        pruned_img[pruned_img != 255] = 0
        
        # Gunakan dilasi untuk mempertajam hasil pruning jika perlu
        pruned_img = cv2.dilate(pruned_img, np.ones((3, 3), np.uint8), iterations=1)

        outputPath = os.path.join(os.getcwd(), MenuMorfologi.outputFile)
        cv2.imwrite(outputPath, pruned_img)
        
        return outputPath


MenuMorfologi.prune_skeleton(rf'C:\Users\Achmad Baihaqi\Pictures\PCV\city-bali.png')

