import os

import systemOperations


def main_script():
    os.times()
    drives = os.listdir("C:\\Users\\MrArtificial\\PycharmProjects")
    print(drives)
    systemOperations.name = "computer"


def file_name():

    file_path = input("What is your file path: ")
    print("Thank you, the path " + file_path + " was found properly")

    file_structure = {
        "name": "path_name",
        "number": "number_path",
    }

    folder_files = ["abd", "abc", "abe"]
    folder_files.insert(0, "aba")
    path_attributes = file_structure.pop("name")


if __name__ == '__main__':
    file_name()
    main_script()
