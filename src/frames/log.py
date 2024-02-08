import customtkinter
import datetime
from ..loader import *


class LogFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        self.master = master
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.values = ['Today', 'Yesterday', 'Last week', 'All']
        self.variable = customtkinter.StringVar(value=self.values[0])

        self.display_log()
        self.add_buttons()

    def display_log(self):
        text = customtkinter.CTkTextbox(master=self)
        text.grid(row=1, column=0, padx=(10, 10), pady=10, sticky='news', columnspan=len(self.values))
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        last_week_date = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
        with open(LOG_PATH, 'r') as log:
            for line in log.readlines():
                date = datetime.datetime.strptime(line.split(' | ')[0], '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d')
                if self.variable.get() == 'Today':
                    if today in line:
                        text.insert(0.0, line)
                elif self.variable.get() == 'Yesterday':
                    if yesterday in line:
                        text.insert(0.0, line)
                elif self.variable.get() == 'Last week':
                    if last_week_date <= date <= today:
                        text.insert(0.0, line)
                else:
                    text.insert(0.0, line)
        text.configure(state='disabled')

    def add_buttons(self):
        for i, value in enumerate(self.values):
            radiobutton = customtkinter.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobutton.grid(row=0, column=i, padx=10, pady=(10, 0), sticky='news')

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)
