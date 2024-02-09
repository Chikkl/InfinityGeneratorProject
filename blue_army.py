import Generator
import time


dg = Generator.DataGenerator("csv")
while True:
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"Formatted time: {formatted_time}")
    dg.generate_file()
    time.sleep(30)
