import os


class Loader:

    def __init__(self):
        self.log_path = os.path.join('data', 'log')
        self.tasks_path = os.path.join('data', 'tasks.json')
        self.data_path = os.path.join('data')


loader = Loader()
LOG_PATH = loader.log_path
TASKS_PATH = loader.tasks_path
DATA_PATH = loader.data_path

__all__ = ['LOG_PATH', 'TASKS_PATH', 'DATA_PATH']
