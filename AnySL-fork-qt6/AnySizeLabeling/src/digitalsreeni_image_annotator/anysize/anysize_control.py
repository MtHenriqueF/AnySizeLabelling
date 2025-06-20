from pylibCZIrw import czi as pyczi #Provavelmente vai sair dessa classe
from .anysize_crop import ImageCropper
import numpy as np

class ImageController():

    """Classe de controle que encapsula anysize_crop e administra a imagem principal e a subimagem"""
    def __init__(self,image_path):
        """
        :param image_path: Caminho da imagem a ser aberta
        :type image_path: str
        """
        self.original_name = image_path
        self.original_cropped = None
        self.original_cropper = ImageCropper(image_path)
        self.sub_cropped = None
        self.sub_cropper = ImageCropper()

    def setOriginalImageCrop(self,x=0,y=0,w=1920,h=1080,slice=0,channel=0,time=0):
        """
        Define o formato do corte da imagem original. A definição default é 1920 x 1080

        :param x: Coordenada X do top-left do corte
        :type x: int 
        :param y: Coordenada Y do top-left do corte
        :type y: int         
        :param w: Largura do corte
        :type w: int
        :param h: Altura do corte
        :type h: int
        :param slice: Camada da imagem.
        :type slice: int
        :param channel: Canal da imagem.
        :type channel: int
        :param time: Tempo da imagem.
        :type time: int
        """
        self.original_cropper.setCrop(x,y,w,h,slice,channel,time)

    def cropOriginalImage(self):
        """
        Realiza um corte na imagem original
        """
        return self.original_cropper.cropImage()

    def setSubImageCrop(self,x=0,y=0,w=1366,h=763):
        """
        Define o formato do corte da subimagem. A definição default é 1366 x 763

        :param x: Coordenada X do top-left do corte
        :type x: int 
        :param y: Coordenada Y do top-left do corte
        :type y: int         
        :param w: Largura do corte
        :type w: int
        :param h: Altura do corte
        :type h: int
        """
        self.sub_cropper.setCrop(x,y,w,h)
    
    def cropSubImage(self):
        """
        Realiza um corte na subimagem
        """
        self.sub_cropper.setImage(self.original_cropped)
        self.sub_cropped = self.sub_cropper.cropImage()

    def crop(self, x=0, y=0, w=1920, h=1080):
        # Pega dimensões
        dimensions = self.original_cropper.getImageDimensions()
        img_T = dimensions.get('T', (0, 1))[1]
        img_C = dimensions.get('C', (0, 1))[1]
        img_Z = dimensions.get('Z', (0, 1))[1]

        # Faz uma leitura inicial para descobrir forma da imagem cropada
        self.setOriginalImageCrop(x, y, w, h, 0, 0, 0)
        sample = self.cropOriginalImage()
        img_shape = sample.shape  # geralmente (H, W) ou (H, W, C)

        # Aloca array final: shape = (T, C, Z, H, W)
        stacked_image = np.zeros((img_T, img_C, img_Z, *img_shape), dtype=sample.dtype)

        for t in range(img_T):
            for c in range(img_C):
                for z in range(img_Z):
                    self.setOriginalImageCrop(x, y, w, h, z, c, t)
                    cropped = self.cropOriginalImage()
                    stacked_image[t, c, z] = cropped

        print(stacked_image.shape)
        self.original_cropped = stacked_image


    def getImageSize(self):
        dimensions = self.original_cropper.getImageDimensions()
        sizes = {"X":dimensions['X'][1],"Y":dimensions['Y'][1]}
        return sizes     

    def getOriginalCropped(self):
        return self.original_cropped

    def getSubCropped(self):
        return self.sub_cropped
    
    def getOriginalTopLeft(self):
        return self.original_cropper.getTopLeft()
    
    def getSubTopLeft(self):
        return self.sub_cropper.getTopLeft()
    
    def getFilePath(self):
        return self.original_name