import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class QuadraticEquation:
    def __init__(self, a, b, c):
        self.x2 = None
        self.x1 = None
        self.discriminant = None
        try:
            self.a = float(a)
            self.b = float(b)
            self.c = float(c)
        except ValueError:
            raise ValueError("Invalid Entry: Coefficients must be number")

    """
        Return tuple (x1, x2) | or (x1) | or err (no solution).
    """
    def solve(self):
        if self.a == 0:
            raise ValueError("Invalid Entry: Coefficient a cannot be zero")

        self.discriminant = (self.b ** 2) - (4 * self.a * self.c)
        denominator = 2 * self.a
        # No Real solutions only complex solutions:
        if self.discriminant < 0:
            raise ValueError("No solutions")
        elif self.discriminant == 0:
            return -self.b / denominator,  # One solution returned as a single tuple.

        # Many solutions
        # We're just applying the quadratic formula here -b+-sqrt(b^2-4ac)/2a
        discriminant = math.sqrt(self.discriminant)
        self.x1 = (-self.b + discriminant) / denominator
        self.x2 = (-self.b - discriminant) / denominator

        return self.x1, self.x2

    def plot(self, topLevelWindow):
        if self.discriminant < 0:
            # We can't plot! No solutions!
            raise ValueError("Unable to plot: No Solutions")
        elif self.discriminant == 0:
            x = -self.b / (2 * self.a)

            # X-values for the plot
            x_vals = np.linspace(x - 1, x + 1, 100)

            # Y-values for the plot
            y_vals = self.a * (x_vals - x) ** 2 + self.c

            # Create the plot
            fig, ax = plt.subplots()
            ax.plot(x_vals, y_vals)
            ax.scatter(x, self.c, color='red')  # plot the one solution as a red dot
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_title('Quadratic Equation with One Root')
            canvas = FigureCanvasTkAgg(fig, master=topLevelWindow)
            canvas.draw()
            canvas.get_tk_widget().pack()
        else:

            """
                Suppose I have x1: 7, x2: -2
                I want to determine the domain dynamically from my roots.
                I calculate the min(7, -2) - 1 ---> will give me -3.0
                I calculate the max(7, -2) +1 ---> will give me 8.0
                As we can see, this allows us to better visualize the domain.
            """
            x_min = min(self.x1, self.x2) - 1
            x_max = max(self.x1, self.x2) + 1

            x = np.linspace(x_min, x_max, 100)  # Generating the domain with numpy linspace
            y = (self.a * x ** 2) + self.b * x + self.c  # Range

            y = np.around(y, decimals=2)  # This rounds the Y to the nearest 2 decimal places, to avoid showing
            # 7.009345134851345134 (Basically large decimal places).
            # Plot
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.plot(x, y, linewidth=2, color='green')

            # Horizontal line for x-intercept
            ax.axhline(y=0, linewidth=1, color='black', linestyle='--')

            # Add vertical lines for x-intercepts
            ax.axvline(x=self.x1, linewidth=1, color='red', linestyle='--')
            ax.axvline(x=self.x2, linewidth=1, color='red', linestyle='--')

            # Set axis labels and title
            ax.set_xlabel('X values', fontsize=14)
            ax.set_ylabel('y', fontsize=14)
            ax.set_title('Quadratic Equation', fontsize=16)

            # Adjust axis limits and tick marks
            ax.set_xlim([x_min, x_max])
            x_ticks = np.arange(x_min, x_max + 1)
            ax.set_xticks(x_ticks)
            ax.set_xticklabels(x_ticks, fontsize=12)
            y_ticks = np.arange(min(y), max(y) + 1)
            ax.set_yticks(y_ticks)
            ax.set_yticklabels(y_ticks, fontsize=12)

            canvas = FigureCanvasTkAgg(fig, master=topLevelWindow)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)


# Taken from Google (How to center a tkinter window).
def center_window(window, appWidth, appHeight):
    # To open the window at the center of the screen, code taken from Google
    app_center_coordinate_x = (window.winfo_screenwidth() // 2) - (appWidth // 2)
    app_center_coordinate_y = (window.winfo_screenheight() // 2) - (appHeight // 2)

    window.geometry(f"{appWidth}x{appHeight}+{app_center_coordinate_x}+{app_center_coordinate_y}")


