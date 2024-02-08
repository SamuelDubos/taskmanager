import customtkinter
from ..task import Task


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
