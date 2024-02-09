import os
import yadisk
from dotenv import load_dotenv
import re


class Analitics():
    def __init__(self) -> None:
        self.red_army_filename = ""
        self.blue_army_filename = ""
        self.yandex_disk_folder = '/red_army'
        self.local_folder =  os.getcwd()
        load_dotenv()
        self.disk = yadisk.YaDisk(token=os.getenv('token'))
        
    def get_file_with_data(self):
        # Получаем список файлов в папке на Яндекс.Диске
        yandex_files = self.disk.listdir(self.yandex_disk_folder)

        # Скачиваем и удаляем файлы
        for yandex_file in yandex_files:
            yandex_file = yandex_file["name"]
            yandex_file_path = f'{self.yandex_disk_folder}/{yandex_file}'
            local_file_path = os.path.join(self.local_folder, yandex_file)

            # Скачиваем файл
            self.disk.download(yandex_file_path, local_file_path)
            print(f'File downloaded from {yandex_file_path} to {local_file_path}')

            # Удаляем файл на Яндекс.Диске
            self.disk.remove(yandex_file_path)
            print(f'File {yandex_file_path} deleted on Yandex.Disk')

    def extract_numerical_suffix(self, file_name):
        """
        Извлекает числовой суффикс из имени файла.
        """
        match = re.search(r'_(\d+)$', file_name)
        if match:
            return int(match.group(1))
        return None

    def compare_file_names(self, file1, file2):
        """
        Сравнивает имена файлов с учетом числового суффикса.
        """
        num1 = self.extract_numerical_suffix(file1)
        num2 = self.extract_numerical_suffix(file2)

        if num1 is not None and num2 is not None:
            return num1 - num2
        else:
            return 0  # Если числового суффикса нет, считаем файлы одинаковыми

anal = Analitics()
anal.get_file_with_data()
