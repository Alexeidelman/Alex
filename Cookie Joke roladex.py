import tkinter as tk
from tkinter import PhotoImage

class ClickingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Clicking Game")

        self.cookie_jokes = [
            "Why did the cookie go to therapy? Because it felt crumbly on the inside!",
            "Why did the cookie apply for a job? It wanted to make dough!",
            "Why are cookies so good at making decisions? They always know what's best for the batter!",
            "Why don't cookies ever feel guilty? Because they always crumble under pressure!",
            "Why did the chocolate chip cookie break up with the oatmeal cookie? It found the relationship too nuts!"
        ]

        self.current_index = 0  # Initialize the index of the current prompt

        self.button_image = PhotoImage(file="cookie.gif")

        self.label = tk.Label(self.master, text="Welcome to the Cookie Joke Game!", font=("Arial", 14))
        self.label.pack(pady=20)

        self.button = tk.Button(self.master, image=self.button_image, command=self.show_cookie_joke, borderwidth=0)
        self.button.image = self.button_image
        self.button.pack(pady=10)

    def show_cookie_joke(self):
        # Display the current prompt
        prompt = self.cookie_jokes[self.current_index]
        self.label.config(text=prompt)

        # Increment the index for the next prompt
        self.current_index = (self.current_index + 1) % len(self.cookie_jokes)

if __name__ == "__main__":
    root = tk.Tk()
    game = ClickingGame(root)
    root.mainloop()
