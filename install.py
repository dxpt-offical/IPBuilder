import subprocess
import sys
import os

def install_and_run(filename):
    print("🔄 Установка зависимостей...")
    subprocess.run([sys.executable, "-m", "pip", "install", "colorama", "termcolor", "PyInstaller"], check=True)
    
    print(f"🚀 Запуск {filename}...")
    if os.path.exists(filename):
        subprocess.run([sys.executable, filename])
    else:
        print(f"❌ Ошибка: Файл {filename} не найден.")
