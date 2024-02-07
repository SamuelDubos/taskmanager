import customtkinter
import datetime
import os


class Task:

    def __init__(self, master, frame, name, row, column, key=None, pady=10):
        self.master = master
        self.frame = frame
        self.name = name
        self.row = row
        self.column = column
        self.key = key
        self.pady = pady

        self.log = os.path.join('..', 'data', 'log')
        self.add_button()

    def add_button(self):
        button = customtkinter.CTkButton(master=self.frame, text=self.name, command=self.action)
        button.grid(row=self.row, column=self.column, padx=10, pady=self.pady, sticky='news')
        if self.key is not None:
            self.master.bind(sequence=self.key, func=lambda event: self.action())

    def action(self):
        text = f'{datetime.datetime.now()} | {self.name}'
        print(text)
        with open(self.log, 'a') as log:
            log.write(text + '\n')
