import csv
import Units
import os
import pandas as pd
from random import randint
from openpyxl import load_workbook
import yadisk
from dotenv import load_dotenv

class FileOSGenerator():
    def __init__(self, file_extension: str) -> None:
        self.generated_file_extensions = file_extension
        self.directory_name = "red_army" if self.generated_file_extensions == "xlsx" else "blue_army"
        
    
    
    def create_directory_for_history_battles(self) -> None:
        """Функция создания папки, хранящей историю отправляемых армий определенной стороны.
        Название папки определяется в зависимости от передаваемого ей значения расширений генерируемых данных."""
        root_path = os.getcwd()
        folder_path = os.path.join(root_path, self.directory_name)

        if not os.path.exists(folder_path):
            try:
                os.mkdir(folder_path)
                print(f'Папка "{self.directory_name}" успешно создана в корне проекта.')
            except Exception as e:
                print(f'Ошибка при создании папки: {e}')
        else:
            print(f'Папка "{self.directory_name}" уже существует в корне проекта.')
    
    def get_directory_path(self) -> str:
        root_path = os.getcwd()
        folder_path = os.path.join(root_path, self.directory_name)

        return folder_path


class DataGenerator():
    '''Класс отвечающий за генерацию данных о войсках армий'''
    def __init__(self, generated_file_extension: str) -> None:
        self.generated_file_extension = self.get_valid_extension(generated_file_extension)
        self.filename = "red_army" if self.generated_file_extension == "xlsx" else "blue_army"
        self.file_generator = FileOSGenerator(self.generated_file_extension)
        self.file_generator.create_directory_for_history_battles()
        if self.generated_file_extension == "xlsx":
             load_dotenv()
             self.yadisk = yadisk.YaDisk(token=os.getenv('token'))
        self.folder_path=self.file_generator.get_directory_path()
        
    
    def get_valid_extension(self, generated_file_extension: str) -> str:
        '''Функция для проверки корректности вводимого расширения'''
        while True:
            if generated_file_extension in ['csv', 'xlsx']:
                break
            else:
                print('Вы ввели некорректное расширение необходимого файла!')
                generated_file_extension = input('Введите "csv" или "xlsx": ')
        return generated_file_extension
    
    def generate_data_for_file(self) -> dict:
        '''Функция для генерации юнита'''
        return Units.UnitGenerator(randint(0, 100_000)).generate_unit_by_id()
    
    def create_excel_file(self) -> None:
        """Функция, создающая excel-файл для дальнейшего его наполнения данными"""
        data = {'id_unit': [], 'hp': [], 'mp': [], 'damage': [], 'defence': []}
        df = pd.DataFrame(data)
        file_name = self.get_unique_filename()
        df.to_excel(file_name, index=False)

    def get_unique_filename(self):
        '''Функция возвращающая уникальное название файла.
        Она проверяет, какие файлы у нас есть в директории, и если это имя свободно, то присваивает его файлу, иначе ищет свободное имя дальше.'''
        if self.generated_file_extension == "csv":
            folder_path=self.folder_path
            file_exists = True
            file_counter = 0

            while file_exists:
                new_filename = f'{self.filename}_{file_counter}.{self.generated_file_extension}' if file_counter > 0 else f'{self.filename}.{self.generated_file_extension}'
                full_path = os.path.join(folder_path, new_filename)
                file_exists = os.path.isfile(full_path)
                file_counter += 1
            return full_path
        elif self.generated_file_extension == "xlsx":
            file_exists = True
            file_counter = 0

            while file_exists:
                new_filename = f'{self.filename}_{file_counter}.{self.generated_file_extension}' if file_counter > 0 else f'{self.filename}.{self.generated_file_extension}'
                full_path = os.path.join("red_army", new_filename)
                file_exists = self.yadisk.exists(full_path)
                file_counter += 1
            return full_path

    def generate_file(self):
        '''Функция, генерирует данные в необходимом и определённом формате, 
            в зависимости от переданного в объект файла расширения.'''
        path_with_file_name = self.get_unique_filename()
        if self.generated_file_extension == 'csv':
            with open(path_with_file_name, 'w') as file:
                writer = csv.writer(file)
                for _ in range(randint(1, 1000)):
                    writer.writerow(self.generate_data_for_file().character_stats)

        elif self.generated_file_extension == 'xlsx':
            data = [[*self.generate_data_for_file().character_stats] for _ in range(randint(1, 100))]

            self.create_excel_file()
            
            wb = load_workbook(path_with_file_name)
            sheet = wb.active
            for row_data in data:
                sheet.append(row_data)
            wb.save(path_with_file_name)
            wb.close()
            return path_with_file_name

