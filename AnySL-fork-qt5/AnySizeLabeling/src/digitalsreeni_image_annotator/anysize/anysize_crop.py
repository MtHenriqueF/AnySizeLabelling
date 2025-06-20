from pylibCZIrw import czi as pyczi
import numpy as np

class ImageCropper():
    """Classe responsável por fazer o 'crop' na imagem"""
    def __init__(self,image=None):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.slice = 0
        self.channel = 0
        self.time = 0
        self.image = image

    def cropImage(self):
        """
        Abre uma imagem czi e realiza um corte.

        :param image: Caminho da imagem a ser cortada ou Numpy array contendo uma subimagem
        :type image: str/ndarray

        :returns: Numpy array contendo as informações da imagem
        :rtype: ndarray
        """
        if(isinstance(self.image,str)):
            custom_plane = {'C': self.channel, 'Z': self.slice, 'T': self.time}
            # Necessário definir depois qual a resolução standard que vamos ler. 
            crop = (self.x,self.y,self.w,self.h)
            with pyczi.open_czi(self.image) as czi:           
                image_as_numpy = czi.read(roi = crop, plane = custom_plane)
            return image_as_numpy
        elif(isinstance(self.image,np.ndarray)):
            starty = self.y
            endy = self.y + self.h
            startx = self.x
            endx = self.x + self.w
            new_image = self.image[starty:endy,startx:endx]
            return new_image

    def setCrop(self,x,y,w,h,slice=0,channel=0,time=0):
        """
        Define o formato do corte na imagem

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
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.slice = slice
        self.channel = channel
        self.time = time

    def setImage(self,image):
        self.image = image
    
    def getImageDimensions(self):
        with pyczi.open_czi(self.image) as czi:
            dimensions = czi.total_bounding_box
        print(dimensions)
        return dimensions
    
    def getTopLeft(self):
        """
        Retorna o top-left da imagem
        
        :returns: Top-left da imagem
        :rtype: int
        """
        return self.x,self.y

    
         


