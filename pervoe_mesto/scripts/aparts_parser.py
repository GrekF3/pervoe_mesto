import os
import re
from pervoe_api.models import Apartment
def create_apartments():
    # Путь к папке, в которой хранятся изображения квартир разных типов
    aparts_path_types = 'pervoe_mesto/static/images/apparts'
    # Обход папок с разными типами квартир
    for room_type_folder in os.listdir(aparts_path_types):
        room_type_path = os.path.join(aparts_path_types, room_type_folder)

        # Извлекаем room_type из имени папки
        room_type = room_type_folder.split('_')[0]
        # Обход файлов внутри каждой папки
        for file in os.listdir(room_type_path):
            file_path = os.path.join(room_type_path, file)
            # Извлекаем информацию из имени файла с использованием регулярного выражения
            match = re.match(r'.*st-(\d+\.\d+)_\d+x\d+_c90\.jpeg', file)
            # if match:
            #     # Извлекаем размер квартиры из регулярного выражения
            #     area = float(match.group(1))
            #     print(area)
            #     # Проверяем, существует ли квартира с такими параметрами
            #     if not Apartment.objects.filter(room_type=room_type, area=area).exists():
            #         # Создаем новую квартиру
            #         apartment = Apartment.objects.create(
            #             room_type=room_type,
            #             area=area,
            #             image=file_path
            #         )
            #         print(f"Created apartment: {apartment}")
if __name__ == "__main__":
    create_apartments()