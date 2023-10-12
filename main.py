import os


def file_name():
    file_path = input("What is your file path: ")
    print("Thank you, the path " + file_path + " was found properly")

    file_structure = {
        "name": "path_name",
        "number": "number_path",
    }


if __name__ == '__main__':
    file_name()
