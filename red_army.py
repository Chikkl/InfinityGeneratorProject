import Generator
import DataSender
import time


dg = Generator.DataGenerator("xlsx")
data_sender = DataSender.DataSender(dg.generated_file_extension)
while True:
    path_to_last_file = dg.generate_file()
    data_sender.send_data(path_to_last_file)
    time.sleep(60)

