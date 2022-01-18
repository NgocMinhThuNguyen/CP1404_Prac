import shutil
import os


def main():
    """Sort files program"""
    os.chdir("FilesToSort")
    file_extensions = []

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension_type = filename.split('.')[-1]
        if extension_type not in file_extensions:
            file_extensions.append(extension_type)

        try:
            os.mkdir(extension_type)
        except FileExistsError:
            pass

        shutil.move(filename, extension_type)


main()