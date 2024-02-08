import os


class Loader:

    def __init__(self):
        self.log_path = os.path.join('data', 'log')
        self.tasks_path = os.path.join('data', 'tasks.json')


loader = Loader()
LOG_PATH = loader.log_path
TASKS_PATH = loader.tasks_path
FONT1 = ('TkDefaultFont', 13, 'normal')
FONT2 = ('Helvetica', 14, 'bold')

__all__ = ['LOG_PATH', 'TASKS_PATH', 'FONT1', 'FONT2']
