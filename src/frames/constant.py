import customtkinter
from ..task import Task


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
