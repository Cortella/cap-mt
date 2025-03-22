import cv2
import numpy as np


class Image:
    def __init__(self, image_path):
        self.image_path = image_path
        image = cv2.imread(self.image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, black_mask = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)

        self.total_pixels = gray.size
        self.black_pixels = np.count_nonzero(black_mask)

        self.black_percentage = (self.black_pixels / self.total_pixels) * 100

    def get_image_proprieties_info(self):
        print("Propriedades da imagem:" + "\n" +
              "Caminho da imagem: " + self.image_path + "\n" +
              "Total de pixels: " + str(self.total_pixels) + "\n" +
              "Pixels pretos: " + str(self.black_pixels) + "\n"
              "Porcentagem de preto: " + str(self.black_percentage)
              )
