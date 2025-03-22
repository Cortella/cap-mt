import os


class Directory:
    def __init__(self, directory_path):
        self.directory_path = directory_path

        try:
            self.files = os.listdir(self.directory_path)

            if self.files is None:
                raise ValueError(
                    "Nao foi possivel carregar o diretorio. Verifique o caminho do diretorio.")

        except Exception as e:
            print(f"Erro ao processar o diretorio: {e}")
            self.directory_path = None
            self.files = None

        else:
            self.files = self.files

        finally:
            pass

    def get_directory_proprieties_info(self):
        print("Propriedades do diretorio:" + "\n" +
              "Caminho do diretorio: " + self.directory_path + "\n" +
              "Total de arquivos: " + str(self.files) + "\n"
              )

    def remove_all_files(self):
        if os.path.exists(self.directory_path) and os.path.isdir(self.directory_path):
            for arquivo in os.listdir(self.directory_path):
                caminho_arquivo = os.path.join(self.directory_path, arquivo)
                if os.path.isfile(caminho_arquivo):
                    os.remove(caminho_arquivo)
                    print(f"Removido: {caminho_arquivo}")
        else:
            print("O diretório não existe.")

    def get_last_print(self):
        return self.files[len(self.files) - 1]
