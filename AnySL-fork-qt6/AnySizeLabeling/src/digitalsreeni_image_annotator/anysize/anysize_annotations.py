import numpy as np

from PySide6.QtWidgets import QLabel
class AnnotationUtils(QLabel):

    """Classe utilitária para manipulação de anotações de segmentação em imagens"""

    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window
    
    def convertAnnotations(self,annotation,top_x,top_y):
        arr = np.array(annotation)
        dx = top_x
        dy = top_y
        offset = np.tile([dx, dy], len(arr) // 2)
        converted_annotation = arr + offset
        return converted_annotation.tolist()
    
    def IsAnnotationWithinCrop(self,annotation, crop_x, crop_y, crop_w, crop_h):
        """
        Verifica se todos os pontos da segmentação estão dentro do crop.

        :param annotation: dict com chave 'segmentation' contendo lista linear [x0, y0, x1, y1, ...]
        :param crop_x: coordenada x do canto superior esquerdo do crop
        :param crop_y: coordenada y do canto superior esquerdo do crop
        :param crop_w: largura do crop
        :param crop_h: altura do crop
        :return: True se todos os pontos estão dentro do crop, False caso contrário
        """

        segmentation = annotation.get('segmentation', [])

        if not segmentation or len(segmentation) % 2 != 0:
            return False  # inválido
        
        max_x = crop_x + crop_w
        max_y = crop_y + crop_h

        # Itera sobre pares (x, y)
        for i in range(0, len(segmentation), 2):
            x, y = segmentation[i], segmentation[i + 1]
            if not (crop_x <= x < max_x and crop_y <= y < max_y):
                return False  # ponto fora do crop
        return True  # todos os pontos dentro do crop