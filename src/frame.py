import customtkinter
import json
from variables import *
from task import Task


class ConstantFrame(customtkinter.CTkFrame):

    def __init__(self, master, tasks, title='Constant Tasks', row=0, column=2):
        super().__init__(master)
        self.title = title
        self.tasks = tasks

        self.grid_columnconfigure(0, weight=1)
        self.set_title()
        self.add_tasks()
        self.grid(row=row, column=column, padx=10, pady=(10, 0), sticky='news', rowspan=3)

    def set_title(self):
        title = customtkinter.CTkLabel(self, text=self.title, fg_color='gray', corner_radius=6)
        title.grid(row=0, column=0, padx=10, pady=(10, 10), sticky='news')

    def add_tasks(self):
        for i, (name, key) in enumerate(self.tasks, start=1):
            Task(master=self.master, frame=self, name=name, row=i, column=0, key=key, pady=10)


class TemporaryFrame(customtkinter.CTkScrollableFrame):

    def __init__(self, master, names, title='Temporary Tasks', row=0, column=0):
        self.master = master
        self.names = names
        self.title = title

        super().__init__(self.master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.set_title()
        self.add_tasks()
        self.grid(row=row, column=column, padx=10, pady=(10, 0), sticky='news', rowspan=3)

    def set_title(self):
        title = customtkinter.CTkLabel(self, text=self.title, fg_color='gray', corner_radius=6)
        title.grid(row=0, column=0, padx=10, pady=(10, 10), sticky='news', columnspan=2)

    def add_tasks(self):
        for i, name in enumerate(self.names, start=1):
            task = Task(self.master, self, name, i, 0, pady=5)
            button = customtkinter.CTkButton(master=self, text='Done', width=65, command=task.deactivate)
            button.grid(row=i, column=1, padx=(0, 10), pady=5)


class EntryFrame(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid(row=3, column=1, padx=(0, 0), pady=(10, 10), sticky='news')
        self.entry = customtkinter.CTkEntry(self, placeholder_text='Type a new task')
        self.entry.grid(row=0, column=0, padx=(10, 0), pady=(10, 10), sticky='nsew', columnspan=2)
        add_button = customtkinter.CTkButton(self, text='Add', command=self.add_task, fg_color='darkslategrey')
        add_button.grid(row=0, column=2, padx=10, pady=10)

    def add_task(self):
        with open(TASKS_PATH, 'r+') as file:
            data = json.load(file)
            data['temporary'][self.entry.get()] = {'active': True}
            file.seek(0)
            json.dump(data, file, indent=4)