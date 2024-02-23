import customtkinter
import datetime
import json
from .loader import *


class Task:

    def __init__(self, master, frame, name, row, column, key=None, pady=10):
        self.master = master
        self.frame = frame
        self.name = name
        self.row = row
        self.column = column
        self.key = key
        self.pady = pady

        self.add_button()

    def add_button(self):
        label = self.name
        if self.key is not None:
            self.master.bind(sequence=f'<Control-{self.key}>', func=lambda event: self.action())
            label = f'{self.name} ({self.key.upper()})'
        button = customtkinter.CTkButton(master=self.frame, text=label, command=self.action)
        button.grid(row=self.row, column=self.column, padx=10, pady=self.pady, sticky='news')

    def action(self):
        text = f'{datetime.datetime.now()} | {self.name}'
        print(text)
        with open(LOG_PATH, 'a', encoding='utf-8') as log:
            log.write(text + '\n')
        self.master.update_frames()

    def deactivate(self):
        with open(TASKS_PATH, 'r+') as file:
            data = json.load(file)
            data['temporary'][self.name]['active'] = False
            file.seek(0)
            json.dump(data, file, indent=4)
        self.master.update_frames()

