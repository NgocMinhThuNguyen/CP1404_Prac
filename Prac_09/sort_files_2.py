import shutil
import os


def main():
    """Sort files program"""
    os.chdir("FilesToSort")
    file_extensions = []
    categories = []

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension_type = filename.split('.')[-1]
        if extension_type not in file_extensions:
            file_extensions.append(extension_type)
            category = input(f"What category would you like to sort {extension_type} files into? ")
            categories.append(category)
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

            shutil.move(filename, category)


main()