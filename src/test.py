import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x150")
        self.grid_columnconfigure(0, weight=1)

        self.button = customtkinter.CTkButton(self, text="my button", font=('Segoe UI', 13, 'normal'))
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="news", columnspan=2)

        self.button1 = customtkinter.CTkButton(self, text="my button")
        self.button1.grid(row=1, column=0, padx=20, pady=20, sticky="news", columnspan=2)


app = App()
app.mainloop()

from tkinter import font

root = customtkinter.CTk()
print(font.nametofont('TkTextFont').actual())
