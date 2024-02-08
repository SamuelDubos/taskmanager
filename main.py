import customtkinter
import json
import os

from src.frames.constant import ConstantFrame
from src.frames.temporary import TemporaryFrame
from src.frames.entry import EntryFrame
from src.frames.log import LogFrame
from src.loader import *


class TaskManager(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.geometry('880x420')
        self.title('TaskManager')

        self.log_frame = None
        self.set_configuration()
        self.set_data()
        self.constant, self.temporary = self.get_tasks()
        self.display_buttons()
        self.add_frames()
        self.bind_keys()

    def set_configuration(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)
        self.grid_columnconfigure(2, weight=2)
        self.grid_rowconfigure(1, weight=1)

    @staticmethod
    def set_data():
        for path in [TASKS_PATH, LOG_PATH]:
            if not os.path.exists(path):
                with open(path, 'w') as _:
                    pass

    def bind_keys(self):
        self.bind('<Alt-u>', lambda event: self.update())
        self.bind('<Escape>', lambda event: self.exit())

    @staticmethod
    def get_tasks():
        with open(TASKS_PATH, 'r') as file:
            data = json.load(file)
        constant = [[task, spec['key']] for task, spec in data['constant'].items()]
        temporary = [task for task, spec in data['temporary'].items() if spec['active']]
        return constant, temporary

    def add_frames(self):
        ConstantFrame(master=self, tasks=self.constant)
        TemporaryFrame(master=self, names=self.temporary)
        EntryFrame(master=self)
        self.log_frame = LogFrame(self)

    def update(self):
        self.constant, self.temporary = self.get_tasks()
        ConstantFrame(master=self, tasks=self.constant)
        TemporaryFrame(master=self, names=self.temporary)
        self.log_frame.display_log()

    def display_buttons(self):
        exit_button = customtkinter.CTkButton(self, text='Exit (Esc)', command=self.exit, fg_color='firebrick')
        exit_button.grid(row=3, column=2, padx=(10, 10), pady=(10, 10), sticky='news')
        update_button = customtkinter.CTkButton(self, text='Update (Alt+U)',
                                                command=self.update, fg_color='olivedrab')
        update_button.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky='news')

    @staticmethod
    def exit():
        print('Exiting Program...')
        exit()


if __name__ == '__main__':
    TaskManager().mainloop()
