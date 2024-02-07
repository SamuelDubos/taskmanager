from variables import *
import json


def add_constant(name, key=None):
    key = key or name[0].lower()
    with open(TASKS_PATH, 'r+') as file:
        data = json.load(file)
        data['constant'][name] = {'key': key}
        file.seek(0)
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    add_constant('Kitchen', 'k')
