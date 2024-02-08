import os
import yadisk
from dotenv import load_dotenv



class DataSender():
    def __init__(self, file_extension:str) -> None:
        self.file_extension = file_extension
        if self.file_extension == "xlsx":
             load_dotenv()
             self.yadisk = yadisk.YaDisk(token=os.getenv('token'))
    
    def get_last_generated_filename_from_dir(self, folder_path):
        file_name = folder_path.split("/")[-1]
        print(file_name)
        return file_name

    def send_data(self, folder_path_on_pc:str = None) -> None:
        """Функция отвечающая за отправку файла"""
        if self.yadisk.check_token():
            if not self.yadisk.is_dir('/red_army'):
                self.yadisk.mkdir('/red_army')
            self.yadisk.upload(folder_path_on_pc, f'/red_army/{self.get_last_generated_filename_from_dir(folder_path_on_pc)}')
        else:
            raise ValueError("Ваш токен не подходит, к яндекс диску, пожалуйста узнайте свой токен и введите его снова.")
