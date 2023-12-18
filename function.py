import os # библиотека работы с файловой системой
import shutil # библиотека копирования файлов

# функция создания новой папки
def create_new_dir(path):
    if os.path.isdir(path) == False: # если папка не существует, то создаем её
        os.mkdir(path) # создание новой папки
        print("Создана новая папка " + path)
    else:
        print("Папка " + path + " уже существует")

# функция переноса фалов в новую папку по названию файла до точки и изменении имени файла
def move_file(parent_dir, new_dir, file):
    if os.path.isfile(parent_dir + "/" + file): # проверка что это файл
        if os.path.isdir(new_dir): # проверка что это новая папка существует

            # новое имя файла - название после точки Гоголь.Мертвые души.txt -> Мертвые души.txt
            # +1 что бы убрать точку
            new_name_file = file[file.find('.')+1:]
            shutil.move(parent_dir + "/" + file,    # копирование откуда
                        new_dir + "/" + new_name_file)          # копирование куда
            print("Файл " + file + " перенесен в папку " + new_dir + " под новым названием " + new_name_file)
        else:
            print("Файл " + file + " не перенесен, т.к папка " + new_dir + " не существует!")
