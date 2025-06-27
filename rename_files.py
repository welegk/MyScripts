import os
import sys

def remove_substring_in_names(target_substring, path='.'):
    for root, dirs, files in os.walk(path, topdown=False):
        # Переименование файлов
        for name in files:
            if target_substring in name:
                old_path = os.path.join(root, name)
                new_name = name.replace(target_substring, "")
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed file: {old_path} -> {new_path}")

        # Переименование директорий
        for name in dirs:
            if target_substring in name:
                old_path = os.path.join(root, name)
                new_name = name.replace(target_substring, "")
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed directory: {old_path} -> {new_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("❗ Использование:")
        print("   python3 rename_script.py /путь/к/папке строка_для_удаления")
        sys.exit(1)

    path = sys.argv[1]
    substring_to_remove = sys.argv[2]

    if not os.path.isdir(path):
        print(f"❌ Указанный путь не существует или не является директорией: {path}")
        sys.exit(1)

    remove_substring_in_names(substring_to_remove, path)

