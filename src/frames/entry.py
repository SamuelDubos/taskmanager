import customtkinter
import json

from ..loader import *


class EntryFrame(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid(row=3, column=1, padx=(0, 0), pady=(10, 10), sticky='news')
        self.entry = customtkinter.CTkEntry(self, placeholder_text='Type a new task')
        self.entry.grid(row=0, column=0, padx=(10, 0), pady=(10, 10), sticky='nsew', columnspan=2)
        add_button = customtkinter.CTkButton(self, text='Add', command=self.add_task, fg_color='darkslategrey')
        add_button.grid(row=0, column=2, padx=10, pady=10)

    def add_task(self):
        if self.entry.get() != '':
            with open(TASKS_PATH, 'r+') as file:
                data = json.load(file)
                data['temporary'][self.entry.get()] = {'active': True}
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
        self.master.update_frames()
