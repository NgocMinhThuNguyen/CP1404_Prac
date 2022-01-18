import os


def main():
    """Clean up program"""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            old_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(old_name, new_name)
            print(new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ""
    old_name = (filename.replace('.TXT', '.txt').replace('.txt', ''))

    for i, letter in enumerate(old_name):
        if letter.isspace():
            letter = "_"
        elif letter.isalpha():
            try:
                previous_char = old_name[i - 1]
                next_letter = old_name[i + 1]
                if next_letter.isupper() or next_letter == "(":
                    letter += "_"
                elif previous_char == "_":
                    letter = letter.upper()
            except IndexError:
                pass

        new_name += letter
    new_name += '.txt'
    return new_name


main()
