"""
Quadratic Equations Solver
Group 2:
Faris Al-Herf
Youssef Al-Muhanna
Omar Al-Bayyebi
Mazen Al-Ghamdi
Hashem Al-Saihati
"""
import customtkinter
from utilities import center_window, QuadraticEquation

customtkinter.set_appearance_mode("system")  # Set the theme (Dark, Light) upon the system preference.
customtkinter.set_default_color_theme("green")  # Set Default theme to green (A builtin color-theme from customtkinter)

# Dictionary to hold our main configuration
config = {
    "windowTitle": "Math: Quadratic Equations",
    "topLevelTitle": "Math: Quadratic Equations | Graph",
    "title": "Quadratic Equations Solver",
    "description": "Our app helps you solve an equation of the form ax^2 + bx + c = 0",
    "appWidth": 900,
    "appHeight": 600,
    "topLevel": {"appWidth": 700, "appHeight": 600}
}
print(config['title'])


class ToplevelWindow(customtkinter.CTkToplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        center_window(self, config["topLevel"]["appWidth"], config["topLevel"]["appHeight"])
        self.title(config["topLevelTitle"])
        self.after(100, self.lift)  # Workaround for bug where main window takes
        # focus (https://github.com/TomSchimansky/CustomTkinter/issues/1486).


class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.toplevel_window = None
        self.label_a = customtkinter.CTkLabel(self, text="Enter the value of a:", width=30, height=25, corner_radius=7)
        self.label_a.grid(row=0, column=0, padx=10, pady=20)

        self.entry_a = customtkinter.CTkEntry(self, placeholder_text="Enter a", width=200, height=30, border_width=2,
                                              corner_radius=10)
        self.entry_a.grid(row=0, column=1, padx=10)

        self.label_b = customtkinter.CTkLabel(self, text="Enter the value of b:", width=30, height=25, corner_radius=7)
        self.label_b.grid(row=1, column=0, padx=10, pady=20)

        self.entry_b = customtkinter.CTkEntry(self, placeholder_text="Enter b", width=200, height=30, border_width=2,
                                              corner_radius=10)
        self.entry_b.grid(row=1, column=1, padx=10)

        self.label_c = customtkinter.CTkLabel(self, text="Enter the value of c:", width=30, height=25, corner_radius=7)
        self.label_c.grid(row=2, column=0, padx=10, pady=20)

        self.entry_c = customtkinter.CTkEntry(self, placeholder_text="Enter c", width=200, height=30, border_width=2,
                                              corner_radius=10)
        self.entry_c.grid(row=2, column=1, padx=10, pady=5)

        self.solve_button = customtkinter.CTkButton(self, text="Solve", command=self.solve_equation, text_color="black",
                                                    font=customtkinter.CTkFont(size=16), height=30)
        self.solve_button.grid(row=4, column=0, padx=20, pady=20)

        self.graph_button = customtkinter.CTkButton(self, text="Graph", command=self.graph_equation, text_color="black",
                                                    font=customtkinter.CTkFont(size=16), height=30)
        self.graph_button.grid(row=4, column=1, padx=20, pady=20)

        self.label_solutions = customtkinter.CTkLabel(self, text="", text_color="#009900",
                                                      font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_solutions.grid(row=3, column=0, columnspan=2, padx=10)

    # from documentation of customtkinter
    # To call TopLevelWindow class.
    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def solve_equation(self):
        # Solving the equation with proper try & except
        try:
            # We use QuadraticEquation class from utilities file
            quadratic = QuadraticEquation(a=self.entry_a.get(), b=self.entry_b.get(),
                                          c=self.entry_c.get())
            solutions = quadratic.solve()
            text = "The solutions are: "
            for i in solutions:
                text += str(i) + ", "
                text = text[:-2]  # This is to remove the last comma. (Due to the above for loop)
                self.label_solutions.configure(text=text, text_color="#009900")

        except ValueError as err:
            # This except block occur when there is an error
            # Such as: A coefficent is 0, or provided entries are not integers or no solution.
            self.label_solutions.configure(
                text=err,
                text_color="#db324d")

    def graph_equation(self):
        try:
            quadratic = QuadraticEquation(a=self.entry_a.get(), b=self.entry_b.get(), c=self.entry_c.get())
            quadratic.solve()
            quadratic.plot(self.toplevel_window)
        except ValueError as err:
            self.label_solutions.configure(
                text=err,
                text_color="#db324d")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title(config["windowTitle"])  # Setting window title
        center_window(self, config["appWidth"],
                      config["appHeight"])  # A utility function that Sets geometry and center window

        self.grid_columnconfigure(0, weight=1)

        self.title_label = customtkinter.CTkLabel(self, text=config["title"],
                                                  font=customtkinter.CTkFont(size=30, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=10, pady=(40, 0), sticky="ew", columnspan=2)
        self.description_label = customtkinter.CTkLabel(self,
                                                        text=config["description"],
                                                        font=customtkinter.CTkFont(size=18))
        self.description_label.grid(row=1, column=0, padx=10, pady=(0, 20), sticky="ew", columnspan=2)

        self.theme_label = customtkinter.CTkLabel(self, text="Change theme:",
                                                  font=customtkinter.CTkFont(size=15))
        self.theme_label.grid(row=2, column=0, padx=20, pady=(10, 0))

        self.theme_menu = customtkinter.CTkOptionMenu(self, values=["System", "Dark", "Light"],
                                                      text_color="black",
                                                      command=self.change_theme)
        self.theme_menu.grid(row=3, column=0, padx=20, pady=(10, 10))

        self.my_frame = MyFrame(master=self, corner_radius=10)
        self.my_frame.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

    def change_theme(self, new_theme: str):
        customtkinter.set_appearance_mode(new_theme)


app = App()
app.mainloop()
