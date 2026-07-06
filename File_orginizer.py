import os
import shutil

FOLDER_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".json"],
}


def get_category(extension):
    for category, extensions in FOLDER_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Other"


def organize_folder(target_folder):
    if not os.path.exists(target_folder):
        print(f"Folder not found: {target_folder}")
        return

    files_moved = 0

    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)

        if os.path.isdir(file_path):
            continue

        _, extension = os.path.splitext(filename)
        if extension == "":
            continue

        category = get_category(extension)
        category_folder = os.path.join(target_folder, category)

        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        destination = os.path.join(category_folder, filename)

        if not os.path.exists(destination):
            shutil.move(file_path, destination)
            print(f"Moved: {filename} -> {category}/")
            files_moved += 1

    print(f"\nDone. {files_moved} file(s) organized.")


if __name__ == "__main__":
    folder_to_organize = input("Enter the folder path to organize: ")
    organize_folder(folder_to_organize)