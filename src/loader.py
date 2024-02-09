import os


class Loader:

    def __init__(self, folder):
        self.log_path = os.path.join(folder, 'log')
        self.tasks_path = os.path.join(folder, 'tasks.json')
        self.data_path = os.path.join(folder)


loader = Loader('data')
LOG_PATH = loader.log_path
TASKS_PATH = loader.tasks_path
DATA_PATH = loader.data_path

__all__ = ['LOG_PATH', 'TASKS_PATH', 'DATA_PATH']
