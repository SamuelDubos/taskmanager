import customtkinter
import os
from variables import *
import json

from frame import ConstantFrame, TemporaryFrame, EntryFrame
from log_frame import LogFrame


class TaskManager(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.geometry('880x420')
        self.add_title()
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)
        self.grid_columnconfigure(2, weight=2)
        self.grid_rowconfigure(1, weight=1)

        self.set_path()

        self.log_frame = LogFrame(self)
        self.log_frame.grid(row=0, column=1, padx=(0, 0), pady=(10, 0), sticky='nsew', rowspan=2)

        self.constant, self.temporary = self.get_tasks()
        self.display_buttons()
        self.display_tasks()
        self.bind_keys()

    @staticmethod
    def set_path():
        for path in [LOG_PATH, TASKS_PATH]:
            if not os.path.exists(path):
                with open(path, 'w') as _:
                    pass

    def add_title(self):  # TODO: Remove?
        self.title('TaskManager')
        # logo_label = customtkinter.CTkLabel(self, text='Task Manager',
        #                                     font=customtkinter.CTkFont(size=24, weight='bold'))
        # logo_label.grid(row=0, column=1, padx=0, pady=(30, 10))

    def bind_keys(self):
        self.bind('<Alt-u>', lambda event: self.update())  # TODO: Auto-update?
        self.bind('<Escape>', lambda event: self.exit())

    @staticmethod
    def get_tasks():
        with open(TASKS_PATH, 'r') as file:
            data = json.load(file)
        constant = [[task, spec['key']] for task, spec in data['constant'].items()]
        temporary = [task for task, spec in data['temporary'].items() if spec['active']]
        return constant, temporary

    def display_tasks(self):
        ConstantFrame(master=self, tasks=self.constant)
        TemporaryFrame(master=self, names=self.temporary)
        EntryFrame(master=self)

    def update(self):
        self.log_frame.display_log()
        self.constant, self.temporary = self.get_tasks()
        self.display_tasks()

    def display_buttons(self):
        exit_button = customtkinter.CTkButton(self, text='Exit (Esc)', command=self.exit, fg_color='firebrick')
        exit_button.grid(row=3, column=2, padx=(10, 10), pady=(10, 10), sticky='news')
        update_button = customtkinter.CTkButton(self, text='Update (Alt+U)',
                                                command=self.update, fg_color='olivedrab')
        update_button.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky='news')

    @staticmethod
    def exit():
        print('Exiting Program')
        exit()


if __name__ == '__main__':
    TaskManager().mainloop()
