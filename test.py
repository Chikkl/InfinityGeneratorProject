import os


def get_last_generated_file_from_dir():
        folder_path = "/home/chikoni/Документы/Python Projects/Задание с генераторами/red_army"  # Замените это на путь к вашей папке
        files = os.listdir(folder_path)
        print(files[-1])

get_last_generated_file_from_dir()
