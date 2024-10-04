from PIL import Image
import os
import subprocess
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QAction, QApplication, QMainWindow
from logic.menu_file import MenuFile
from logic.menu_color import MenuColor
from logic.menu_image_proc import MenuImageProc
from logic.menu_view import MenuView
from logic.menu_geometrik import MenuGeometrik
from logic.menu_segmentasi import MenuSegmentasi
from logic.menu_morfologi import MenuMorfologi
from logic.menu_edge_detection import MenuEdgeDetection
from dialog_tentang import Ui_DialogAbout
from dialog_translate_image import Ui_TranslateImage
from dialog_factor_linear import Ui_DialogFactorLinear
from dialog_rotate_image import Ui_RotateImage
from dialog_zoom_image import Ui_ZoomImage
from dialog_crop_image import Ui_CropImage
from dialog_seed import Ui_RegionGrowing
from dialog_kmeans_clustering import Ui_KmeansCLus
from dialog_global_thresholding import Ui_GlobalThres

class Ui_MainWindow(object):

    imageInputPath = ''
    currentFilename = ''
    imageOutputPath = ''
    imageOutputPathDef = '\\output.png'
    outputFile = rf".\output\output.png"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1322, 678)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imageInput = QtWidgets.QGraphicsView(self.centralwidget)
        self.imageInput.setGeometry(QtCore.QRect(20, 20, 631, 541))
        self.imageInput.setObjectName("imageInput")
        self.imageOutput = QtWidgets.QGraphicsView(self.centralwidget)
        self.imageOutput.setGeometry(QtCore.QRect(671, 20, 631, 541))
        self.imageOutput.setObjectName("imageOutput")
        self.toolStripLabel = QtWidgets.QLabel(self.centralwidget)
        self.toolStripLabel.setGeometry(QtCore.QRect(20, 609, 991, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolStripLabel.sizePolicy().hasHeightForWidth())
        self.toolStripLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolStripLabel.setFont(font)
        self.toolStripLabel.setObjectName("toolStripLabel")
        self.btnOpenImage = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenImage.setGeometry(QtCore.QRect(1160, 580, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnOpenImage.setFont(font)
        self.btnOpenImage.setObjectName("btnOpenImage")
        self.toolStripAction = QtWidgets.QLabel(self.centralwidget)
        self.toolStripAction.setGeometry(QtCore.QRect(20, 580, 991, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolStripAction.sizePolicy().hasHeightForWidth())
        self.toolStripAction.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolStripAction.setFont(font)
        self.toolStripAction.setObjectName("toolStripAction")
        self.btnInputPhoto = QtWidgets.QPushButton(self.centralwidget)
        self.btnInputPhoto.setGeometry(QtCore.QRect(1020, 580, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnInputPhoto.setFont(font)
        self.btnInputPhoto.setObjectName("btnInputPhoto")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1322, 31))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuINput = QtWidgets.QMenu(self.menubar)
        self.menuINput.setObjectName("menuINput")
        self.menuHIstogram = QtWidgets.QMenu(self.menuINput)
        self.menuHIstogram.setObjectName("menuHIstogram")
        self.menuColors = QtWidgets.QMenu(self.menubar)
        self.menuColors.setObjectName("menuColors")
        self.menuRGB = QtWidgets.QMenu(self.menuColors)
        self.menuRGB.setObjectName("menuRGB")
        self.menuRGB_to_Grayscale = QtWidgets.QMenu(self.menuColors)
        self.menuRGB_to_Grayscale.setObjectName("menuRGB_to_Grayscale")
        self.menuLInear = QtWidgets.QMenu(self.menuColors)
        self.menuLInear.setObjectName("menuLInear")
        self.menuQuantize = QtWidgets.QMenu(self.menuColors)
        self.menuQuantize.setObjectName("menuQuantize")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuHistogram_Equalization = QtWidgets.QMenu(self.menubar)
        self.menuHistogram_Equalization.setObjectName("menuHistogram_Equalization")
        self.menuAritmetical_Operation = QtWidgets.QMenu(self.menubar)
        self.menuAritmetical_Operation.setObjectName("menuAritmetical_Operation")
        self.menuFilter = QtWidgets.QMenu(self.menubar)
        self.menuFilter.setObjectName("menuFilter")
        self.menuEdge_Detection = QtWidgets.QMenu(self.menuFilter)
        self.menuEdge_Detection.setObjectName("menuEdge_Detection")
        self.menuGaussian_Blur = QtWidgets.QMenu(self.menuFilter)
        self.menuGaussian_Blur.setObjectName("menuGaussian_Blur")
        self.menuEdge_Detection_2 = QtWidgets.QMenu(self.menubar)
        self.menuEdge_Detection_2.setObjectName("menuEdge_Detection_2")
        self.menuMorfologi = QtWidgets.QMenu(self.menubar)
        self.menuMorfologi.setObjectName("menuMorfologi")
        self.menuErosion = QtWidgets.QMenu(self.menuMorfologi)
        self.menuErosion.setObjectName("menuErosion")
        self.menuDilation = QtWidgets.QMenu(self.menuMorfologi)
        self.menuDilation.setObjectName("menuDilation")
        self.menuOpening = QtWidgets.QMenu(self.menuMorfologi)
        self.menuOpening.setObjectName("menuOpening")
        self.menuClosing = QtWidgets.QMenu(self.menuMorfologi)
        self.menuClosing.setObjectName("menuClosing")
        self.menuGeometrics = QtWidgets.QMenu(self.menubar)
        self.menuGeometrics.setObjectName("menuGeometrics")
        self.menuFlip_Image = QtWidgets.QMenu(self.menuGeometrics)
        self.menuFlip_Image.setObjectName("menuFlip_Image")
        self.menuSegmentation = QtWidgets.QMenu(self.menubar)
        self.menuSegmentation.setObjectName("menuSegmentation")
        self.menuAdaptive_Thresh = QtWidgets.QMenu(self.menuSegmentation)
        self.menuAdaptive_Thresh.setObjectName("menuAdaptive_Thresh")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionInput = QtWidgets.QAction(MainWindow)
        self.actionInput.setObjectName("actionInput")
        self.actionOutput = QtWidgets.QAction(MainWindow)
        self.actionOutput.setObjectName("actionOutput")
        self.actionInput_Output = QtWidgets.QAction(MainWindow)
        self.actionInput_Output.setObjectName("actionInput_Output")
        self.actionBrightness_Constrast = QtWidgets.QAction(MainWindow)
        self.actionBrightness_Constrast.setObjectName("actionBrightness_Constrast")
        self.actionInvers = QtWidgets.QAction(MainWindow)
        self.actionInvers.setObjectName("actionInvers")
        self.actionLog_Brightness = QtWidgets.QAction(MainWindow)
        self.actionLog_Brightness.setObjectName("actionLog_Brightness")
        self.actionGamma_Correction = QtWidgets.QAction(MainWindow)
        self.actionGamma_Correction.setObjectName("actionGamma_Correction")
        self.actionYellow = QtWidgets.QAction(MainWindow)
        self.actionYellow.setObjectName("actionYellow")
        self.actionOrange = QtWidgets.QAction(MainWindow)
        self.actionOrange.setObjectName("actionOrange")
        self.actionCyan = QtWidgets.QAction(MainWindow)
        self.actionCyan.setObjectName("actionCyan")
        self.actionPurple = QtWidgets.QAction(MainWindow)
        self.actionPurple.setObjectName("actionPurple")
        self.actionGrey = QtWidgets.QAction(MainWindow)
        self.actionGrey.setObjectName("actionGrey")
        self.actionChocolate = QtWidgets.QAction(MainWindow)
        self.actionChocolate.setObjectName("actionChocolate")
        self.actionRed = QtWidgets.QAction(MainWindow)
        self.actionRed.setObjectName("actionRed")
        self.actionAverage = QtWidgets.QAction(MainWindow)
        self.actionAverage.setObjectName("actionAverage")
        self.actionLightness = QtWidgets.QAction(MainWindow)
        self.actionLightness.setObjectName("actionLightness")
        self.actionLuminance = QtWidgets.QAction(MainWindow)
        self.actionLuminance.setObjectName("actionLuminance")
        self.actionConstrast = QtWidgets.QAction(MainWindow)
        self.actionConstrast.setObjectName("actionConstrast")
        self.action1_bit = QtWidgets.QAction(MainWindow)
        self.action1_bit.setObjectName("action1_bit")
        self.action2_bit = QtWidgets.QAction(MainWindow)
        self.action2_bit.setObjectName("action2_bit")
        self.action3_bit = QtWidgets.QAction(MainWindow)
        self.action3_bit.setObjectName("action3_bit")
        self.action4_bit = QtWidgets.QAction(MainWindow)
        self.action4_bit.setObjectName("action4_bit")
        self.action5_bit = QtWidgets.QAction(MainWindow)
        self.action5_bit.setObjectName("action5_bit")
        self.action6_bit = QtWidgets.QAction(MainWindow)
        self.action6_bit.setObjectName("action6_bit")
        self.action7_bit = QtWidgets.QAction(MainWindow)
        self.action7_bit.setObjectName("action7_bit")
        self.actionHistogram_Equalization = QtWidgets.QAction(MainWindow)
        self.actionHistogram_Equalization.setObjectName("actionHistogram_Equalization")
        self.actionFuzzy_HE_RGB = QtWidgets.QAction(MainWindow)
        self.actionFuzzy_HE_RGB.setObjectName("actionFuzzy_HE_RGB")
        self.actionFuzzy_Grayscale = QtWidgets.QAction(MainWindow)
        self.actionFuzzy_Grayscale.setObjectName("actionFuzzy_Grayscale")
        self.actionIdentity = QtWidgets.QAction(MainWindow)
        self.actionIdentity.setObjectName("actionIdentity")
        self.actionSharpen = QtWidgets.QAction(MainWindow)
        self.actionSharpen.setObjectName("actionSharpen")
        self.actionUnsharp_Masking = QtWidgets.QAction(MainWindow)
        self.actionUnsharp_Masking.setObjectName("actionUnsharp_Masking")
        self.actionAverage_Filter = QtWidgets.QAction(MainWindow)
        self.actionAverage_Filter.setObjectName("actionAverage_Filter")
        self.actionLow_Pass_Filter = QtWidgets.QAction(MainWindow)
        self.actionLow_Pass_Filter.setObjectName("actionLow_Pass_Filter")
        self.actionHight_Pass_Filter = QtWidgets.QAction(MainWindow)
        self.actionHight_Pass_Filter.setObjectName("actionHight_Pass_Filter")
        self.actionBandstop_Filter = QtWidgets.QAction(MainWindow)
        self.actionBandstop_Filter.setObjectName("actionBandstop_Filter")
        self.actionEdge_Detection_1 = QtWidgets.QAction(MainWindow)
        self.actionEdge_Detection_1.setObjectName("actionEdge_Detection_1")
        self.actionEdge_Detection_2 = QtWidgets.QAction(MainWindow)
        self.actionEdge_Detection_2.setObjectName("actionEdge_Detection_2")
        self.actionEdge_Detection_3 = QtWidgets.QAction(MainWindow)
        self.actionEdge_Detection_3.setObjectName("actionEdge_Detection_3")
        self.actionGaussian_Blur_3x3 = QtWidgets.QAction(MainWindow)
        self.actionGaussian_Blur_3x3.setObjectName("actionGaussian_Blur_3x3")
        self.actionGaussian_Blur_3x5 = QtWidgets.QAction(MainWindow)
        self.actionGaussian_Blur_3x5.setObjectName("actionGaussian_Blur_3x5")
        self.actionPrewitt = QtWidgets.QAction(MainWindow)
        self.actionPrewitt.setObjectName("actionPrewitt")
        self.actionSebel = QtWidgets.QAction(MainWindow)
        self.actionSebel.setObjectName("actionSebel")
        self.actionErosionSquare_3 = QtWidgets.QAction(MainWindow)
        self.actionErosionSquare_3.setObjectName("actionErosionSquare_3")
        self.actionErosionSquare_5 = QtWidgets.QAction(MainWindow)
        self.actionErosionSquare_5.setObjectName("actionErosionSquare_5")
        self.actionErosionCross_3 = QtWidgets.QAction(MainWindow)
        self.actionErosionCross_3.setObjectName("actionErosionCross_3")
        self.actionDilationSquare_3 = QtWidgets.QAction(MainWindow)
        self.actionDilationSquare_3.setObjectName("actionDilationSquare_3")
        self.actionDilationSquare_5 = QtWidgets.QAction(MainWindow)
        self.actionDilationSquare_5.setObjectName("actionDilationSquare_5")
        self.actionDilationCross_5 = QtWidgets.QAction(MainWindow)
        self.actionDilationCross_5.setObjectName("actionDilationCross_5")
        self.actionOpeningSquare_9 = QtWidgets.QAction(MainWindow)
        self.actionOpeningSquare_9.setObjectName("actionOpeningSquare_9")
        self.actionClosingSquare_9 = QtWidgets.QAction(MainWindow)
        self.actionClosingSquare_9.setObjectName("actionClosingSquare_9")
        self.actionBersihkan = QtWidgets.QAction(MainWindow)
        self.actionBersihkan.setObjectName("actionBersihkan")
        self.actionClearImage = QtWidgets.QAction(MainWindow)
        self.actionClearImage.setObjectName("actionClearImage")
        self.actionSaturation = QtWidgets.QAction(MainWindow)
        self.actionSaturation.setObjectName("actionSaturation")
        self.actionBrightness = QtWidgets.QAction(MainWindow)
        self.actionBrightness.setObjectName("actionBrightness")
        self.actionLevel_1 = QtWidgets.QAction(MainWindow)
        self.actionLevel_1.setObjectName("actionLevel_1")
        self.actionLevel_2 = QtWidgets.QAction(MainWindow)
        self.actionLevel_2.setObjectName("actionLevel_2")
        self.actionLevel_3 = QtWidgets.QAction(MainWindow)
        self.actionLevel_3.setObjectName("actionLevel_3")
        self.actionLevel_4 = QtWidgets.QAction(MainWindow)
        self.actionLevel_4.setObjectName("actionLevel_4")
        self.actionLevel_5 = QtWidgets.QAction(MainWindow)
        self.actionLevel_5.setObjectName("actionLevel_5")
        self.actionLevel_6 = QtWidgets.QAction(MainWindow)
        self.actionLevel_6.setObjectName("actionLevel_6")
        self.actionLevel_7 = QtWidgets.QAction(MainWindow)
        self.actionLevel_7.setObjectName("actionLevel_7")
        self.actionShow_Histogram_Citra = QtWidgets.QAction(MainWindow)
        self.actionShow_Histogram_Citra.setObjectName("actionShow_Histogram_Citra")
        self.actionTranslate_Image = QtWidgets.QAction(MainWindow)
        self.actionTranslate_Image.setObjectName("actionTranslate_Image")
        self.actionRotate_Image = QtWidgets.QAction(MainWindow)
        self.actionRotate_Image.setObjectName("actionRotate_Image")
        self.actionZoom_Image = QtWidgets.QAction(MainWindow)
        self.actionZoom_Image.setObjectName("actionZoom_Image")
        self.actionCrop_Image = QtWidgets.QAction(MainWindow)
        self.actionCrop_Image.setObjectName("actionCrop_Image")
        self.actionAdjust = QtWidgets.QAction(MainWindow)
        self.actionAdjust.setObjectName("actionAdjust")
        self.actionHorizontal = QtWidgets.QAction(MainWindow)
        self.actionHorizontal.setObjectName("actionHorizontal")
        self.actionVertical = QtWidgets.QAction(MainWindow)
        self.actionVertical.setObjectName("actionVertical")
        self.actionRegion_Growing = QtWidgets.QAction(MainWindow)
        self.actionRegion_Growing.setObjectName("actionRegion_Growing")
        self.actionKmeans_Clustering = QtWidgets.QAction(MainWindow)
        self.actionKmeans_Clustering.setObjectName("actionKmeans_Clustering")
        self.actionWatershed_Segmentation = QtWidgets.QAction(MainWindow)
        self.actionWatershed_Segmentation.setObjectName("actionWatershed_Segmentation")
        self.actionGlobal_Thresholding = QtWidgets.QAction(MainWindow)
        self.actionGlobal_Thresholding.setObjectName("actionGlobal_Thresholding")
        self.actionMean = QtWidgets.QAction(MainWindow)
        self.actionMean.setObjectName("actionMean")
        self.actionGaussian = QtWidgets.QAction(MainWindow)
        self.actionGaussian.setObjectName("actionGaussian")
        self.actionHit_Or_Miss = QtWidgets.QAction(MainWindow)
        self.actionHit_Or_Miss.setObjectName("actionHit_Or_Miss")
        self.actionThinned = QtWidgets.QAction(MainWindow)
        self.actionThinned.setObjectName("actionThinned")
        self.actionSkeleton = QtWidgets.QAction(MainWindow)
        self.actionSkeleton.setObjectName("actionSkeleton")
        self.actionPrune_Skeleton = QtWidgets.QAction(MainWindow)
        self.actionPrune_Skeleton.setObjectName("actionPrune_Skeleton")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionClearImage)
        self.menuFile.addAction(self.actionClose)
        self.menuHIstogram.addAction(self.actionInput)
        self.menuHIstogram.addAction(self.actionOutput)
        self.menuHIstogram.addAction(self.actionInput_Output)
        self.menuINput.addAction(self.menuHIstogram.menuAction())
        self.menuRGB.addAction(self.actionYellow)
        self.menuRGB.addAction(self.actionOrange)
        self.menuRGB.addAction(self.actionCyan)
        self.menuRGB.addAction(self.actionPurple)
        self.menuRGB.addAction(self.actionGrey)
        self.menuRGB.addAction(self.actionChocolate)
        self.menuRGB.addAction(self.actionRed)
        self.menuRGB_to_Grayscale.addAction(self.actionAverage)
        self.menuRGB_to_Grayscale.addAction(self.actionLightness)
        self.menuRGB_to_Grayscale.addAction(self.actionLuminance)
        self.menuLInear.addAction(self.actionBrightness)
        self.menuLInear.addAction(self.actionConstrast)
        self.menuLInear.addAction(self.actionSaturation)
        self.menuLInear.addAction(self.actionAdjust)
        self.menuQuantize.addAction(self.actionLevel_1)
        self.menuQuantize.addAction(self.actionLevel_2)
        self.menuQuantize.addAction(self.actionLevel_3)
        self.menuQuantize.addAction(self.actionLevel_4)
        self.menuQuantize.addAction(self.actionLevel_5)
        self.menuQuantize.addAction(self.actionLevel_6)
        self.menuQuantize.addAction(self.actionLevel_7)
        self.menuColors.addAction(self.menuRGB.menuAction())
        self.menuColors.addAction(self.menuQuantize.menuAction())
        self.menuColors.addAction(self.menuRGB_to_Grayscale.menuAction())
        self.menuColors.addAction(self.menuLInear.menuAction())
        self.menuColors.addAction(self.actionInvers)
        self.menuColors.addAction(self.actionLog_Brightness)
        self.menuColors.addAction(self.actionGamma_Correction)
        self.menuHistogram_Equalization.addAction(self.actionShow_Histogram_Citra)
        self.menuHistogram_Equalization.addAction(self.actionHistogram_Equalization)
        self.menuHistogram_Equalization.addAction(self.actionFuzzy_HE_RGB)
        self.menuHistogram_Equalization.addAction(self.actionFuzzy_Grayscale)
        self.menuEdge_Detection.addAction(self.actionEdge_Detection_1)
        self.menuEdge_Detection.addAction(self.actionEdge_Detection_2)
        self.menuEdge_Detection.addAction(self.actionEdge_Detection_3)
        self.menuGaussian_Blur.addAction(self.actionGaussian_Blur_3x3)
        self.menuGaussian_Blur.addAction(self.actionGaussian_Blur_3x5)
        self.menuFilter.addAction(self.actionIdentity)
        self.menuFilter.addAction(self.menuEdge_Detection.menuAction())
        self.menuFilter.addAction(self.actionSharpen)
        self.menuFilter.addAction(self.menuGaussian_Blur.menuAction())
        self.menuFilter.addAction(self.actionUnsharp_Masking)
        self.menuFilter.addAction(self.actionAverage_Filter)
        self.menuFilter.addAction(self.actionLow_Pass_Filter)
        self.menuFilter.addAction(self.actionHight_Pass_Filter)
        self.menuFilter.addAction(self.actionBandstop_Filter)
        self.menuEdge_Detection_2.addAction(self.actionPrewitt)
        self.menuEdge_Detection_2.addAction(self.actionSebel)
        self.menuErosion.addAction(self.actionErosionSquare_3)
        self.menuErosion.addAction(self.actionErosionSquare_5)
        self.menuErosion.addAction(self.actionErosionCross_3)
        self.menuDilation.addAction(self.actionDilationSquare_3)
        self.menuDilation.addAction(self.actionDilationSquare_5)
        self.menuDilation.addAction(self.actionDilationCross_5)
        self.menuOpening.addAction(self.actionOpeningSquare_9)
        self.menuClosing.addAction(self.actionClosingSquare_9)
        self.menuMorfologi.addAction(self.menuErosion.menuAction())
        self.menuMorfologi.addAction(self.menuDilation.menuAction())
        self.menuMorfologi.addAction(self.menuOpening.menuAction())
        self.menuMorfologi.addAction(self.menuClosing.menuAction())
        self.menuMorfologi.addAction(self.actionHit_Or_Miss)
        self.menuMorfologi.addAction(self.actionThinned)
        self.menuMorfologi.addAction(self.actionSkeleton)
        self.menuMorfologi.addAction(self.actionPrune_Skeleton)
        self.menuFlip_Image.addAction(self.actionHorizontal)
        self.menuFlip_Image.addAction(self.actionVertical)
        self.menuGeometrics.addAction(self.actionTranslate_Image)
        self.menuGeometrics.addAction(self.actionRotate_Image)
        self.menuGeometrics.addAction(self.menuFlip_Image.menuAction())
        self.menuGeometrics.addAction(self.actionZoom_Image)
        self.menuGeometrics.addAction(self.actionCrop_Image)
        self.menuAdaptive_Thresh.addAction(self.actionMean)
        self.menuAdaptive_Thresh.addAction(self.actionGaussian)
        self.menuSegmentation.addAction(self.actionRegion_Growing)
        self.menuSegmentation.addAction(self.actionKmeans_Clustering)
        self.menuSegmentation.addAction(self.actionWatershed_Segmentation)
        self.menuSegmentation.addAction(self.actionGlobal_Thresholding)
        self.menuSegmentation.addAction(self.menuAdaptive_Thresh.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuINput.menuAction())
        self.menubar.addAction(self.menuColors.menuAction())
        self.menubar.addAction(self.menuGeometrics.menuAction())
        self.menubar.addAction(self.menuSegmentation.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHistogram_Equalization.menuAction())
        self.menubar.addAction(self.menuAritmetical_Operation.menuAction())
        self.menubar.addAction(self.menuFilter.menuAction())
        self.menubar.addAction(self.menuEdge_Detection_2.menuAction())
        self.menubar.addAction(self.menuMorfologi.menuAction())

        # Connect actions to slots
        self.action(MainWindow)  

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kelompok C2"))
        self.toolStripLabel.setText(_translate("MainWindow", "toolStripFile"))
        self.btnOpenImage.setText(_translate("MainWindow", "Output Photo"))
        self.toolStripAction.setText(_translate("MainWindow", "toolStripAction"))
        self.btnInputPhoto.setText(_translate("MainWindow", "Input Photo"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuINput.setTitle(_translate("MainWindow", "View"))
        self.menuHIstogram.setTitle(_translate("MainWindow", "HIstogram"))
        self.menuColors.setTitle(_translate("MainWindow", "Colors"))
        self.menuRGB.setTitle(_translate("MainWindow", "RGB"))
        self.menuRGB_to_Grayscale.setTitle(_translate("MainWindow", "RGB to Grayscale"))
        self.menuLInear.setTitle(_translate("MainWindow", "Linear"))
        self.menuQuantize.setTitle(_translate("MainWindow", "Quantize"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuHistogram_Equalization.setTitle(_translate("MainWindow", "Image Processing"))
        self.menuAritmetical_Operation.setTitle(_translate("MainWindow", "Aritmetical Operation"))
        self.menuFilter.setTitle(_translate("MainWindow", "Filter"))
        self.menuEdge_Detection.setTitle(_translate("MainWindow", "Edge Detection"))
        self.menuGaussian_Blur.setTitle(_translate("MainWindow", "Gaussian Blur"))
        self.menuEdge_Detection_2.setTitle(_translate("MainWindow", "Edge Detection"))
        self.menuMorfologi.setTitle(_translate("MainWindow", "Morphology"))
        self.menuErosion.setTitle(_translate("MainWindow", "Erosion"))
        self.menuDilation.setTitle(_translate("MainWindow", "Dilation"))
        self.menuOpening.setTitle(_translate("MainWindow", "Opening"))
        self.menuClosing.setTitle(_translate("MainWindow", "Closing"))
        self.menuGeometrics.setTitle(_translate("MainWindow", "Geometrics"))
        self.menuFlip_Image.setTitle(_translate("MainWindow", "Flip Image"))
        self.menuSegmentation.setTitle(_translate("MainWindow", "Segmentation"))
        self.menuAdaptive_Thresh.setTitle(_translate("MainWindow", "Adaptive Thresh"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save As.."))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionInput.setText(_translate("MainWindow", "Input"))
        self.actionOutput.setText(_translate("MainWindow", "Output"))
        self.actionInput_Output.setText(_translate("MainWindow", "Input Output"))
        self.actionBrightness_Constrast.setText(_translate("MainWindow", "Brightness - Constrast"))
        self.actionInvers.setText(_translate("MainWindow", "Invers"))
        self.actionLog_Brightness.setText(_translate("MainWindow", "Log Brightness"))
        self.actionGamma_Correction.setText(_translate("MainWindow", "Gamma Correction"))
        self.actionYellow.setText(_translate("MainWindow", "Yellow"))
        self.actionOrange.setText(_translate("MainWindow", "Orange"))
        self.actionCyan.setText(_translate("MainWindow", "Cyan"))
        self.actionPurple.setText(_translate("MainWindow", "Purple"))
        self.actionGrey.setText(_translate("MainWindow", "Grey"))
        self.actionChocolate.setText(_translate("MainWindow", "Chocolate"))
        self.actionRed.setText(_translate("MainWindow", "Red"))
        self.actionAverage.setText(_translate("MainWindow", "Average"))
        self.actionLightness.setText(_translate("MainWindow", "Lightness"))
        self.actionLuminance.setText(_translate("MainWindow", "Luminance"))
        self.actionConstrast.setText(_translate("MainWindow", "Constrast"))
        self.action1_bit.setText(_translate("MainWindow", "1 bit"))
        self.action2_bit.setText(_translate("MainWindow", "2 bit"))
        self.action3_bit.setText(_translate("MainWindow", "3 bit"))
        self.action4_bit.setText(_translate("MainWindow", "4 bit"))
        self.action5_bit.setText(_translate("MainWindow", "5 bit"))
        self.action6_bit.setText(_translate("MainWindow", "6 bit"))
        self.action7_bit.setText(_translate("MainWindow", "7 bit"))
        self.actionHistogram_Equalization.setText(_translate("MainWindow", "Histogram Equalization"))
        self.actionFuzzy_HE_RGB.setText(_translate("MainWindow", "Fuzzy HE RGB"))
        self.actionFuzzy_Grayscale.setText(_translate("MainWindow", "Fuzzy Grayscale"))
        self.actionIdentity.setText(_translate("MainWindow", "Identity"))
        self.actionSharpen.setText(_translate("MainWindow", "Sharpen"))
        self.actionUnsharp_Masking.setText(_translate("MainWindow", "Unsharp Masking"))
        self.actionAverage_Filter.setText(_translate("MainWindow", "Average Filter"))
        self.actionLow_Pass_Filter.setText(_translate("MainWindow", "Low Pass Filter"))
        self.actionHight_Pass_Filter.setText(_translate("MainWindow", "High Pass Filter"))
        self.actionBandstop_Filter.setText(_translate("MainWindow", "Bandstop Filter"))
        self.actionEdge_Detection_1.setText(_translate("MainWindow", "Edge Detection 1"))
        self.actionEdge_Detection_2.setText(_translate("MainWindow", "Edge Detection 2"))
        self.actionEdge_Detection_3.setText(_translate("MainWindow", "Edge Detection 3"))
        self.actionGaussian_Blur_3x3.setText(_translate("MainWindow", "Gaussian Blur 3x3"))
        self.actionGaussian_Blur_3x5.setText(_translate("MainWindow", "Gaussian Blur 3x5"))
        self.actionPrewitt.setText(_translate("MainWindow", "Prewitt"))
        self.actionSebel.setText(_translate("MainWindow", "Sebel"))
        self.actionErosionSquare_3.setText(_translate("MainWindow", "Square 3"))
        self.actionErosionSquare_5.setText(_translate("MainWindow", "Square 5"))
        self.actionErosionCross_3.setText(_translate("MainWindow", "Cross 3"))
        self.actionDilationSquare_3.setText(_translate("MainWindow", "Square 3"))
        self.actionDilationSquare_5.setText(_translate("MainWindow", "Square 5"))
        self.actionDilationCross_5.setText(_translate("MainWindow", "Cross 3"))
        self.actionOpeningSquare_9.setText(_translate("MainWindow", "Square 9"))
        self.actionClosingSquare_9.setText(_translate("MainWindow", "Square 9"))
        self.actionBersihkan.setText(_translate("MainWindow", "Bersihkan"))
        self.actionClearImage.setText(_translate("MainWindow", "Clear Image"))
        self.actionSaturation.setText(_translate("MainWindow", "Saturation"))
        self.actionBrightness.setText(_translate("MainWindow", "Brightness"))
        self.actionLevel_1.setText(_translate("MainWindow", "Level 1"))
        self.actionLevel_2.setText(_translate("MainWindow", "Level 2"))
        self.actionLevel_3.setText(_translate("MainWindow", "Level 3"))
        self.actionLevel_4.setText(_translate("MainWindow", "Level 4"))
        self.actionLevel_5.setText(_translate("MainWindow", "Level 5"))
        self.actionLevel_6.setText(_translate("MainWindow", "Level 6"))
        self.actionLevel_7.setText(_translate("MainWindow", "Level 7"))
        self.actionShow_Histogram_Citra.setText(_translate("MainWindow", "Show Histogram Citra"))
        self.actionTranslate_Image.setText(_translate("MainWindow", "Translate Image"))
        self.actionRotate_Image.setText(_translate("MainWindow", "Rotate Image"))
        self.actionZoom_Image.setText(_translate("MainWindow", "Zoom Image"))
        self.actionCrop_Image.setText(_translate("MainWindow", "Crop Image"))
        self.actionAdjust.setText(_translate("MainWindow", "Adjust"))
        self.actionHorizontal.setText(_translate("MainWindow", "Horizontal"))
        self.actionVertical.setText(_translate("MainWindow", "Vertical"))
        self.actionRegion_Growing.setText(_translate("MainWindow", "Region Growing"))
        self.actionKmeans_Clustering.setText(_translate("MainWindow", "Kmeans Clustering"))
        self.actionWatershed_Segmentation.setText(_translate("MainWindow", "Watershed Segmentation"))
        self.actionGlobal_Thresholding.setText(_translate("MainWindow", "Global Thresholding"))
        self.actionMean.setText(_translate("MainWindow", "Mean"))
        self.actionGaussian.setText(_translate("MainWindow", "Gaussian"))
        self.actionHit_Or_Miss.setText(_translate("MainWindow", "Hit Or Miss"))
        self.actionThinned.setText(_translate("MainWindow", "Thinned"))
        self.actionSkeleton.setText(_translate("MainWindow", "Skeleton"))
        self.actionPrune_Skeleton.setText(_translate("MainWindow", "Prune Skeleton"))

    # semua aksi pada window
    def action(self, MainWindow):
        self.actionOpen.triggered.connect(self.openFile)
        self.actionClose.triggered.connect(MainWindow.close)
        self.actionClearImage.triggered.connect(self.clearImage)
        self.actionAverage.triggered.connect(self.grayscale_average)
        self.actionLightness.triggered.connect(self.grayscale_lightness)
        self.actionLuminance.triggered.connect(self.grayscale_luminance)
        self.actionLevel_1.triggered.connect(self.quantize_level_1)
        self.actionLevel_2.triggered.connect(self.quantize_level_2)
        self.actionLevel_3.triggered.connect(self.quantize_level_3)
        self.actionLevel_4.triggered.connect(self.quantize_level_4)
        self.actionLevel_5.triggered.connect(self.quantize_level_5)
        self.actionLevel_6.triggered.connect(self.quantize_level_6)
        self.actionLevel_7.triggered.connect(self.quantize_level_7)
        self.actionBrightness.triggered.connect(self.linear_brightness)
        self.actionConstrast.triggered.connect(self.linear_contrast)
        self.actionSaturation.triggered.connect(self.linear_saturation)
        self.actionAdjust.triggered.connect(self.linear_adjust)
        self.actionInvers.triggered.connect(self.inverse)
        self.actionLog_Brightness.triggered.connect(self.log_brightness)
        self.actionSaveAs.triggered.connect(self.saveAs)
        self.actionInput.triggered.connect(self.input_histogram)
        self.actionOutput.triggered.connect(self.output_histogram)
        self.actionInput_Output.triggered.connect(self.input_output_histogram)
        self.btnOpenImage.clicked.connect(self.open_ouput_in_photo)
        self.btnInputPhoto.clicked.connect(self.open_input_in_photo)
        self.actionShow_Histogram_Citra.triggered.connect(self.histogram_citra)
        self.actionHistogram_Equalization.triggered.connect(self.histogram_equalization)
        self.actionFuzzy_HE_RGB.triggered.connect(self.fuzzy_he_rgb)
        self.actionFuzzy_Grayscale.triggered.connect(self.fuzzy_grayscale)
        # geomterics
        self.actionTranslate_Image.triggered.connect(self.show_dialog_translate_image)
        self.actionRotate_Image.triggered.connect(self.show_dialog_rotate_image)
        self.actionZoom_Image.triggered.connect(self.show_dialog_zoom_image)
        self.actionHorizontal.triggered.connect(self.flipHorizontal)
        self.actionVertical.triggered.connect(self.flipVertical)
        self.actionCrop_Image.triggered.connect(self.show_dialog_crop_image)
        # segmentations
        self.actionRegion_Growing.triggered.connect(self.region_growing)
        self.actionKmeans_Clustering.triggered.connect(self.kmeans_clustering)
        self.actionWatershed_Segmentation.triggered.connect(self.watershed_segmentation)
        self.actionGlobal_Thresholding.triggered.connect(self.global_thresholding)
        self.actionMean.triggered.connect(self.adaptive_thresh_mean)
        self.actionGaussian.triggered.connect(self.adaptive_thresh_gaussian)
        # morfologi
        self.actionErosionSquare_3.triggered.connect(self.erotion33)
        self.actionErosionSquare_5.triggered.connect(self.erotion53)
        self.actionErosionCross_3.triggered.connect(self.erotion3)
        self.actionDilationSquare_3.triggered.connect(self.dilate33)
        self.actionDilationSquare_5.triggered.connect(self.dilate53)
        self.actionDilationCross_5.triggered.connect(self.dilate3)
        self.actionOpeningSquare_9.triggered.connect(self.opening9)
        self.actionClosingSquare_9.triggered.connect(self.closing9)
        # edge detection
        self.actionSebel.triggered.connect(self.sobel)
        self.actionPrewitt.triggered.connect(self.prewit)

    # digunakan untuk menampilkan gambar hasil processing ke output
    def showToOutput(self, actionName):
        pixmap = QtGui.QPixmap(self.outputFile)
        scene = QtWidgets.QGraphicsScene()
        scene.addPixmap(pixmap)
        self.toolStripAction.setText(rf"ACTION : {actionName}")
        self.imageOutput.setScene(scene)

    # digunakan untuk memngambil gambar input
    def openFile(self):
        print('choose image from explorer')
        self.imageInputPath = MenuFile.openFile(self)
        self.imageOutputPath = os.path.dirname(self.imageInputPath)
        self.currentFilename = os.path.basename(self.imageInputPath)
        self.toolStripLabel.setText(rf"IMAGE : {self.imageInputPath}")
        self.toolStripAction.setText("No Action Selected")
    
    # digunakan untuk menyimpan hasil output dari processing
    def saveAs(self):
        if not os.path.exists(self.outputFile):
            QMessageBox.warning(None, "Warning", "Output file does not exist.")
            return

        # Open Save As dialog
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getSaveFileName(None, "Save Image As", "", 
                                                "PNG Files (*.png);;JPEG Files (*.jpg);;All Files (*)", 
                                                options=options)
        if filePath:
            try:
                # Save the file to the chosen path
                image = Image.open(self.outputFile)
                image.save(filePath)
                QMessageBox.information(None, "Success", "Image saved successfully.")
            except Exception as e:
                QMessageBox.critical(None, "Error", f"Failed to save the image: {str(e)}")

    # membersihkan image baik input maupun output
    def clearImage(self):
        MenuFile.clearImage(self)
        self.imageInputPath = ''
        self.toolStripLabel.setText(self.imageInputPath)
        self.toolStripAction.setText("No Action Selected")

    # membuka gambar hasil processing ke photo
    def open_ouput_in_photo(self):
        image_path = self.outputFile
        # Cek apakah file gambar ada
        if os.path.exists(image_path):
            try:
                # Membuka gambar dengan aplikasi Photo
                os.startfile(image_path)
                print(f"Gambar {image_path} dibuka di Photo.")
            except Exception as e:
                print(f"Error saat membuka gambar: {e}")
        else:
            print(f"File {image_path} tidak ditemukan.")

    # membuka gambar hasil processing ke photo
    def open_input_in_photo(self):
        image_path = self.imageInputPath
        # Cek apakah file gambar ada
        if os.path.exists(image_path):
            try:
                # Membuka gambar dengan aplikasi Photo
                os.startfile(image_path)
                print(f"Gambar {image_path} dibuka di Photo.")
            except Exception as e:
                print(f"Error saat membuka gambar: {e}")
        else:
            print(f"File {image_path} tidak ditemukan.")

    def quantize_level_1(self):
        self.outputFile = MenuColor.quantize_color_level(self.imageInputPath, 1)
        self.showToOutput("Quantize Level 1")

    def quantize_level_2(self):
        self.outputFile = MenuColor.quantize_color_level(self.imageInputPath, 2)
        self.showToOutput("Quantize Level 2")

    def quantize_level_3(self):
        self.outputFile = MenuColor.quantize_color_level(self.imageInputPath, 3)
        self.showToOutput("Quantize Level 3")

    def quantize_level_4(self):
        self.outputFile = MenuColor.quantize_color_level(self.imageInputPath, 4)
        self.showToOutput("Quantize Level 4")

    def quantize_level_5(self):
        self.outputFile = MenuColor.quantize_color_level(self.imageInputPath, 5)
        self.showToOutput("Quantize Level 5")

    def quantize_level_6(self):
        self.outputFile = MenuColor.quantize_color_level(self.imageInputPath, 6)
        self.showToOutput("Quantize Level 6")

    def quantize_level_7(self):
        self.outputFile = MenuColor.quantize_color_level(self.imageInputPath, 7)
        self.showToOutput("Quantize Level 7")

    def grayscale_average(self):
        self.outputFile = MenuColor.rgb_to_grayscale_average(self.imageInputPath)
        self.showToOutput("Grayscale Average")

    def grayscale_lightness(self):
        self.outputFile = MenuColor.rgb_to_grayscale_lightness(self.imageInputPath)
        self.showToOutput("Grayscale Lightness")

    def grayscale_luminance(self):
        self.outputFile = MenuColor.rgb_to_grayscale_luminance(self.imageInputPath)
        self.showToOutput("Grayscale Luminance")

    def show_dialog_and_get_value(self, factor_type):
        """
        Menampilkan dialog dan mengambil nilai parameter berdasarkan tipe.
        """
        self.pop_up = QtWidgets.QDialog()
        self.ui = Ui_DialogFactorLinear()
        self.ui.setupUi(self.pop_up)
        result = self.pop_up.exec_()

        if result == QtWidgets.QDialog.Accepted:
            if factor_type == 'brightness':
                value = self.ui.get_brightness_factor()
                self.outputFile = MenuColor.linear_brightness(self.imageInputPath, value)
                self.showToOutput(f"Brightness Factor: {value}")
            elif factor_type == 'contrast':
                value = self.ui.get_contrast_factor()
                self.outputFile = MenuColor.linear_contrast(self.imageInputPath, value)
                self.showToOutput(f"Contrast Factor: {value}")
            elif factor_type == 'saturation':
                value = self.ui.get_saturation_factor()
                self.outputFile = MenuColor.linear_saturation(self.imageInputPath, value)
                self.showToOutput(f"Saturation Factor: {value}")
            elif factor_type == 'adjust':
                brightness = self.ui.get_brightness_factor()
                constrast = self.ui.get_contrast_factor()
                saturation = self.ui.get_saturation_factor()
                self.outputFile = MenuColor.linear_brightness(self.imageInputPath, brightness)
                self.outputFile = MenuColor.linear_saturation(self.outputFile, saturation)
                self.outputFile = MenuColor.linear_contrast(self.outputFile, constrast)
                self.showToOutput(f"Adjust Factor : brightness({brightness}) / contrast({constrast}) / saturation({saturation})")

    def linear_brightness(self):
        self.show_dialog_and_get_value('brightness')

    def linear_contrast(self):
        self.show_dialog_and_get_value('contrast')

    def linear_saturation(self):
        self.show_dialog_and_get_value('saturation')

    def linear_adjust(self):
        self.show_dialog_and_get_value('adjust')

    def inverse(self):
        self.outputFile = MenuColor.inverse(self.imageInputPath)
        self.showToOutput("Inverse")

    def log_brightness(self):
        self.outputFile = MenuColor.log_brightness(self.imageInputPath)
        self.showToOutput("Log Brightness")

    def input_histogram(self):
        MenuView.showHistogram(self.imageInputPath, "Input Histogram Image")
        self.showToOutput("Input Histogram Image")

    def output_histogram(self):
        MenuView.showHistogram(self.outputFile, "Output Histogram Image")
        self.showToOutput("Output Histogram Image")

    def input_output_histogram(self):
        MenuView.showHistogram(self.imageInputPath, "Input Histogram Image")
        MenuView.showHistogram(self.outputFile, "Ouput Histogram Image")
        self.showToOutput("Input/Output Histogram Image")

    def histogram_citra(self):
        self.outputFile = MenuImageProc.histogram_citra(self.imageInputPath)
        self.showToOutput("Histogram Citra")

    def histogram_equalization(self):
        self.outputFile = MenuImageProc.histogram_equalization(self.imageInputPath)
        self.showToOutput("Histogram Equalization")

    def fuzzy_he_rgb(self):
        self.outputFile = MenuImageProc.fuzzy_he_rgb(self.imageInputPath)
        self.showToOutput("Fuzzy HE RGB")

    def fuzzy_grayscale(self):
        self.outputFile = MenuImageProc.fuzzy_grayscale(self.imageInputPath)
        self.showToOutput("Fuzzy Grayscale")

    def show_dialog_translate_image(self):
        self.pop_up = QtWidgets.QDialog()
        self.ui = Ui_TranslateImage()
        self.ui.setupUi(self.pop_up)
        result = self.pop_up.exec_()

        if result == QtWidgets.QDialog.Accepted:
            valueX = self.ui.get_x()
            valueY = self.ui.get_y()
            self.outputFile = MenuGeometrik.translate_image(self.imageInputPath, valueX, valueY)
            self.showToOutput("Translate Image")
    
    def flipVertical(self):
        self.outputFile = MenuGeometrik.flip_image(self.imageInputPath, 'vertical')
        self.showToOutput("Flip Vertical")

    def flipHorizontal(self):
        self.outputFile = MenuGeometrik.flip_image(self.imageInputPath, 'horizontal')
        self.showToOutput("Flip Horizontal")

    def show_dialog_rotate_image(self):
        self.pop_up = QtWidgets.QDialog()
        self.ui = Ui_RotateImage()
        self.ui.setupUi(self.pop_up)
        result = self.pop_up.exec_()

        if result == QtWidgets.QDialog.Accepted:
            value = self.ui.get_rotate()
            self.outputFile = MenuGeometrik.rotate_image(self.imageInputPath, value)
            print('output ' + self.outputFile)
            self.showToOutput("Rotate Image")

    def show_dialog_zoom_image(self):
        self.pop_up = QtWidgets.QDialog()
        self.ui = Ui_ZoomImage()
        self.ui.setupUi(self.pop_up)
        result = self.pop_up.exec_()

        if result == QtWidgets.QDialog.Accepted:
            value = self.ui.get_zoom_level()
            self.outputFile = MenuGeometrik.zoom_image(self.imageInputPath, value)
            print('output ' + self.outputFile)
            self.showToOutput("Zoom Image")

    def show_dialog_crop_image(self):
        # Create an instance of Ui_CropImage with the image path
        self.dialog = Ui_CropImage(self.imageInputPath)
        
        # Execute the dialog and get the result
        result = self.dialog.exec_()

        # Check if the dialog was accepted
        if result == QtWidgets.QDialog.Accepted:
            # Use the correct instance to get the bounding box coordinates
            posTop = self.dialog.get_pos_top()
            posBottom = self.dialog.get_pos_bottom()
            posRight = self.dialog.get_pos_right()
            posLeft = self.dialog.get_pos_left()
            
            # Crop the image using the coordinates
            self.outputFile = MenuGeometrik.crop_image(self.imageInputPath, posLeft, posTop, posRight, posBottom)
            # self.outputFile = rf".\output\output.png"

            # Show the cropped image or perform other actions
            self.showToOutput("Crop Image")

    # def region_growing(self):
    #     seed = (10, 10) 
    #     threshold_value = 20
    #     self.outputFile = MenuSegmentasi.region_growing(self.imageInputPath, seed, threshold_value)
    #     self.showToOutput("Region Growing")
    def region_growing(self):
        # Gunakan QDialog untuk dialog input
        RegionGrowingWindow = QtWidgets.QDialog()
        ui = Ui_RegionGrowing()
        ui.setupUi(RegionGrowingWindow)

        # Tampilkan dialog dan ambil hasilnya
        if RegionGrowingWindow.exec_() == QtWidgets.QDialog.Accepted:
            seed1 = ui.get_inpSeed1()
            seed2 = ui.get_inpSeed2()
            threshold_value = ui.get_inpThresold()

            seed = (seed1, seed2)
            self.outputFile = MenuSegmentasi.region_growing(self.imageInputPath, seed, threshold_value)
            self.showToOutput("Region Growing")
        
    # def kmeans_clustering(self):
    #     self.outputFile = MenuSegmentasi.kmeans_clustering(self.imageInputPath, 2)
    #     self.showToOutput("Kmeans Clustering")
    def kmeans_clustering(self):
        KmeansCLusDialog = QtWidgets.QDialog()
        ui = Ui_KmeansCLus()
        ui.setupUi(KmeansCLusDialog)

        if KmeansCLusDialog.exec_() == QtWidgets.QDialog.Accepted:
            k_value = ui.get_inpK()  # Ambil nilai K dari input pengguna

            self.outputFile = MenuSegmentasi.kmeans_clustering(self.imageInputPath, k_value)
            self.showToOutput("Kmeans Clustering")


    def watershed_segmentation(self):
        self.outputFile = MenuSegmentasi.watershed_segmentation(self.imageInputPath)
        self.showToOutput("Watershed Segmentation")

    # def global_thresholding(self):
    #     self.outputFile = MenuSegmentasi.global_thresholding(self.imageInputPath, 100)
    #     self.showToOutput("Golbal Thresholding")
    def global_thresholding(self):
        GlobalThresDialog = QtWidgets.QDialog()
        ui = Ui_GlobalThres()
        ui.setupUi(GlobalThresDialog)

        if GlobalThresDialog.exec_() == QtWidgets.QDialog.Accepted:
            threshold_value = ui.get_inpThres()  # Ambil nilai threshold dari input pengguna

            self.outputFile = MenuSegmentasi.global_thresholding(self.imageInputPath, threshold_value)
            self.showToOutput("Global Thresholding")


    def adaptive_thresh_mean(self):
        self.outputFile = MenuSegmentasi.adaptive_thresh_mean(self.imageInputPath)
        self.showToOutput("Adaptive Thresh Mean")

    def adaptive_thresh_gaussian(self):
        self.outputFile = MenuSegmentasi.adaptive_thresh_gaussian(self.imageInputPath)
        self.showToOutput("Adaptive Thresh Gaussian")

    def erotion33(self):
        self.outputFile = MenuMorfologi.erotion(self.imageInputPath, 1)
        self.showToOutput("Erotion Square 3")

    def erotion53(self):
        self.outputFile = MenuMorfologi.erotion(self.imageInputPath,2)
        self.showToOutput("Erotion Square 5")

    def erotion3(self):
        self.outputFile = MenuMorfologi.erotion(self.imageInputPath, 3)
        self.showToOutput("Erotion Cross 3")

    def dilate33(self):
        self.outputFile = MenuMorfologi.dilate(self.imageInputPath, 1)
        self.showToOutput("Dilate Square 3")

    def dilate53(self):
        self.outputFile = MenuMorfologi.dilate(self.imageInputPath,2)
        self.showToOutput("Dilate Square 5")

    def dilate3(self):
        self.outputFile = MenuMorfologi.dilate(self.imageInputPath, 3)
        self.showToOutput("Dilate Cross 3")

    def opening9(self):
        self.outputFile = MenuMorfologi.opening(self.imageInputPath, 4)
        self.showToOutput("Square 9")

    def closing9(self):
        self.outputFile = MenuMorfologi.closing(self.imageInputPath, 4)
        self.showToOutput("Square 9")
        
    def sobel(self):
        self.outputFile = MenuEdgeDetection.sobel(self.imageInputPath)
        self.showToOutput("Sobel")

    def prewit(self):
        self.outputFile = MenuEdgeDetection.prewit(self.imageInputPath)
        self.showToOutput("Prewit")

    def canny(self):
        self.outputFile = MenuEdgeDetection.canny(self.imageInputPath)
        self.showToOutput("Canny")
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
