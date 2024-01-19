import os
import shutil

def clean_temp_files():
    # Очистка временных файлов
    temp_folder = os.path.join(os.environ["TEMP"])
    for root, dirs, files in os.walk(temp_folder):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"Ошибка при удалении файла {file_path}: {e}")

def clean_cache():
    # Очистка кеша
    local_app_data = os.environ["LOCALAPPDATA"]
    cache_folder = os.path.join(local_app_data, "Microsoft", "Windows", "INetCache")
    try:
        shutil.rmtree(cache_folder)
    except Exception as e:
        print(f"Ошибка при удалении кеша: {e}")

if __name__ == "__main__":
    clean_temp_files()
    clean_cache()
    print("Очистка завершена!")
