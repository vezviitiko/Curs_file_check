import os   # библиотека работы с файловой системой
from function import * # наша библиотека с функциями

if __name__ == '__main__':
    parent_dir = os.getcwd() + "./Author"  # полный путь до рабочей папки. os.getcwd() - текущая директория файла main.py
    content = os.listdir('./Author') # список файлов в первоначальной папке

    for file in content: # проходим первоначального массива - выбираем названия для создания папок
        if os.path.isfile(parent_dir + "/" + file): # проверка что это файл

            # название новой папки - название до точки в первоначальном списке
            name_new_folder = file[0: file.find('.')]
            # полный путь до новой папки
            new_dir = parent_dir + "/" + name_new_folder

            # создаем новую папку
            create_new_dir(new_dir) # путь до новой папки

            # копирование файла в новую папку из текущей
            move_file(parent_dir, new_dir, file) # путь до текущей папки, путь до новой папки, название файла
