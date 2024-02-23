import customtkinter
import json
import os

from src.frames.constant import ConstantFrame
from src.frames.temporary import TemporaryFrame
from src.frames.entry import EntryFrame
from src.frames.log import LogFrame
from src.loader import *
from analysis import Analyzer


class TaskManager(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.geometry('880x450')
        self.title('TaskManager')

        self.set_data()
        self.log_frame = None
        self.entry_frame = None
        self.set_configuration()
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
        if not os.path.exists(DATA_PATH):
            os.mkdir(DATA_PATH)
        if not os.path.exists(LOG_PATH):
            with open(LOG_PATH, 'w') as _:
                pass
        if not os.path.exists(TASKS_PATH):
            with open(TASKS_PATH, 'w') as file:
                data = {"temporary": {"TemporaryTask": {"active": True}},
                        "constant": {"Night": {"key": "n"},
                                     "Break": {"key": "b"},
                                     "Work": {"key": "w"},
                                     "Meal": {"key": "m"}}}
                json.dump(data, file, indent=4)

    def bind_keys(self):
        self.bind('<Alt-a>', lambda event: self.analyze())
        self.bind('<Escape>', lambda event: self.exit())
        self.bind('<Return>', lambda event: self.entry_frame.add_task())

    @staticmethod
    def get_tasks():
        with open(TASKS_PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)
        constant = [[task, spec['key']] for task, spec in data['constant'].items()]
        temporary = [task for task, spec in data['temporary'].items() if spec['active']]
        return constant, temporary

    def add_frames(self):
        ConstantFrame(master=self, tasks=self.constant)
        TemporaryFrame(master=self, names=self.temporary)
        self.entry_frame = EntryFrame(master=self)
        self.log_frame = LogFrame(self)

    def update_frames(self):
        self.constant, self.temporary = self.get_tasks()
        ConstantFrame(master=self, tasks=self.constant)
        TemporaryFrame(master=self, names=self.temporary)
        self.entry_frame = EntryFrame(master=self)
        self.log_frame.display_log()

    def display_buttons(self):
        exit_button = customtkinter.CTkButton(self, text='Exit (Esc)', command=self.exit, fg_color='firebrick')
        exit_button.grid(row=3, column=2, padx=(10, 10), pady=(10, 10), sticky='news')
        analyze_button = customtkinter.CTkButton(self, text='Analyze (Alt+A)',
                                                 command=self.analyze, fg_color='olivedrab')
        analyze_button.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky='news')

    @staticmethod
    def exit():
        print('Exiting Program...')
        exit()

    def analyze(self):
        period = self.log_frame.variable.get()
        Analyzer(period)


if __name__ == '__main__':
    TaskManager().mainloop()
