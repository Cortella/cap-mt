import cv2
import numpy as np


class Image:
    def __init__(self, image_path):
        self.image_path = image_path

        try:
            image = cv2.imread(self.image_path)

            if image is None:
                raise ValueError(
                    "Não foi possível carregar a imagem. Verifique o caminho do arquivo.")

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            _, black_mask = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)

            self.total_pixels = gray.size
            self.black_pixels = np.count_nonzero(black_mask)
            self.black_percentage = (
                self.black_pixels / self.total_pixels) * 100

        except Exception as e:
            print(f"Erro ao processar a imagem: {e}")
            self.total_pixels = 0
            self.black_pixels = 0
            self.black_percentage = 0

    def is_captcha_image(self):
        return self.black_percentage > 50

    def get_image_proprieties_info(self):
        print("Propriedades da imagem:" + "\n" +
              "Caminho da imagem: " + self.image_path + "\n" +
              "Total de pixels: " + str(self.total_pixels) + "\n" +
              "Pixels pretos: " + str(self.black_pixels) + "\n" +
              "Porcentagem de preto: " + str(self.black_percentage) + "%"
              )
